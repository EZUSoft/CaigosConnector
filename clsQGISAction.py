# -*- coding: utf-8 -*-
"""
/***************************************************************************
 clsQGISAction: Gemeinsame Basis für QGIS2 und QGIS3
  17.07.2018 V0.6
  - Anpassungen an QGIS 3.2
  09.11.2017 V0.5
  - Shapeexport optional speichern Layerdefinitions- und Projektdatei
  26.10.2017 V0.5
  - Shapeexport optional Darstellung (im Shapeverzeichnis) speichern
  08.07.2017 V0.4
  - Shape mit Darstellung speichern
  25.10.2016 V0.3
  - toUTF8(qry4priEbene): lName auf alle Zugriffe erweitert
  31.08.2016 V0.3
  - Integration Shape-Export
  - Hinweis für Kreise für QGis.QGIS_VERSION_INT < 21200
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
 *                                                                         
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 """
from osgeo import ogr 
from qgis.utils import *

try:
    from PyQt5 import QtGui, uic
    from PyQt5.QtCore import  Qt
    from PyQt5.QtWidgets import QDialog, QProgressBar
    from PyQt5.QtCore import QSettings
    from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlError

except:
    from PyQt4 import QtGui, uic
    from PyQt4.QtCore import  Qt
    from PyQt4.QtGui  import QDialog, QProgressBar
    from PyQt4.QtCore import QSettings
    from PyQt4.QtSql import QSqlDatabase, QSqlQuery, QSqlError  
 

try:
    from fnc4all import *
    from fnc4CaigosConnector import *
    from clsDatenbank import *
    from clsRenderingByQML import *


except:
    from .fnc4all import *
    from .fnc4CaigosConnector import *
    from .clsDatenbank import *
    from .clsRenderingByQML import *




class clsQGISAction():  
    def DelShapeDatBlock (self, shpDat):
        try:
            rest=shpDat # für Fehlermeldung
            for rest in glob(shpDat[0:-4] + '.*'):
                os.remove(rest)
            return True
        except OSError as e:  ## if failed, report it back to the user ##
            addFehler(u"Datei Löschfehler %s - %s." % (e.filename,e.strerror))
            #QMessageBox.critical(None, u"Datei Löschfehler","Error: %s - %s." % (e.filename,e.strerror)) 
            return None
        
    def AlleLayerLoeschen(self):
        # Löscht (im Moment) nur die Layer - nicht die Gruppen 
        LayerList = QgsMapLayerRegistry.instance().mapLayers()
        for layer in LayerList:
            if myqtVersion == 4:
                QgsMapLayerRegistry.instance().removeMapLayer(layer)
            else:
                QgsProject.instance().removeMapLayer(layer)
 
    def GruppeLoeschenByName(self, NameOfGroup):
        # Löscht  die Gruppen 
        toc = iface.legendInterface()
        LegList = toc.groups()
        if NameOfGroup in LegList:
            groupIndex = LegList.index(NameOfGroup)
            toc.removeGroup(groupIndex)
    
    def getGroupIDByName(self, NameOfGroup):
        toc = iface.legendInterface()
        LegList = toc.groups()
        if NameOfGroup in LegList:
            return LegList.index(NameOfGroup)


    def LayerbyName (self,lName):
        if myqtVersion == 4:
            for lyr in QgsMapLayerRegistry.instance().mapLayers().values():
                if lyr.name() == lName:
                    return lyr
                    break        
        else:
            for lyr in QgsProject.instance().mapLayers().values():
                if lyr.name() == lName:
                    return lyr
                    break       
                    
    def ObjektAnzahlZeigen(self):
        root = QgsProject.instance().layerTreeRoot()
        for child in root.children():
            if isinstance(child, QgsLayerTreeLayer):
                child.setCustomProperty("showFeatureCount", True)
    
    def ErzeugeStruktur (self, prjNameInTree, qry):
        newparent = True
        Fachschale = ""
        Thema = ""
        Gruppe = ""
        i=0
        
        # 1.) evetuell vorhandenes Projekt/Projektname (-gruppe) in Root löschen
        rNode=QgsProject.instance().layerTreeRoot()   
        for node in rNode.children(): # oberste Ebene in Schleife durchlaufen
            if str(type(node))  == "<class 'qgis._core.QgsLayerTreeGroup'>":
                if node.name() == prjNameInTree:
                        rNode.removeChildNode(node)

        # 2.) LayerTreeGroup in Wurzel Projektbaum erstellen
        ltgProjekt = rNode.addGroup(prjNameInTree)
        ltgProjekt.setExpanded(True) 
        if myqtVersion == 4:
            ltgProjekt.setVisible(False)
        else:
            ltgProjekt.setItemVisibilityChecked(True)    

        while (qry.next()):
            i=i+1
            if qry.value(0) != Fachschale:
                newparent=True
                f = ltgProjekt.addGroup(qry.value(0))
                f.setExpanded(True)
                if myqtVersion == 4:
                    f.setVisible(False)
                else:
                    f.setItemVisibilityChecked(True)


            if newparent or qry.value(1) != Thema:
                newparent=True
                t = f.addGroup(toUTF8(qry.value(1)))
                t.setExpanded(False)
                if myqtVersion == 4:
                    t.setVisible(False)
                else:
                    t.setItemVisibilityChecked(True)
            
            if newparent or qry.value(2) != Gruppe:
                newparent=True
                g = t.addGroup(toUTF8(qry.value(2)))
                if myqtVersion == 4:
                    g.setVisible(False)
                else:
                    g.setItemVisibilityChecked(True)
            Fachschale=qry.value(0)
            Thema=qry.value(1)
            Gruppe=qry.value(2)
            newparent=False
        return ltgProjekt
        
    def QGISBaum(self, AktDB, User, prjNameInTree, qry4pri, qry, bGenDar, bPrjNeu, iDarGruppe, b3DDar, bDBTab, bSHPexp, bLeer, OutOfQGIS=False):
        def Fortschritt(prgBar, msgBar, Step, Titel, Text):
            # Fortschritt(prgBar, msgBar, Step,  Text)
            try:
                prgBar.setValue(Step)
                msgBar.setTitle(Titel)
                msgBar.setText(Text)
                QCoreApplication.processEvents()
                return True
            except:
                QMessageBox.critical( None, "Abbruch","Vorgang dort durch Nutzereingriff beendet")
                return False
        idxLayer = -1
        if bSHPexp:
            s = QSettings( "EZUSoft", fncProgKennung() )
            bSaveDar = True if s.value( "bSaveDar", "Ja" )  == "Ja"   else False
            bOnlyDarField = True if s.value( "bOnlyDarField", "Ja" )  == "Ja"   else False
            bNoGISDBIntern = True if s.value( "bNoGISDBIntern", "Ja" )  == "Ja"   else False
            txtCodePage = s.value( "txtCodePage", 0)
            txtZielPfad = s.value( "txtSHPDir", "" )
            
        # allgemeine Daten für Layereinbindung ermitteln
        clsRendXML = clsRenderingByQML()
        ConnInfo=AktDB.GetConnString()
        Epsg=GetEPSG()
        cgVersion = GetCGVersion()

  
        # Teil 1 =======================  Ebenen laden und attributieren  =============================
        ltgProjekt = self.ErzeugeStruktur(prjNameInTree,qry) # Projektbaum generieren           
        iface.mapCanvas().setRenderFlag( False )   # Kartenaktualisierung abschalten                 

        QApplication.setOverrideCursor(Qt.WaitCursor)
        step=0
        # Progressbar intitialisieren
        GesAnz = qry4pri.size()
        if bSHPexp: 
            GesAnz = GesAnz * 2 # zwischenschritt für Progressbar
        GesAnz = GesAnz + 1
        msgBar = iface.messageBar().createMessage("...")
        prgBar = QProgressBar()
        prgBar.setAlignment(Qt.AlignLeft)
        prgBar.setValue(0)
        prgBar.setMaximum(GesAnz)           
        msgBar.layout().addWidget(prgBar)
        iface.messageBar().pushWidget(msgBar, 0) # 15.02.18 Fehler bei QGIS 2018/02 iface.messageBar().INFO --> 0
        
        # 3.) Ebenen laden
        #   0      1        2     
        # layername, lyrtable.layerid, lyrtable.layertyp, dbname, priority

        i=0    
        while (qry4pri.next()):
            # 17.07.18: im weiteren Verlauf crasht der Zugriff auf qry4pri.value(x), deshalb werden die Werte in eine Liste geschrieben
            qry4priEbene=qry4pri.value(0)
            qry4priLayerID=qry4pri.value(1)
            qry4priLayerTyp=qry4pri.value(2)
            qry4priDBname=qry4pri.value(3)
            try:
                i=i+1
                #print (i, step, GesAnz, qry4priEbene)
            except:
                pass
            #Progressbar weiterschalten
            step = step + 1
            if not Fortschritt(prgBar, msgBar, step, "Laden", qry4priEbene):
                break
            
            GISDBTabName=None
            
            """
            -> hat irgendwie nix gebracht, war langsam und vor allem hat sich der Speicher irgendwie aufgeschauckelt
            if bLeer:
                LayerMachWas = True
            else:
                LayerMachWas =  not (clsdb.sqlLayerIsEmpty(q    ry4pri.value(2),qry4priLayerID))
            """
            
            if bDBTab and qry4priDBname:#
                if dbExistsGISDBTab(qry4priDBname):
                    GISDBTabName=qry4priDBname.lower()
                else:
                    addFehler("Fehler Tabellenzugriff (" + qry4priDBname + ") bei: " + lName )

            vlp = VectorLayerPath (qry4priLayerTyp,ConnInfo,Epsg, qry4priLayerID,b3DDar, GISDBTabName, cgVersion, bSHPexp)
            # 17.07.18: ab hier crasht der Zugriff auf qry4pri.value, deshalb werden die Werte in ein normales array geschrieben
            if vlp:
                # ================== 1. Schritt Layer einbinden =============================
                lName=toUTF8(qry4priEbene)
                #print (vlp)
                #print (lName)
                Layer = QgsVectorLayer(vlp, lName , "postgres") 
                if Layer.isValid():
                    Layer.setReadOnly() # sicherheitshalbe ReadOnly auf PG-Layer
                    if bLeer or Layer.featureCount() > 0:
                        if bSHPexp:
                            # Bei Shape-Option: Layer als Shape speichern, Postgres lösen und Shape setzen
                            # 30.07.18:
                            #   - Dateien vorher löschen, sonst gibt es Nebeneffekte: z.B: Export ohne Darstellung und schom vorhandene qml
                                        #Progressbar weiterschalten
                            step = step + 1
                            
                            if not Fortschritt(prgBar, msgBar, step, "Speichern", qry4priEbene):
                                break
                            if  self.DelShapeDatBlock (txtZielPfad + "/" + lName +".shp"):
                                pShp=fncMakeDatName(txtZielPfad + "/" + lName +".shp")
                                qmldat=fncMakeDatName(txtZielPfad + "/" + lName +".qml")
                                QgsVectorFileWriter.writeAsVectorFormat(Layer,pShp,txtCodePage,Layer.crs(),"ESRI Shapefile")
                                del(Layer) # Referenz sicherhaltshalber löschen

                                if bOnlyDarField or bNoGISDBIntern:
                                    # def DBFAnpassen (self,shpdat, bOnlyDarField, bNoGISDBIntern, likeShpDat = None, negativliste=None, positivliste=None)
                                    if not Fortschritt(prgBar, msgBar, step, "DBF Anpassen", qry4priEbene):
                                        break
                                    DBFAnpassen (pShp, bOnlyDarField, bNoGISDBIntern)
                                if not Fortschritt(prgBar, msgBar, step, "Anfügen", qry4priEbene):
                                    break

                                Layer = QgsVectorLayer(pShp,lName , "ogr") 
                                # 13.07.17: jetzt für den importieren Layer den Zeichensatz setzen
                                Layer.setProviderEncoding(txtCodePage)
                                Layer.dataProvider().setEncoding(txtCodePage) 
                            else:
                                addFehler("'"+ txtZielPfad + "/" + lName + ".shp' wurde nicht erzeugt!")

                        if Layer.isValid():
                            if bGenDar: 
                                # ================== 2. Schritt Darstellung definieren  ================== 
                                #          Render(self, cgUser, qLayer, cgEbenenTyp, LayerID, bRolle, Group=0): 
                                if myQGIS_VERSION_INT() < 21200 and qry4priLayerTyp == 3:
                                    # Texte in Wien und Pisa:  ohne Rolle schreiben (nur erster Maßstab) Maßstab
                                    clsRendXML.Render(AktDB, User, Layer, qry4priLayerTyp, qry4priLayerID, False, iDarGruppe)
                                else:                    
                                    # Neue Version über QML
                                    clsRendXML.Render(AktDB, User, Layer, qry4priLayerTyp, qry4priLayerID, True, iDarGruppe)


                                if bSHPexp:
                                    if bSaveDar:
                                        Layer.saveNamedStyle (qmldat)


                            # Layer zunächst in Projektroot einladen
                            AktFachschale, AktThema, AktGruppe, AktLayer = dbLayerStrukturByID(qry4priLayerID, AktDB)
                            # QGIS 2:
                            if myqtVersion == 4:
                                QgsMapLayerRegistry.instance().addMapLayer(Layer, False)
                            else:
                                QgsProject.instance().addMapLayer(Layer, False) 

                            g = ltgProjekt.findGroup(AktFachschale)
                            g = g.findGroup(AktThema)
                            g = g.findGroup(AktGruppe)
                            g.insertLayer(0, Layer)
                        else:
                            addFehler("Fehler Layerkonvertierung nach Shape: " + pShp + '|' + lName + "|ogr" )

                else:
                    if not (lName[-4:] == "(RL)" and myQGIS_VERSION_INT() < 21200):
                        addFehler("Fehler Layereinbindung bei: " + lName + "\n" + vlp)
                    else:
                        # Bei QGIS-Wien und leerem Layer (keine Referenzllinie) kommt es zum Fehler - welcher eigentlich ja keiner ist
                        debuglog (vlp + "|" + lName  + "|" + "postgres")
            else:
                addFehler(u"Nicht unterstützt Typ " + str(qry4priLayerTyp) + ": " + lName)
        
        if bSHPexp:
            if bSaveDar:
                if myqtVersion == 5:
                    substPrjPath=txtZielPfad
                else:
                    substPrjPath=txtZielPfad.encode('utf8')
                
                #substPrjPath=txtZielPfad.encode('utf8').decode('utf8'))
                # die Layerdefinitionsdatei speichern
                # -> Nachteil es wird keine Layerreihenfolge gespeichert
                tmpDat=tempfile.gettempdir() + "/{D5E6A1F8-392F-4241-A0BD-5CED09CFABC7}.qlr"
                qlrDat=fncMakeDatName(txtZielPfad + "/00-" + prjNameInTree + ".qlr")
                QgsLayerDefinition.exportLayerDefinition(tmpDat,[ltgProjekt])
                qXDatAbsolute2Relativ(tmpDat, qlrDat, substPrjPath) # txtZielPfad)
                
                # eine Projektdatei schreiben
                # -> macht prizipiell wenig Sinn, weil das gesamte Projekt und nicht nur die importieren Layer gespeichert werden
                #    allerding gibt es hier nicht die Nachteile der *.qlr
                QgsProject.instance().setFileName(tmpDat)
                QgsProject.instance().write()
                qgsDat=fncMakeDatName(txtZielPfad + "/00-" + prjNameInTree + ".qgs")
                qXDatAbsolute2Relativ(tmpDat, qgsDat, substPrjPath) # txtZielPfad)


        # Anzeige wieder aktivieren, Progressbar rucksetzen
        if not OutOfQGIS:
            iface.messageBar().clearWidgets()
            widget = iface.messageBar().createMessage("Baum wird aufgebaut")
            prgBar = QProgressBar()
            prgBar.setAlignment(Qt.AlignLeft)
            prgBar.setValue(1)
            prgBar.setMaximum(2)           
            widget.layout().addWidget(prgBar)
            iface.messageBar().pushWidget(widget, 0) # 15.02.18 Fehler bei QGIS 2018/02 iface.messageBar().INFO --> 0
            QCoreApplication.processEvents()
        

            iface.mapCanvas().refresh()
            iface.mapCanvas().zoomToSelected()
            iface.mapCanvas().zoomScale(2000)
            iface.mapCanvas().setRenderFlag( True )

            # Reihenfolge laut LayerListe ab QGIS 2.12 
            try:
                # 2.12 - 2.99 Februar 2017
                iface.layerTreeCanvasBridge().setHasCustomLayerOrder(True)
            except:
                try:
                    # 2.99 Juli 2017
                    QgsProject.instance().layerTreeRoot().setHasCustomLayerOrder(True)
                except:
                    # in Wien und (Pisa) funktioniert das nicht
                    addHinweis("\nBenutzerdefinierte Layserreihenfolge konnte nicht automatisch gesetzt werden!\nDiese muss in  dieser QGIS-Version manuell aktiviert werden.")
        
        iface.messageBar().clearWidgets()
        QApplication.restoreOverrideCursor()
        
        if myQGIS_VERSION_INT() < 21200:
            addHinweis("Bis QGIS 2.12 ist nur eine eingeschränkte Textdarstellung möglich!\nAußerdem können keine Kreise dargestellt werden!")
        
        if len(getFehler()) > 0:
            errbox("* " + "\n* ".join(getFehler())) # 25.10.18 "\n\n" --> "\n* "
        if len(getHinweis()) > 0:
            msgbox("* " + "\n* ".join(getHinweis())) # 25.10.18 "\n\n" --> "\n* " 
       
if __name__ == "__main__":
    ('txtZielPfad').encode('utf8')
    # zur zum lokalen testen 
    #app = QApplication(sys.argv)
    #QgsApplication.initQgis()
    """
    clsdb1 = pgDataBase()
    if clsdb1.CheckDBTabSpalte("D4USTDOK_QS"):
        GISDBTabName="D4USTDOK_QS".lower()
        print ("Wahr")
    else:
        print ("Falsch")
    """

    """
    OutOfQGIS=True
    c=clsQGISAction()
    clsdb=pgDataBase()
    db=clsdb.OpenDatabase(clsdb.GetConnString())
 
    if  db :
        print (clsdb.sqlStrukAlleLayer("'{B22183E0-3AEC-44ED-B0A8-60B2F02C6649}'"))
        print (db.OpenRecordset(sqlStrukAlleLayer("'{B22183E0-3AEC-44ED-B0A8-60B2F02C6649}'")) )
        qry = db.OpenRecordset(sqlStrukAlleLayer("'{B22183E0-3AEC-44ED-B0A8-60B2F02C6649}'")) 
        while (qry.next()):
            s=qry.value(0)
            printlog(s)
        
        #def QGISBaum(self, db, User, prjNameInTree, qry4pri, qry, bGenDar, bPrjNeu, OutOfQGIS=False)
        #c.QGISBaum(db,'000', clsdb.GetDBname(),qry,qry,True,True,True)
        

    else:
        QMessageBox.critical( None, "Fehler beim Datenbankzu")
    """