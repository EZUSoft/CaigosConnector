# -*- coding: utf-8 -*-
"""
/***************************************************************************
 clsDatenbank: Gemeinsame Basis für QGIS2 und QGIS3
  18.07.2018 V0.6
  - Komplettüberarbeitung Datenbankzugriff
 
  27.10.2017 V0.5
  - DBFAnpassen definiert: Löschen von DPF-Spalten
  09.10.2017 V0.5
  - Shapeexport optional Darstellung (im Shapeverzeichnis) speichern
  04.07.2017 V0.4
  - GISDB Tab jetzt auch an Punkten (Fehler im Select)
  - CheckVerbDaten umgebaut
  - CAIGOS 2016: VectorLayerPath kein setsrid mehr notwendig
  
  23.08.2016 V0.3
  - Layerreihenfolge nach Priorität zusätzlich nach Layertyp
  - sqlAttParam4IDandArt Reihenfolge der Teillinien (testweise) umgekehrt 
  
  09.08.2016 V0.3
  - optionale 3D Anbindung
  - Einbindung SQL für Kreis
  
  20.06.2016 V0.2
  - Einbindung der GIDDB Sachdaten
                                 A QGIS plugin
 CAIGOS-PostgreSQL/PostGIS in QGIS darstellen
                              -------------------
        begin                : 2016-04-18
        git sha              : $Format:%H$
        copyright            : (C) 2016 by EZUSoft
        email                : qgis (at) makobo.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from osgeo import ogr # 02.10.17 muss bei 2.99 am Anfang kommen
from qgis.core import *
from qgis.utils import os, sys
try:
    from PyQt5.QtCore import QSettings, Qt
    from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlError
    from PyQt5 import QtGui
    myqtVersion = 5
    QString = type("")

except:
    from PyQt4.QtCore import QSettings, Qt
    from PyQt4.QtSql import QSqlDatabase, QSqlQuery, QSqlError
    from PyQt4 import QtGui
    def QgsDataSourceUri():
        return QgsDataSourceURI()
    myqtVersion = 4



try:
    from fnc4all import *
    from fnc4CaigosConnector import *
    from modCGSqlCodes import *
except:
    from .fnc4all import *
    from .fnc4CaigosConnector import *
    from .modCGSqlCodes import *
    
import os.path
import tempfile
import sqlite3
import locale
import uuid


"""
/***************************************************************************/
                    Teil1: Klasse Datenbankzugriffe
/***************************************************************************/
"""
class pgOpenDatabase():
    def __init__( self, service, host, port, dbname, uid, pwd):
        self.Fehler = None
        # 19.07.18: GUID als Name, da unter QGIS3.2 ein Löschen der DB bei offenen Recordset zum Absturz führt
        self.ConNameByGIUD=str(uuid.uuid4())
        self.QSqlDB = QSqlDatabase.addDatabase("QPSQL", self.ConNameByGIUD )
        """
        if service == "":
            self.QSqlDB.setHostName(host)
            self.QSqlDB.setPort(int(port))
        else:
            self.QSqlDB.setService(service)
        
        self.QSqlDB.setDatabaseName(dbname)
        self.QSqlDB.setUserName(uid)
        self.QSqlDB.setPassword(pwd)
        """
        
        # 19.08.18:
        # irgendwie ist/war das doppelt, die Uri wird für andere Programmteile benötigt
        # und in der alten Version wurde die auch zur DB-Anbindung genutzt: db.setConnectOptions( conninfo0 )
        self.uri = QgsDataSourceUri()
        if service == "":
            self.uri.setConnection( host, port, dbname, uid, pwd )
        else:
            self.uri.setConnection(service, dbname, uid, pwd )
        
        self.QSqlDB.setConnectOptions( self.uri.connectionInfo() )

    
    def GetConnString(self):
        return self.uri.connectionInfo()

    # Überlegen, ob das Open gleich mit ins Ini kommt
    def Open(self):
        if self.QSqlDB.open():
            return self.QSqlDB
        else:
            err = (u"pgOpenDatabase:"  + '\n' +
            "Text: " + self.QSqlDB.lastError().text() +  '\n' +
            "Type: " + str(self.QSqlDB.lastError().type()) +  '\n' +
            "Number: " + str(self.QSqlDB.lastError().number()) )
            self.Fehler =  (toUnicode(err))
            self.QSqlDB = None

    def getFehler(self):
        return self.Fehler
    
    def OpenRecordset (self, SQLString):
        # in Python 3 hängt rs scheinbar noch an der QSqlDatabase
        # weshalb nach zerstören der pgDatabaseNeu() Instanz  bzw. bei  QSqlDatabase.removeDatabase(self.conname)
        # beim Zugriff ein Absturz auftritt
        rs = QSqlQuery(self.QSqlDB)
        if rs.exec_( SQLString ):
            return rs
        else:
            err = (u"exec_( SQLString ):"  + "\n" +
            "Text: " + rs.lastError().text() +  "\n" +
            "Type: " + str(rs.lastError().type()) +  "\n" +
            "Number: " + str(rs.lastError().number()) +  "\n" +
            "SQL: " + SQLString)
            self.Fehler =  (toUnicode(err))            
    
    def CheckVerbDaten(self,idxVersion = None, EPSG=None, CGSignaturPfad=None,CGProjektName=None,conninfo=None, NurFehler=False):
        Meldung =""; Fehler=""; Warnung = ""
        if not idxVersion:
            idxVersion = GetCGVersion()  
        if not EPSG:
            EPSG = GetEPSG()  
        if not CGSignaturPfad:
            CGSignaturPfad = GetCGSignaturPfad()    
        if not CGProjektName:
            CGProjektName = GetCGProjektName()      
        if not conninfo:
            conninfo = self.GetConnString()
        
        # 16.08.18 DB-Check war deaktiviert!?
        #          --> neu aktiviert
        QApplication.setOverrideCursor(Qt.WaitCursor)
        if self.Open():
            Meldung= u"Datenbankverbindung erfolgreich"
            if self.OpenRecordset("Select * from pointssqlspatial limit 1"):
                Meldung = Meldung + "\n" if Meldung else ""
                Meldung = Meldung + u"CAIGOS Geodatentabelle in der Datenbank gefunden"
            else:
                Fehler=Fehler + "\n" if Fehler else ""
                Fehler=Fehler + u"Keine CAIGOS Geodatentabelle in der Datenbank gefunden:\n" + "\n"       
        else:
            Fehler= u"Datenbankverbindung schlug fehl:\n" + self.getFehler() + "\n"
        QApplication.restoreOverrideCursor()
        
        if EPSG == None or EPSG == "" or EPSG == 0 or EPSG == "0":
            Fehler=Fehler + "\n" if Fehler else ""
            Fehler= Fehler + "EPSG-Code nicht definiert"
        
        if CGProjektName == "":
            Fehler=Fehler + "\n" if Fehler else ""
            Fehler=Fehler+"Kein Projektname festgelegt"
    
        if CGSignaturPfad == "":
            Warnung=Warnung + "\n" if Warnung else ""
            Warnung=Warnung+toUnicode("CAIGOS Signaturverzeichnis nicht festgelegt\n  ->Es können keinen SVG-Symbole generiert werden")           
        else:
            sigPfad = CGSignaturPfad    
            if idxVersion  == 1: sigPfad = sigPfad  + CGProjektName + '/'

            if os.path.exists(sigPfad):
                Meldung = Meldung + "\n" if Meldung else ""
                Meldung = Meldung + "CAIGOS Signaturverzeichnis gefunden"
            else:
                Warnung = Warnung + "\n" if Warnung else ""
                Warnung = Warnung +  u"\nCAIGOS Signaturverzeichnis ('" + sigPfad + toUnicode("') nicht gefunden\n  ->Es können keine SVG-Symbole generiert werden")            
        
        if Fehler:
            QMessageBox.critical( None, u"Es sind Fehler aufgetreten", Fehler)
            return False
        else:  
            if not NurFehler:
               QMessageBox.information( None,u'Folgende Tests waren erfolgreich:',Meldung)
            if Warnung:
               QMessageBox.information( None,u'Konfigurationsproblem',Warnung)
            return True             

 
    def __del__(self):
        if self.QSqlDB:
            self.QSqlDB.close()
            del(self.QSqlDB)
            QSqlDatabase.removeDatabase(self.ConNameByGIUD) 

class pgCurrentDB(pgOpenDatabase):
    def __init__( self ):
        s = QSettings( "EZUSoft", fncProgKennung() )
        service = s.value( "service", "" )
        host    = s.value( "host", "localhost" )
        port    = s.value( "port", "5432" )
        dbname  = s.value( "dbname", "cgTestProjekt" )
        uid     = s.value( "uid", "caigos" )
        pwd     = s.value( "pwd", "*****" )
        pgOpenDatabase.__init__( self, service, host, port, dbname, uid, pwd)
        pgOpenDatabase.Open(self)

        
    def __del__(self):
        pgOpenDatabase.__del__(self)

def pgCurrendLookUp (sqlStringMitEinemFeld, OffeneDB = None, FldNum = 0):  
# aktuell ungenutzt
    if OffeneDB:
        AktDB = OffeneDB
    else:
        AktDB = pgCurrentDB()
        if not AktDB.Open():
            del(AktDB)
            return None
            
    AktRS= AktDB.OpenRecordset (sqlStringMitEinemFeld)
    AktRS.next()
    Wert = AktRS.value(FldNum)
    del(AktRS)
    if not OffeneDB:
        del (AktDB)
    return Wert
        
    
"""
/***************************************************************************/
                    Teil2: nachschlagen in der Registy
/***************************************************************************/
"""
def GetCGVersion():
    s = QSettings( "EZUSoft", fncProgKennung() )
    try:
        return int(s.value( "cgversion"))
    except:
        return None

def sGetCGVersion():
    s = QSettings( "EZUSoft", fncProgKennung() )
    try:
        if int(s.value( "cgversion"))==0: return "V11"
        if int(s.value( "cgversion"))==1: return "V2016"
    except:
        return None
        
def GetEPSG():
    s = QSettings( "EZUSoft", fncProgKennung() )
    try:
        return int(s.value( "epsg"))
    except:
        return None

def GetQSVGSignaturPfad():
    # SVG's im Shape-Pfad oder im temporären Projektpfad speichern
    # Überarbeitung 15.02.18
    s = QSettings( "EZUSoft", fncProgKennung() )
    if s.value( "bSHPexp") == "Ja": # and s.value("txtSHPDir","nicht festgelegt") != "nicht festgelegt":
        return s.value("txtSHPDir") + '/'
    else:      
        return tempfile.gettempdir() + "/{D5E6A1F8-392F-4241-A0BD-5CED09CFABC7}/" + 'projekt_svg' + '/' + GetCGProjektName() + '/'
    #return os.path.dirname(__file__) + "/" + 'projekt_svg' + '/' + GetCGProjektName() + '/'          

def GetCGSignaturPfad():
    s = QSettings( "EZUSoft", fncProgKennung() )
    return s.value("cgsignaturpfad","nicht festgelegt")

def GetCGProjektName():
    s = QSettings( "EZUSoft", fncProgKennung() )
    return s.value( "cgprojektname")  

def GetDBname():
    s = QSettings( "EZUSoft", fncProgKennung() )
    return s.value( "dbname")



"""
/***************************************************************************/
                    Teil3: other stuff
                           --> Datenbankarbeit und SQL-Codes sollten mal getrennt werden
/***************************************************************************/
"""


"""
/***************************************************************************/
                    Teil4: Zugriffe auf PostgreSQL
/***************************************************************************/
"""
def dbLayerStrukturByID(LayerID, AktDB = None):
    # Lesen und übergeben
    #      0        1       2      3
    # Fachschale, Thema, Gruppe, Layer
    if AktDB:
        db1=AktDB
    else:
        db1 = pgCurrentDB()
    rs1 = db1.OpenRecordset (sqlStruk4Layer(LayerID))
    rs1.next() # erster (und letzer) Datensatz
    ausg = rs1.value(0),rs1.value(1),rs1.value(2),rs1.value(3)
    del (rs1)
    if not AktDB: del (db1)
    return ausg

def db2sqlGisDBShortFieldName (TabName, AktDB = None):
    # Erzeugt einen SQL-String für den Zugriff auf eine GISDB mit kurzen Aliasnamen
    if AktDB:
        db=AktDB
    else:
        db = pgCurrentDB()
        
    rs = db.OpenRecordset("select column_name from information_schema.columns where table_name='" + TabName + "'")
    s = "select "
    while (rs.next()) :
        if rs.value(0).replace(TabName + '_','') == 'objid':
            s = s + rs.value(0) + " as objidgistab," # objid wäre sonnst doppelter Name in Abfrage, da Spalte objid auch in GeoTab
        else:
            s = s + rs.value(0) + " as " + rs.value(0).replace(TabName + '_','') + ","
    # letztes , weg
    s = s[:-1]
    s=  s + " FROM " + TabName 
    del rs
    if not AktDB: del (db)
    return s


def dbExistsGISDBTab(GISDBTabName, AktDB = None):
    # ermittlt, ob eine bestimmte GISDB-Tabelle existiert
    # --> Tabellenname und ein Feld <tabname>_objid muss exisitieren
    if AktDB:
        db=AktDB
    else:
        db = pgCurrentDB()

    sDB=GISDBTabName.lower()
    sSQL=("SELECT True FROM pg_attribute WHERE attrelid = (SELECT oid FROM pg_class WHERE relname = '%s') AND attname = '%s_objid'")%(sDB,sDB)
    rs=db.OpenRecordset(sSQL)
    Antw=rs.size()==1
    del rs
    if not AktDB: del (db)
    return (Antw) 



def VectorLayerPath ( Art, ConnInfo, Epsg, LayerID, b3DDar , GISDbTab, cgVersion, bShape):
    bDeltaTexte = True # evtl. später mal optional 
    uri = None
    geoTabName=GeoTabName4Art(Art)
    if LayerID:
        where="layerid='%s'" % (LayerID)
    else:
        where =""
    
    if b3DDar:
        ken3D="Z"
    else:    
        ken3D=""
        
    if GISDbTab:
        if bShape:
            # Tabellennamen aus Spalte kürzen, da Shape nur 10 Zeichen
            sql4GISDB = db2sqlGisDBShortFieldName(GISDbTab).replace("\\","")
            sqlZusatz = (' left join (%s) as gtab on %s.objid = gtab.objidgistab') % (sql4GISDB,geoTabName)
        else:
            sqlZusatz = (' left join %s  on %s.objid = %s.%s_objid') % (GISDbTab,geoTabName,GISDbTab,GISDbTab)

    else:
        sqlZusatz=""
    
    if myQGIS_VERSION_INT() < 21200: # ab Lyon
        # Unterabfrage definieren - macht das Ganze aber ziemlich langsam und ist bei Essen nicht mehr notwendig
        IndexGen1="(SELECT row_number() over () AS _uid_,* FROM "
        IndexGen2=" as dummy)"
        Key="_uid_"
    else:
        IndexGen1 =''
        IndexGen2 =''
        Key="objid"
    
    #08.08.16:
    # table='%s' --> table=\"%s\": sicherheitshalber für alle, obwohl es nur beim Kreis Probleme gab
    
    # in CAIGOS 2016 steht der EPSG-Code jetzt korrekt in PostGIS
    # der neue Code ist irgendwie schlecht aus dem alten ableitbar --> 2 komplett verschiedene Varianten 
    if cgVersion == 0: # alte Variante mit EPSG-Einabu
        if Art == 0: # Point      
            table=("%s(select *, st_setsrid(st_translate(shape, deltar, deltah),%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%s type=Point%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)        
        if Art == 1: # Line
            table=("%s(select *,st_setsrid(shape,%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 2: # Kreis
            # 05.10.16: Kreis als Fläche
            #table= ("%s(select *,st_setsrid(shape,%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            #uri=("%s key='%s' srid=%d type=CircularString table='%s' (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, table, where)
            table=("%s(select *,st_setsrid('CurvePolygon(' || array_to_string( array_append( array_append((string_to_array(ST_AsText(shape),','))[1:3], substring((string_to_array(ST_AsText(shape),','))[5], 1,length((string_to_array(ST_AsText(shape),','))[5])-1)),(string_to_array( substring(ST_AsText(shape),19),','))[1]),',') || '))',%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            if myQGIS_VERSION_INT()  < 21200:
                uri=None
            else:
                uri=("%s key='%s' srid=%d type=CurvePolygon%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)

        if Art == 3: # Text
            sShape = "st_translate(shape, deltar, deltah)" if bDeltaTexte else "shape"
            table=("%s(select *,st_setsrid(" + sShape  + " ,%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=Point%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 31: # Textreferenzpfeil
            # 1. Punkt steht in "shape" 
            # 2. Punkt "st_translate(shape, deltar, deltah)"           
            sShape = "st_makeline(shape, st_translate(shape, deltar, deltah))"
            table=("%s(select *,st_setsrid(" + sShape  + " ,%d) as sid_shape from %s %s WHERE isdelta = 'J' and (deltar * deltah) != 0)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 4: # Bemaßung
            uri = None
        if Art == 5: # Polylinie
            table=("%s(select *,st_setsrid(shape,%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)     
        if Art == 6: # Fläche
            table=("%s(select *,st_setsrid(shape,%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=MultiPolygon%s table=\"%s\"(sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
    else:
        if Art == 0: # Point      
            table=("%s(select *, st_translate(shape, deltar, deltah) as geom from %s %s)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%s type=Point%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)        
        if Art == 1: # Line
            table=("%s(select *,shape as geom from %s %s)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 2: # Kreis
            table=("%s(select *,st_setsrid('CurvePolygon(' || array_to_string( array_append( array_append((string_to_array(ST_AsText(shape),','))[1:3], substring((string_to_array(ST_AsText(shape),','))[5], 1,length((string_to_array(ST_AsText(shape),','))[5])-1)),(string_to_array( substring(ST_AsText(shape),19),','))[1]),',') || '))',%d) as geom from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            if myQGIS_VERSION_INT()  < 21200:
                uri=None
            else:
                uri=("%s key='%s' srid=%d type=CurvePolygon%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 3: # Text
            sShape = "st_translate(shape, deltar, deltah)" if bDeltaTexte else "shape"
            table=("%s(select *," + sShape  + " as geom from %s %s)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=Point%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 31: # Textreferenzpfeil
            # 1. Punkt steht in "shape" 
            # 2. Punkt "st_translate(shape, deltar, deltah)"           
            sShape = "st_makeline(shape, st_translate(shape, deltar, deltah))"
            table=("%s(select *," + sShape  + " as geom from %s %s WHERE isdelta = 'J' and (deltar * deltah) != 0)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 4: # Bemaßung
            uri = None
        if Art == 5: # Polylinie
            table=("%s(select *,shape as geom from %s %s)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)     
        if Art == 6: # Fläche
            table=("%s(select *,shape as geom from %s %s)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=MultiPolygon%s table=\"%s\"(geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
    return uri
    

"""    
def sqlLayerIsEmpty( Art, LayerID):
    geoTabName=GeoTabName4Art(Art)
    sSQL = "SELECT count(*) FROM " + geoTabName + " where layerid='" + LayerID + "'"
    db1 = pgCurrentDB()
    db1.Open()
    rs1 = db1.OpenRecordset (sSQL)
    rs1.next() # erster (und letzer) Datensatz
    if rs1.value(0) > 0:
        Wert = True
    else:    
        Wert = False
    del (rs1)
    del (db1)
    return Wert
"""    

def AttDefID4Layer( db, LayerID, cgUser):
    # Attributdefinitionen der Ebene auslesen
    sqlString=("select defid from prptable where layerid='%s' and usernr='%s'") %(LayerID, cgUser)
    rs = db.OpenRecordset(sqlString)
    rs.next() # erster (und letzer) Datensatz
    Wert = rs.value(0)
    del(rs)
    return Wert

def AttDefName4ID (db,DefID):
    # Name der Attributdefinition aus der DefID ermitteln
    sqlString=("SELECT defname FROM  deftable WHERE defid ='%s'") % (DefID)
    rs = db.OpenRecordset(sqlString)
    rs.next() # erster (und letzer) Datensatz
    Wert = rs.value(0)
    del(rs)
    return Wert

def NeedLine4TextLayer(db,LayerID, cgUser):  
    sqlString= sqlAtt4Massstab ( 3,None, cgUser)
    sqlString = "select count(*) from (" + sqlString + ") as t1 inner join ("
    sqlString = sqlString + ("SELECT DISTINCT textssqlspatial.defid FROM textssqlspatial LEFT JOIN deftable ON textssqlspatial.defid =deftable.defid where layerid='%s' and textssqlspatial.defid != '{00000000-0000-0000-0000-000000000000}' union all select defid from prptable where layerid='%s' and usernr='%s'")%(LayerID,LayerID,cgUser)
    sqlString = sqlString + ") as t2 on t1.adid = t2.defid"

    rs = db.OpenRecordset(sqlString)
    rs.next() # erster (und letzer) Datensatz
    Wert=rs.value(0) != 0
    del(rs)
    return Wert

def DBFAnpassen (shpdat, bOnlyDarField, bNoGISDBIntern, likeShpDat = None, negativliste=None, positivliste=None):
    paramanz=0
    if likeShpDat: paramanz+=1
    if negativliste: paramanz+=1
    if positivliste: paramanz+=1
    if paramanz > 1: return -1
    delAnz=0
    
    source = ogr.Open(shpdat, update=True)
    if source is None:
        addFehler(tr('ogr: can not open: ') + shpdat)
        return
    layer = source.GetLayer()
    laydef = layer.GetLayerDefn()
    
    # alle Spaltennamen ermitteln
    bOrgSHP = False
    schema = []
    for n in range(laydef.GetFieldCount()):
        if laydef.GetFieldDefn(n).name == "shape": bOrgSHP = True # shape ist immer letzte Spalte der CAIGOS-Geodaten
        schema.append(laydef.GetFieldDefn(n).name)
    

    if bNoGISDBIntern:
        go = False
        for sp in schema:
            if sp == "shape":
                go=True  # shape ist immer letzte Spalte der CAIGOS-Geodaten

            if go :
                if sp in ["id", "objidgista", "pmfmark","pmfkey", "datestampn", "timestampn","datestampe", "timestampe"]:
                    layer.DeleteField(laydef.GetFieldIndex(sp))
                    delAnz+=1 
                
    if bOnlyDarField and bOrgSHP:
        for sp in schema:
            if sp == "shape":
                layer.DeleteField(laydef.GetFieldIndex("shape"))
                break  # shape ist immer letzte Spalte der CAIGOS-Geodaten

            if not sp in ["defid", "alpha", "pstext"]:
                layer.DeleteField(laydef.GetFieldIndex(sp))
                delAnz+=1 

                
    if likeShpDat:
        print("hier")
        likesource = ogr.Open(likeShpDat, update=True)
        likelayer = likesource.GetLayer()
        likelaydef = likelayer.GetLayerDefn()
        likeschema = []
        for n in range(likelaydef.GetFieldCount()):
            likeschema.append(likelaydef.GetFieldDefn(n).name) 
        likesource.Destroy()
        for sp in schema:
            if not sp in likeschema:
                layer.DeleteField(laydef.GetFieldIndex(sp))
                delAnz+=1   

    elif positivliste:
        # alle anderen löschen
        for sp in schema:
            if not sp in positivliste:
                layer.DeleteField(laydef.GetFieldIndex(sp))
                delAnz+=1
    elif negativliste:
        for sp in schema:
            if sp in negativliste:
                layer.DeleteField(laydef.GetFieldIndex(sp))  
                delAnz+=1
    source.Destroy()   
    return delAnz
    
if __name__ == "__main__":
    print (dbLayerStrukturByID('{893F0B09-8BE1-4A14-91A3-EB3AD7D3D784}'))
    p1="dbname='cgStrassendokumentation' host=10.201.201.21 port=5432 user='CAIGOS' password='CAIGOS'"
    vlp = VectorLayerPath (5,p1,25833, '{623E894A-9944-4F62-A337-DF713DC42439}',False, 'd4ustdok_qs', 0, True)
    print (vlp)
    #print (AktDB.CheckVerbDaten(None,None,None,None, True))
    #print ("crashtest1")



