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
    from modDownload import *


except:
    from .fnc4all import *
    from .fnc4CaigosConnector import *
    from .clsDatenbank import *
    from .clsRenderingByQML import *
    from .modDownload import *




class clsQGISAction():  
    def EZU03023EF7FCAA442486B6AF6B66E6DC95 (self, shpDat):
        try:
            rest=shpDat 
            for rest in glob(shpDat[0:-4] + '.*'):
                os.remove(rest)
            return True
        except OSError as e:  
            EZUC8DCB02F1A8145AF82C8A69A43E0529B(u"Datei Löschfehler %s - %s." % (e.filename,e.strerror))

            return None
        
    def EZUFC52B0BB0EB14DA582CD889C9683B298(self):

        LayerList = QgsMapLayerRegistry.instance().mapLayers()
        for layer in LayerList:
            if myqtVersion == 4:
                QgsMapLayerRegistry.instance().removeMapLayer(layer)
            else:
                QgsProject.instance().removeMapLayer(layer)
 
    def EZU36EB5B0BF324447DB03DB38A6DBEC31E(self, NameOfGroup):

        toc = iface.legendInterface()
        LegList = toc.groups()
        if NameOfGroup in LegList:
            groupIndex = LegList.index(NameOfGroup)
            toc.removeGroup(groupIndex)
    
    def EZUC6B7AA70E6D148F4BA70BF8E44116329(self, NameOfGroup):
        toc = iface.legendInterface()
        LegList = toc.groups()
        if NameOfGroup in LegList:
            return LegList.index(NameOfGroup)


    def EZU2E78EDB4D1D440558B77FFCE3E2724AA (self,lName):
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
                    
    def EZU36BBFBA4F61246038D8E16E3CE6E2973(self):
        root = QgsProject.instance().layerTreeRoot()
        for child in root.children():
            if isinstance(child, QgsLayerTreeLayer):
                child.setCustomProperty("showFeatureCount", True)
    
    def EZU4EB57D86B4434DCEBA927278193D9F1D (self, prjNameInTree, qry):
        newparent = True
        Fachschale = None
        Thema = None
        Gruppe = None
        i=0
        

        rNode=QgsProject.instance().layerTreeRoot()   
        for node in rNode.children(): 
            if str(type(node))  == "<class 'qgis._core.QgsLayerTreeGroup'>":
                if node.name() == prjNameInTree:
                        rNode.removeChildNode(node)


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
                t = f.addGroup(EZU9A25B96EF34E432F8B39C40EA0D860A6(qry.value(1)))
                t.setExpanded(False)
                if myqtVersion == 4:
                    t.setVisible(False)
                else:
                    t.setItemVisibilityChecked(True)
            
            if newparent or qry.value(2) != Gruppe:
                newparent=True
                g = t.addGroup(EZU9A25B96EF34E432F8B39C40EA0D860A6(qry.value(2)))
                if myqtVersion == 4:
                    g.setVisible(False)
                else:
                    g.setItemVisibilityChecked(True)
            Fachschale=qry.value(0)
            Thema=qry.value(1)
            Gruppe=qry.value(2)
            newparent=False
        return ltgProjekt
        
    def EZU9569D8F0E36C44ACB766DB0A73364BC3(self, AktDB, User, prjNameInTree, qry4pri, qry, bGenDar, bPrjNeu, iDarGruppe, b3DDar, bDBTab, bSHPexp, bLeer, OutOfQGIS=False):
        def EZU1797DF3F28734C58A62078E9471FB2D6(prgBar, msgBar, Step, Titel, Text):

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
            s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
            bSaveDar = True if s.value( "bSaveDar", "Ja" )  == "Ja"   else False
            bOnlyDarField = True if s.value( "bOnlyDarField", "Ja" )  == "Ja"   else False
            bNoGISDBIntern = True if s.value( "bNoGISDBIntern", "Ja" )  == "Ja"   else False
            txtCodePage = s.value( "txtCodePage", 0)
            txtZielPfad = s.value( "txtSHPDir", "" )
            

        clsRendXML = clsRenderingByQML()
        ConnInfo=AktDB.EZUA098FD21021B43B78B52D0DC3130605D()
        param=str(User)+";"+EZUC936D29251B44D4E994497BF023338C7(prjNameInTree)+";"+str(bGenDar)+";"+str(bPrjNeu)+";"+str(iDarGruppe)+";"+str(b3DDar)+";"+str(bDBTab)+";"+str(bSHPexp)+";"+ str(bLeer)+";"+str(OutOfQGIS)
        param=param.replace("False","F").replace("True","T")
        Epsg=EZU07A28165B1CC4CC09B4AC9235EA3E8E9()
        cgVersion = EZU1C1D2B936A1D475D8F4C176B585F2301()

  

        ltgProjekt = self.EZU4EB57D86B4434DCEBA927278193D9F1D(prjNameInTree,qry) 
        iface.mapCanvas().setRenderFlag( False )   

        QApplication.setOverrideCursor(Qt.WaitCursor)
        step=0

        GesAnz = qry4pri.size()
        if bSHPexp: 
            GesAnz = GesAnz * 2 
        GesAnz = GesAnz + 1
        msgBar = iface.messageBar().createMessage("...")
        prgBar = QProgressBar()
        prgBar.setAlignment(Qt.AlignLeft)
        prgBar.setValue(0)
        dummy="http://www.makobo.de/links/Caigos_CheckImport.php?"
        prgBar.setMaximum(GesAnz)           
        msgBar.layout().addWidget(prgBar)
        iface.messageBar().pushWidget(msgBar, 0) 
        




        i=0    
        while (qry4pri.next()):

            qry4priEbene=qry4pri.value(0)
            qry4priLayerID=qry4pri.value(1)
            qry4priLayerTyp=qry4pri.value(2)
            qry4priDBname=qry4pri.value(3)

            try:
                i=i+1

            except:
                pass

            step = step + 1
            if not EZU1797DF3F28734C58A62078E9471FB2D6(prgBar, msgBar, step, "Laden", qry4priEbene):
                break
            
            GISDBTabName=None
            refObjID=None
            







            
            lName=EZU9A25B96EF34E432F8B39C40EA0D860A6(qry4priEbene) 
            if bDBTab and qry4priDBname:
                if EZU728F99262A784CE298F08321DF84E81D(qry4priDBname):
                    GISDBTabName=qry4priDBname.lower()
                    refObjID=EZUE2234C86576E4AFDBA184A9078854DDC(qry4priDBname)
                else:
                    EZUC8DCB02F1A8145AF82C8A69A43E0529B("Fehler Tabellenzugriff (Tabelle:" + qry4priDBname + ", Matchcode: like '%%\_objid', Ebene: " + lName )

            vlp, LastGeoTabSpalte = EZU494640CF7D9A43E19FD083B6B034293A (qry4priLayerTyp,ConnInfo,Epsg, qry4priLayerID,b3DDar, GISDBTabName, cgVersion, bSHPexp, refObjID)

            if vlp:

                


                Layer = QgsVectorLayer(vlp, lName , "postgres") 
                if Layer.isValid():
                    Layer.setReadOnly() 
                    if bLeer or Layer.featureCount() > 0:
                        if bSHPexp:




                            step = step + 1
                            
                            if not EZU1797DF3F28734C58A62078E9471FB2D6(prgBar, msgBar, step, "Speichern", qry4priEbene):
                                break
                            if  self.EZU03023EF7FCAA442486B6AF6B66E6DC95 (txtZielPfad + "/" + lName +".shp"):
                                pShp=EZUE7D17250C3C7421C9D8813540A672DFC(txtZielPfad + "/" + lName +".shp")
                                qmldat=EZUE7D17250C3C7421C9D8813540A672DFC(txtZielPfad + "/" + lName +".qml")
                                QgsVectorFileWriter.writeAsVectorFormat(Layer,pShp,txtCodePage,Layer.crs(),"ESRI Shapefile")
                                del(Layer) 

                                if bOnlyDarField or bNoGISDBIntern:

                                    if not EZU1797DF3F28734C58A62078E9471FB2D6(prgBar, msgBar, step, "DBF Anpassen", qry4priEbene):
                                        break
                                    EZUCA7646F5CB604929B5B1138CDCC58756 (pShp, bOnlyDarField, bNoGISDBIntern, LastGeoTabSpalte)
                                if not EZU1797DF3F28734C58A62078E9471FB2D6(prgBar, msgBar, step, "Anfügen", qry4priEbene):
                                    break

                                Layer = QgsVectorLayer(pShp,lName , "ogr") 

                                Layer.setProviderEncoding(txtCodePage)
                                Layer.dataProvider().setEncoding(txtCodePage) 
                            else:
                                EZUC8DCB02F1A8145AF82C8A69A43E0529B("'"+ txtZielPfad + "/" + lName + ".shp' wurde nicht erzeugt!")

                        if Layer.isValid():
                            if bGenDar: 


                                if EZUC86841CA58BC4846B265D42D4397141D() < 21200 and qry4priLayerTyp == 3:

                                    clsRendXML.EZUD5A9A7B19C594CD5AA23BB973E8B906D(AktDB, User, Layer, qry4priLayerTyp, qry4priLayerID, False, iDarGruppe)
                                else:                    

                                    clsRendXML.EZUD5A9A7B19C594CD5AA23BB973E8B906D(AktDB, User, Layer, qry4priLayerTyp, qry4priLayerID, True, iDarGruppe)


                                if bSHPexp:
                                    if bSaveDar:
                                        Layer.saveNamedStyle (qmldat)



                            AktFachschale, AktThema, AktGruppe, AktLayer = EZU7F7DA500B4FF409BB13A35E5F7EC2E59(qry4priLayerID, AktDB)

                            if myqtVersion == 4:
                                QgsMapLayerRegistry.instance().addMapLayer(Layer, False)
                            else:
                                QgsProject.instance().addMapLayer(Layer, False) 

                            g = ltgProjekt.findGroup(AktFachschale)
                            g = g.findGroup(AktThema)
                            g = g.findGroup(AktGruppe)
                            g.insertLayer(0, Layer)
                        else:
                            EZUC8DCB02F1A8145AF82C8A69A43E0529B("Fehler Layerkonvertierung nach Shape: " + pShp + '|' + lName + "|ogr" )

                else:
                    if not (lName[-4:] == "(RL)" and EZUC86841CA58BC4846B265D42D4397141D() < 21200):
                        EZUC8DCB02F1A8145AF82C8A69A43E0529B("Fehler Layereinbindung bei: " + lName + "\n" + vlp)
                    else:

                        debuglog (vlp + "|" + lName  + "|" + "postgres")
            else:
                EZUC8DCB02F1A8145AF82C8A69A43E0529B(u"Nicht unterstützt Typ " + str(qry4priLayerTyp) + ": " + lName)
        
        if bSHPexp:
            if bSaveDar:
                if myqtVersion == 5:
                    substPrjPath=txtZielPfad
                else:
                    substPrjPath=txtZielPfad.encode('utf8')
                



                tmpDat=tempfile.gettempdir() + "/{D5E6A1F8-392F-4241-A0BD-5CED09CFABC7}.qlr"
                qlrDat=EZUE7D17250C3C7421C9D8813540A672DFC(txtZielPfad + "/00-" + prjNameInTree + ".qlr")
                QgsLayerDefinition.exportLayerDefinition(tmpDat,[ltgProjekt])
                EZUAC460E6F0D4B49ABBAC60E8D53FD6A34(tmpDat, qlrDat, substPrjPath) 
                



                QgsProject.instance().setFileName(tmpDat)
                QgsProject.instance().write()
                qgsDat=EZUE7D17250C3C7421C9D8813540A672DFC(txtZielPfad + "/00-" + prjNameInTree + ".qgs")
                EZUAC460E6F0D4B49ABBAC60E8D53FD6A34(tmpDat, qgsDat, substPrjPath) 

        try:
            s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
            if (s.value( "status","") != "false"):
                check= dummy  + EZU11DE7CED39F2439E803B738E6E678716() + "|" + param
                EZUC8D59B20568948389B1274373D8E0990(check,EZUE2CC6C01835941909C82368EAB1CE1E2()+'test.zip')
        except:

            pass


        if not OutOfQGIS:
            iface.messageBar().clearWidgets()
            widget = iface.messageBar().createMessage("Baum wird aufgebaut")
            prgBar = QProgressBar()
            prgBar.setAlignment(Qt.AlignLeft)
            prgBar.setValue(1)
            prgBar.setMaximum(2)           
            widget.layout().addWidget(prgBar)
            iface.messageBar().pushWidget(widget, 0) 
            QCoreApplication.processEvents()
        

            iface.mapCanvas().refresh()
            iface.mapCanvas().zoomToSelected()
            iface.mapCanvas().zoomScale(2000)
            iface.mapCanvas().setRenderFlag( True )


            try:

                iface.layerTreeCanvasBridge().setHasCustomLayerOrder(True)
            except:
                try:

                    QgsProject.instance().layerTreeRoot().setHasCustomLayerOrder(True)
                except:

                    EZU9AC841489FAD40E4B1A1232B3CA9B315("\nBenutzerdefinierte Layserreihenfolge konnte nicht automatisch gesetzt werden!\nDiese muss in  dieser QGIS-Version manuell aktiviert werden.")
        
        iface.messageBar().clearWidgets()
        QApplication.restoreOverrideCursor()
        
        if EZUC86841CA58BC4846B265D42D4397141D() < 21200:
            EZU9AC841489FAD40E4B1A1232B3CA9B315("Bis QGIS 2.12 ist nur eine eingeschränkte Textdarstellung möglich!\nAußerdem können keine Kreise dargestellt werden!")
        
        if len(EZU03F45B01171E465F835613DBEE097689()) > 0:
            errbox("* " + "\n* ".join(EZU03F45B01171E465F835613DBEE097689())) 
        if len(EZU9D0157F9BB984DE991CEB81C700FA02B()) > 0:
            msgbox("* " + "\n* ".join(EZU9D0157F9BB984DE991CEB81C700FA02B())) 
       
if __name__ == "__main__":
    dummy=1

































