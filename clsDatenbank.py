# -*- coding: utf-8 -*-
"""
/***************************************************************************
 A QGIS plugin
CaigosConnector: Connect CAIGOS-GIS with QGIS
        copyright            : (C) 2019 by EZUSoft
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







































from osgeo import ogr 
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







class pgOpenDatabase():
    def __init__( self, service, host, port, dbname, uid, pwd):
        self.Fehler = None

        self.ConNameByGIUD=str(uuid.uuid4())
        self.QSqlDB = QSqlDatabase.addDatabase("QPSQL", self.ConNameByGIUD )











        



        self.uri = QgsDataSourceUri()
        if service == "":
            self.uri.setConnection( host, port, dbname, uid, pwd )
        else:
            self.uri.setConnection(service, dbname, uid, pwd )
        
        self.QSqlDB.setConnectOptions( self.uri.connectionInfo() )

    
    def EZUA098FD21021B43B78B52D0DC3130605D(self):
        return self.uri.connectionInfo()


    def Open(self):
        if not self.QSqlDB:
            return None
        if self.QSqlDB.open():
            return self.QSqlDB
        else:
            err = (u"pgOpenDatabase:"  + '\n' +
            "Text: " + self.QSqlDB.lastError().text() +  '\n' +
            "Type: " + str(self.QSqlDB.lastError().type()) +  '\n' +
            "Number: " + str(self.QSqlDB.lastError().number()) )
            self.Fehler =  (EZUC936D29251B44D4E994497BF023338C7(err))
            self.QSqlDB = None

    def EZU03F45B01171E465F835613DBEE097689(self):
        return self.Fehler
    
    def EZUDCF0989FCCB948B08C56317AE7037619 (self, SQLString):



        rs = QSqlQuery(self.QSqlDB)
        if rs.exec_( SQLString ):
            return rs
        else:
            err = (u"exec_( SQLString ):"  + "\n" +
            "Text: " + rs.lastError().text() +  "\n" +
            "Type: " + str(rs.lastError().type()) +  "\n" +
            "Number: " + str(rs.lastError().number()) +  "\n" +
            "SQL: " + SQLString)
            self.Fehler =  (EZUC936D29251B44D4E994497BF023338C7(err))            
    
    def EZU8011F18E65644E5D9231765F31D7EE19(self,idxVersion = None, EPSG=None, CGSignaturPfad=None,CGProjektName=None,conninfo=None, NurFehler=False):
        Meldung =""; Fehler=""; Warnung = ""
        if not idxVersion:
            idxVersion = EZU1C1D2B936A1D475D8F4C176B585F2301()  
        if not EPSG:
            EPSG = EZU07A28165B1CC4CC09B4AC9235EA3E8E9()  
        if not CGSignaturPfad:
            CGSignaturPfad = EZUEA8B6496E4A94763B4DE5BCE67BA0F14()    
        if not CGProjektName:
            CGProjektName = EZU0239CDC0875B4C7B837227F9004BC5D0()      
        if not conninfo:
            conninfo = self.EZUA098FD21021B43B78B52D0DC3130605D()
        


        QApplication.setOverrideCursor(Qt.WaitCursor)
        if self.Open():
            Meldung= u"Datenbankverbindung erfolgreich"
            if self.EZUDCF0989FCCB948B08C56317AE7037619("Select * from pointssqlspatial limit 1"):
                Meldung = Meldung + "\n" if Meldung else ""
                Meldung = Meldung + u"CAIGOS Geodatentabelle in der Datenbank gefunden"
            else:
                Fehler=Fehler + "\n" if Fehler else ""
                Fehler=Fehler + u"Keine CAIGOS Geodatentabelle in der Datenbank gefunden:\n" + "\n"       
        else:
            Fehler= u"Datenbankverbindung schlug fehl:\n" + self.EZU03F45B01171E465F835613DBEE097689() + "\n"
        QApplication.restoreOverrideCursor()
        
        if EPSG == None or EPSG == "" or EPSG == 0 or EPSG == "0":
            Fehler=Fehler + "\n" if Fehler else ""
            Fehler= Fehler + "EPSG-Code nicht definiert"
        
        if CGProjektName == "":
            Fehler=Fehler + "\n" if Fehler else ""
            Fehler=Fehler+"Kein Projektname festgelegt"
    
        if CGSignaturPfad == "":
            Warnung=Warnung + "\n" if Warnung else ""
            Warnung=Warnung+EZUC936D29251B44D4E994497BF023338C7("CAIGOS Signaturverzeichnis nicht festgelegt\n  ->Es können keinen SVG-Symbole generiert werden")           
        else:
            sigPfad = CGSignaturPfad 





            if os.path.exists(sigPfad):
                Meldung = Meldung + "\n" if Meldung else ""
                Meldung = Meldung + "CAIGOS Signaturverzeichnis gefunden"
            else:
                Warnung = Warnung + "\n" if Warnung else ""
                Warnung = Warnung +  u"\nCAIGOS Signaturverzeichnis ('" + sigPfad + EZUC936D29251B44D4E994497BF023338C7("') nicht gefunden\n  ->Es können evtl. keine SVG-Symbole generiert werden")            
         
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
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
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

def EZU027799A0458943EEB71284D19BAA3FE5 (sqlStringMitEinemFeld, OffeneDB = None, FldNum = 0):  

    if OffeneDB:
        AktDB = OffeneDB
    else:
        AktDB = pgCurrentDB()
        if not AktDB.Open():
            del(AktDB)
            return None
            
    AktRS= AktDB.EZUDCF0989FCCB948B08C56317AE7037619 (sqlStringMitEinemFeld)
    AktRS.next()
    Wert = AktRS.value(FldNum)
    del(AktRS)
    if not OffeneDB:
        del (AktDB)
    return Wert
        
    





def EZU1C1D2B936A1D475D8F4C176B585F2301():
    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    try:
        return int(s.value( "cgversion"))
    except:
        return None

def EZU6F300E76DB074FB99636B535E712DED7():
    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    try:
        if int(s.value( "cgversion"))==0: return "V11"
        if int(s.value( "cgversion"))==1: return "V20xx"
    except:
        return None
        
def EZU07A28165B1CC4CC09B4AC9235EA3E8E9():
    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    try:
        return int(s.value( "epsg"))
    except:
        return None

def EZUA6B299741D5D4E39B1F0ADB88AD47F18():


    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    if s.value( "bSHPexp") == "Ja": 
        return s.value("txtSHPDir") + '/'
    else:      
        return tempfile.gettempdir() + "/{D5E6A1F8-392F-4241-A0BD-5CED09CFABC7}/" + 'projekt_svg' + '/' + EZU0239CDC0875B4C7B837227F9004BC5D0() + '/'


def EZUEA8B6496E4A94763B4DE5BCE67BA0F14():
    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    return s.value("cgsignaturpfad","nicht festgelegt")

def EZU0239CDC0875B4C7B837227F9004BC5D0():
    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    return s.value( "cgprojektname")  

def EZUA079F45549884E088F43D9E667F651BF():
    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    return s.value( "dbname")
















def EZU7F7DA500B4FF409BB13A35E5F7EC2E59(LayerID, AktDB = None):



    if AktDB:
        db1=AktDB
    else:
        db1 = pgCurrentDB()
    rs1 = db1.EZUDCF0989FCCB948B08C56317AE7037619 (EZU1B44A2C9E7584B0BAEB94E020A2B4139(LayerID))
    rs1.next() 
    ausg = rs1.value(0),rs1.value(1),rs1.value(2),rs1.value(3)
    del (rs1)
    if not AktDB: del (db1)
    return ausg

def EZU624FEDF4E3654DEBA88006DC55E937C2 (TabName, GeoTabName, AktDB = None):



    if AktDB:
        db=AktDB
    else:
        db = pgCurrentDB()

    geoFList=[]
    rs = db.EZUDCF0989FCCB948B08C56317AE7037619("select column_name from information_schema.columns where table_name='" + GeoTabName + "'")
    LastGeoTabSpalte = ""
    while (rs.next()) :
        geoFList.append (rs.value(0))
        LastGeoTabSpalte = rs.value(0)


    rs = db.EZUDCF0989FCCB948B08C56317AE7037619("select column_name from information_schema.columns where table_name='" + TabName + "'")
    s = "select "
    while (rs.next()) :

        if rs.value(0)[-6:] == '_objid':
            s = s + rs.value(0) + " as objidgistab," 
        else:

            NeuNam=rs.value(0).replace(TabName + '_','')           
            while NeuNam in geoFList:
                NeuNam="_" + NeuNam               
            s = s + rs.value(0) + " as " + NeuNam + ","
    

    s = s[:-1]
    s=  s + " FROM " + TabName 
    del rs
    if not AktDB: del (db)
    return s, LastGeoTabSpalte


def EZU728F99262A784CE298F08321DF84E81D(GISDBTabName, AktDB = None):


    if AktDB:
        db=AktDB
    else:
        db = pgCurrentDB()

    sDB=GISDBTabName.lower()

    sSQL=("SELECT True FROM pg_attribute WHERE attrelid = (SELECT oid FROM pg_class WHERE relname = '%s') AND attname like '%%\\\_objid'")%(sDB)
    rs=db.EZUDCF0989FCCB948B08C56317AE7037619(sSQL)
    Antw=rs.size()==1
    del rs
    if not AktDB: del (db)
    return (Antw) 

def EZUE2234C86576E4AFDBA184A9078854DDC(GISDBTabName, AktDB = None):
    if AktDB:
        db=AktDB
    else:
        db = pgCurrentDB()

    sDB=GISDBTabName.lower()

    sSQL=("SELECT attname FROM pg_attribute WHERE attrelid = (SELECT oid FROM pg_class WHERE relname = '%s') AND attname like '%%\\\_objid'")%(sDB)
    rs=db.EZUDCF0989FCCB948B08C56317AE7037619(sSQL)
    if rs.size()==1:
        rs.next()
        Antw = rs.value(0)
    del rs
    if not AktDB: del (db)
    return (Antw)

def EZU494640CF7D9A43E19FD083B6B034293A ( Art, ConnInfo, Epsg, LayerID, b3DDar , GISDbTab, cgVersion, bShape, refObjID):


    bDeltaTexte = True 
    uri = None
    LastGeoTabSpalte=None
        
    geoTabName=EZUBB35FE2AD3BE43C0BED5E2BB71976827(Art)
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


            sql4GISDB, LastGeoTabSpalte = EZU624FEDF4E3654DEBA88006DC55E937C2(GISDbTab,geoTabName)
            sql4GISDB.replace("\\","")
            sqlZusatz = (' left join (%s) as gtab on %s.objid = gtab.objidgistab') % (sql4GISDB,geoTabName)
        else:
            sqlZusatz = (' left join %s  on %s.objid = %s.%s') % (GISDbTab,geoTabName,GISDbTab,refObjID)

    else:
        sqlZusatz=""
    
    if EZUC86841CA58BC4846B265D42D4397141D() < 21200: 

        IndexGen1="(SELECT row_number() over () AS _uid_,* FROM "
        IndexGen2=" as dummy)"
        Key="_uid_"
    else:
        IndexGen1 =''
        IndexGen2 =''
        Key="objid"
    


    


    if cgVersion == 0: 
        if Art == 0: 
            table=("%s(select *, st_setsrid(st_translate(shape, deltar, deltah),%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%s type=Point%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)        
        if Art == 1: 
            table=("%s(select *,st_setsrid(shape,%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 2: 



            table=("%s(select *,st_setsrid('CurvePolygon(' || array_to_string( array_append( array_append((string_to_array(ST_AsText(shape),','))[1:3], substring((string_to_array(ST_AsText(shape),','))[5], 1,length((string_to_array(ST_AsText(shape),','))[5])-1)),(string_to_array( substring(ST_AsText(shape),19),','))[1]),',') || '))',%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            if EZUC86841CA58BC4846B265D42D4397141D()  < 21200:
                uri=None
            else:
                uri=("%s key='%s' srid=%d type=CurvePolygon%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)

        if Art == 3: 
            sShape = "st_translate(shape, deltar, deltah)" if bDeltaTexte else "shape"
            table=("%s(select *,st_setsrid(" + sShape  + " ,%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=Point%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 31: 


            sShape = "st_makeline(shape, st_translate(shape, deltar, deltah))"
            table=("%s(select *,st_setsrid(" + sShape  + " ,%d) as sid_shape from %s %s WHERE isdelta = 'J' and (deltar * deltah) != 0)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 4: 
            uri = None
        if Art == 5: 
            table=("%s(select *,st_setsrid(shape,%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)     
        if Art == 6: 
            table=("%s(select *,st_setsrid(shape,%d) as sid_shape from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=MultiPolygon%s table=\"%s\"(sid_shape) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
    else:
        if Art == 0: 
            table=("%s(select *, st_translate(shape, deltar, deltah) as geom from %s %s)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%s type=Point%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)        
        if Art == 1: 
            table=("%s(select *,shape as geom from %s %s)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 2: 
            table=("%s(select *,st_setsrid('CurvePolygon(' || array_to_string( array_append( array_append((string_to_array(ST_AsText(shape),','))[1:3], substring((string_to_array(ST_AsText(shape),','))[5], 1,length((string_to_array(ST_AsText(shape),','))[5])-1)),(string_to_array( substring(ST_AsText(shape),19),','))[1]),',') || '))',%d) as geom from %s %s)%s") % (IndexGen1,Epsg,geoTabName,sqlZusatz,IndexGen2)
            if EZUC86841CA58BC4846B265D42D4397141D()  < 21200:
                uri=None
            else:
                uri=("%s key='%s' srid=%d type=CurvePolygon%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 3: 
            sShape = "st_translate(shape, deltar, deltah)" if bDeltaTexte else "shape"
            table=("%s(select *," + sShape  + " as geom from %s %s)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=Point%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 31: 


            sShape = "st_makeline(shape, st_translate(shape, deltar, deltah))"
            table=("%s(select *," + sShape  + " as geom from %s %s WHERE isdelta = 'J' and (deltar * deltah) != 0)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
        if Art == 4: 
            uri = None
        if Art == 5: 
            table=("%s(select *,shape as geom from %s %s)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=LineString%s table=\"%s\" (geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)     
        if Art == 6: 
            table=("%s(select *,shape as geom from %s %s)%s") % (IndexGen1,geoTabName,sqlZusatz,IndexGen2)
            uri=("%s key='%s' srid=%d type=MultiPolygon%s table=\"%s\"(geom) sql=%s") % (ConnInfo, Key, Epsg, ken3D, table, where)
    return uri, LastGeoTabSpalte
    


















def EZUAFAF458DCD164EA4A76CF69189C827B7( db, LayerID, cgUser):

    sqlString=("select defid from prptable where layerid='%s' and usernr='%s'") %(LayerID, cgUser)
    rs = db.EZUDCF0989FCCB948B08C56317AE7037619(sqlString)
    rs.next() 
    Wert = rs.value(0)
    del(rs)
    return Wert

def EZUDCADB4666E944E57BEC334CD9635C33E (db,DefID):

    sqlString=("SELECT defname FROM  deftable WHERE defid ='%s'") % (DefID)
    rs = db.EZUDCF0989FCCB948B08C56317AE7037619(sqlString)
    rs.next() 
    Wert = rs.value(0)
    del(rs)
    return Wert

def EZUD50D8C51F08C4A5EA7A344E41666D439(db,LayerID, cgUser):  
    sqlString= EZUE46C97B18D5843DFB7668B8846F26976 ( 3,None, cgUser)
    sqlString = "select count(*) from (" + sqlString + ") as t1 inner join ("
    sqlString = sqlString + ("SELECT DISTINCT textssqlspatial.defid FROM textssqlspatial LEFT JOIN deftable ON textssqlspatial.defid =deftable.defid where layerid='%s' and textssqlspatial.defid != '{00000000-0000-0000-0000-000000000000}' union all select defid from prptable where layerid='%s' and usernr='%s'")%(LayerID,LayerID,cgUser)
    sqlString = sqlString + ") as t2 on t1.adid = t2.defid"

    rs = db.EZUDCF0989FCCB948B08C56317AE7037619(sqlString)
    rs.next() 
    Wert=rs.value(0) != 0
    del(rs)
    return Wert

def EZUCA7646F5CB604929B5B1138CDCC58756 (shpdat, bOnlyDarField, bNoGISDBIntern, LastGeoTabSpalte, likeShpDat = None, negativliste=None, positivliste=None):
    paramanz=0
    if likeShpDat: paramanz+=1
    if negativliste: paramanz+=1
    if positivliste: paramanz+=1
    if paramanz > 1: return -1
    delAnz=0
    
    source = ogr.Open(shpdat, update=True)
    if source is None:
        EZUC8DCB02F1A8145AF82C8A69A43E0529B(tr('ogr: can not open: ') + shpdat)
        return
    layer = source.GetLayer()
    laydef = layer.GetLayerDefn()
    

    



    schema = []
    for n in range(laydef.GetFieldCount()):

        schema.append(laydef.GetFieldDefn(n).name)
    

    if bNoGISDBIntern: 
        go = False
        for sp in schema:
            if sp == LastGeoTabSpalte:
                 go=True  

            if go :
                if sp in ["id", "objidgista", "pmfmark","pmfkey", "datestampn", "timestampn","datestampe", "timestampe"]:
                    layer.DeleteField(laydef.GetFieldIndex(sp))
                    delAnz+=1 
                

    if bOnlyDarField: 
        for sp in schema:
            if not sp in ["defid", "alpha", "pstext"]:
                layer.DeleteField(laydef.GetFieldIndex(sp))
                delAnz+=1 
            if sp == LastGeoTabSpalte:
                break
            
                
    if likeShpDat:
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
    dummy=1




