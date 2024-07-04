# -*- coding: utf-8 -*-
"""
/***************************************************************************
 A QGIS plugin
CaigosConnector: Connect CAIGOS-GIS with QGIS
        copyright            : (C) 2020 by EZUSoft
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


















from qgis.utils import os, sys
try:
    from PyQt5.QtCore import QSettings
    from PyQt5 import QtGui, uic
    from PyQt5.QtCore import  QDir, Qt
    from PyQt5.QtWidgets import * 
except:
    from PyQt4.QtCore import QSettings
    from PyQt4 import QtGui, uic
    from PyQt4.QtCore import  QDir, Qt
    from PyQt4.QtGui  import * 

try:
    from fnc4all import *
    from fnc4CaigosConnector import *
    from modDownload import *

except:
    from .fnc4all import *   
    from .fnc4CaigosConnector import *
    from .modDownload import *





FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'uiExplorer.ui'))


class uiExplorer(QDialog, FORM_CLASS):
    charsetList = ["System",
     "ascii",
     "big5",
     "big5hkscs",
     "cp037",
     "cp424",
     "cp437",
     "cp500",
     "cp720",
     "cp737",
     "cp775",
     "cp850",
     "cp852",
     "cp855",
     "cp856",
     "cp857",
     "cp858",
     "cp860",
     "cp861",
     "cp862",
     "cp863",
     "cp864",
     "cp865",
     "cp866",
     "cp869",
     "cp874",
     "cp875",
     "cp932",
     "cp949",
     "cp950",
     "cp1006",
     "cp1026",
     "cp1140",
     "cp1250",
     "cp1251",
     "cp1252",
     "cp1253",
     "cp1254",
     "cp1255",
     "cp1256",
     "cp1257",
     "cp1258",
     "euc_jp",
     "euc_jis_2004",
     "euc_jisx0213",
     "euc_kr",
     "gb2312",
     "gbk",
     "gb18030",
     "hz",
     "iso2022_jp",
     "iso2022_jp_1",
     "iso2022_jp_2",
     "iso2022_jp_2004",
     "iso2022_jp_3",
     "iso2022_jp_ext",
     "iso2022_kr",
     "latin_1",
     "iso8859_2",
     "iso8859_3",
     "iso8859_4",
     "iso8859_5",
     "iso8859_6",
     "iso8859_7",
     "iso8859_8",
     "iso8859_9",
     "iso8859_10",
     "iso8859_13",
     "iso8859_14",
     "iso8859_15",
     "iso8859_16",
     "johab",
     "koi8_r",
     "koi8_u",
     "mac_cyrillic",
     "mac_greek",
     "mac_iceland",
     "mac_latin2",
     "mac_roman",
     "mac_turkish",
     "ptcp154",
     "shift_jis",
     "shift_jis_2004",
     "shift_jisx0213",
     "System",
     "utf_32",
     "utf_32_be",
     "utf_32_le",
     "utf_16",
     "utf_16_be",
     "utf_16_le",
     "utf_7",
     "utf_8",
     "utf_8_sig"]
    def __init__(self,  parent=None):

        super(uiExplorer, self).__init__(parent)





        self.setupUi(self)
        btn = self.button_box.button(QDialogButtonBox.Apply)
        btn.clicked.connect(self.EZU866EA2C310114D5CA9F718FEC89F651F)
        self.browseZielPfad.clicked.connect(self.EZU09753DE7B19B413CA8594D73CE7D6074)
        self.cmdReset.clicked.connect(self.EZU5B07B73B000A446CBEFCD87EF2D82514)         
        self.chkSHPexp.clicked.connect(self.EZU0344358B5EF84BE88B8E3C73A2476FBE) 
        self.chkGPKGexp.clicked.connect(self.EZU99FF3B1EAB4C4CF3B1AA4F1AEC72EFA2)        
        self.chkGISDB.clicked.connect(self.EZU663B59541A9B4AC1B23819C4A6E3E89B)      
        self.chkFiltObjKl.clicked.connect(self.EZU663B59541A9B4AC1B23819C4A6E3E89B)
        self.bWarnKeyTab = True 
        self.chkKeyTab.clicked.connect(self.EZUDBF5E1186DAB4EEEA506DA9F852510DF)
        self.cbKeyTab.currentIndexChanged.connect(self.EZUDBF5E1186DAB4EEEA506DA9F852510DF)
        

        
        chkurl="https://www.makobo.de/links/Caigos_CheckVersion.php?"
        
        EZU1C9648848F904099A178AD545D77A882()
        self.setWindowTitle (EZUAC62A428AD734562A807B0FF8D792A61())  

        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        bGenDar = True  if s.value( "bGenDar", "Ja" )   == "Ja"   else False
        bPrjNeu = True  if s.value( "bPrjNeu", "Ja" )   == "Ja"   else False
        bLeer = False   if s.value( "bLeer", "Nein" )   == "Nein" else True
        bDBTab = False  if s.value( "bDBTab", "Nein" )  == "Nein" else True
        bFiltObjKl = False  if s.value( "bFiltObjKl", "Nein" )  == "Nein" else True
        bKeyTab = False  if s.value( "bKeyTab", "Nein" )  == "Nein" else True
        bDarObjKl = False   if s.value( "bDarObjKl", "Nein" )   == "Nein" else True
        b3DDar = False  if s.value( "b3DDar", "Nein" )  == "Nein" else True
        bSHPexp = False if s.value( "bSHPexp", "Nein" ) == "Nein" else True
        bGPKGexp = False if s.value( "bGPKGexp", "Nein" ) == "Nein" else True
        bSaveDar = True if s.value( "bSaveDar", "Ja" )  == "Ja"   else False
        bOnlyDarField = True if s.value( "bOnlyDarField", "Ja" )  == "Ja"   else False
        bNoGISDBIntern = True if s.value( "bNoGISDBIntern", "Ja" )  == "Ja"   else False
        chkurl="https://www.makobo.de/links/Caigos_CheckVersion.php?"   
        iCodePage=s.value( "iCodePage", 0)
        iObjKlasse=s.value( "iObjKlasse", 0)

        self.txtZielPfad.setText(s.value( "txtSHPDir", "" ))
        
        self.cbCharSet.addItems(self.charsetList)
        self.cbCharSet.setCurrentIndex(int(iCodePage))

        self.cbKeyTab.addItem('Nur Key01') 
        self.cbKeyTab.addItem('alle definierten')        
 
        iGruppe=s.value( "iDarGruppe", 0 )

        self.chkDar.setChecked(bGenDar)
        
        iServer=EZU50464908A0F8417AA7B9045C4E9B1F6A() 
        if (iServer != 0 and bDBTab):
            bDBTab= False 
        if (iServer != 0 and bLeer == False):
            bLeer = True  
        self.chkGISDB.setEnabled(iServer == 0)
        self.chkLeer.setEnabled(iServer == 0)
        
        self.chkGISDB.setChecked(bDBTab)
        self.chkFiltObjKl.setChecked(bFiltObjKl)
        self.chkKeyTab.setChecked(bKeyTab)
        self.chkDarObjKl.setChecked(bDarObjKl)
        self.chkLeer.setChecked(bLeer)
        self.chk3DDar.setChecked(b3DDar)
        self.chkDarObjKl.setChecked(bDarObjKl)
        
        self.chkSHPexp.setChecked(bSHPexp)
        self.chkGPKGexp.setChecked(bGPKGexp)
        self.chkSaveDar.setChecked(bSaveDar)
        self.chkOnlyDarField.setChecked(bOnlyDarField)
        self.chkNoGISDBIntern.setChecked(bNoGISDBIntern)
        
        self.EZU663B59541A9B4AC1B23819C4A6E3E89B()
        
        if bPrjNeu:
            self.rBNeu.setChecked(True)
        else:
            self.rBHinz.setChecked(True)

        

        self.rBNeu.setChecked(True)
        self.grpBoxProjDat.setEnabled (False)
        self.grpBoxProjDat.hide()

        for g in range(5): 
            self.cbGruppe.addItem("Gruppe-" + str(g))
        self.cbGruppe.setCurrentIndex(iGruppe)  
    
        
    def EZU0344358B5EF84BE88B8E3C73A2476FBE(self):
        if self.chkSHPexp.isChecked(): self.chkGPKGexp.setChecked(False) 
        self.EZU663B59541A9B4AC1B23819C4A6E3E89B()
    
    def EZU99FF3B1EAB4C4CF3B1AA4F1AEC72EFA2(self):
        if self.chkGPKGexp.isChecked(): self.chkSHPexp.setChecked(False) 
        self.EZU663B59541A9B4AC1B23819C4A6E3E89B()

    
    def EZUDBF5E1186DAB4EEEA506DA9F852510DF(self):
        if self.chkKeyTab.isChecked() and self.cbKeyTab.currentIndex() == 1:
            if self.bWarnKeyTab:
                self.bWarnKeyTab = False
                msgbox ("Alle Keyfelder einzubinden ist ein sehr rechenintensiver Prozess.\nDies sollte nur bei einigen wenigen Ebenen genutzt werden")
        self.EZU663B59541A9B4AC1B23819C4A6E3E89B()
        
    def EZU663B59541A9B4AC1B23819C4A6E3E89B(self):
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        bGenExport = self.chkSHPexp.isChecked() or self.chkGPKGexp.isChecked()

        bDBTab  = self.chkGISDB.isChecked()
        bFiltObjKl= self.chkFiltObjKl.isChecked()
        bKeyTab= self.chkKeyTab.isChecked()

        self.browseZielPfad.setEnabled(bGenExport) 
        self.cbCharSet.setEnabled(bGenExport) 
        self.lbCharSet.setEnabled(bGenExport) 
        self.chkSaveDar.setEnabled(bGenExport) 
        self.chkOnlyDarField.setEnabled(bGenExport) 
        self.chkNoGISDBIntern.setEnabled(bDBTab and bGenExport) 
        self.cbObjKlasse.setEnabled(bFiltObjKl)
        self.cbKeyTab.setEnabled(bKeyTab)
        if bGenExport:
            self.txtZielPfad.setPlaceholderText(self.tr("Specify destination path")) 
        else:
            self.txtZielPfad.setPlaceholderText("") 
            
        if (s.value( "status","")==''):
            self.chkDar.setEnabled(False)
            self.chkDar.setChecked(False)          
        else:
            self.chkDar.setEnabled(s.value( "status","")==b'ok' or s.value( "status","")==b'man')
            if (s.value( "status","")!=b'ok' and s.value( "status","")!=b'man'):
                self.chkDar.setChecked(False)    
    
    def EZU5B07B73B000A446CBEFCD87EF2D82514(self):
        self.chkDar.setChecked(True)
        self.chkGISDB.setChecked(False)
        self.chkFiltObjKl.setChecked(False)
        self.chkKeyTab.setChecked(False)
        self.chkDarObjKl.setChecked(False)
        
        iServer=EZU50464908A0F8417AA7B9045C4E9B1F6A() 
        if (iServer == 0):
            self.chkLeer.setChecked(False)
        if (iServer == 1): 
            self.chkLeer.setChecked(True)
        
        self.chk3DDar.setChecked(False)
        self.chkSHPexp.setChecked(False)
        self.chkGPKGexp.setChecked(False)
        self.chkSaveDar.setChecked(False)
        self.chkOnlyDarField.setChecked(False)
        self.chkNoGISDBIntern.setChecked(False)
        QSettings("EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA()).setValue("status",'')
        EZU1C9648848F904099A178AD545D77A882()
        self.setWindowTitle (EZUAC62A428AD734562A807B0FF8D792A61()) 
        self.bWarnKeyTab=True 
        self.EZU663B59541A9B4AC1B23819C4A6E3E89B()
 
    
    def EZU09753DE7B19B413CA8594D73CE7D6074(self):
        if self.txtZielPfad.text() == "":
            s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
            lastSHPDir = s.value("txtSHPDir", ".")
        else:
            lastSHPDir = self.txtZielPfad.text()
        
        if not os.path.exists(lastSHPDir):
            lastSHPDir=os.getcwd()    
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        shpDirName = QFileDialog.getExistingDirectory(self, u"Verzeichnis für Export-Dateien wählen",lastSHPDir,flags)
        if shpDirName != "":
            if len( os.listdir( shpDirName ) ) > 0:
                reply = QMessageBox.question(None, u'Verzeichnis ist nicht leer',u"Namensgleiche Export-Dateien werden überschrieben", QMessageBox.Yes |  QMessageBox.Cancel, QMessageBox.Cancel)
                if reply ==  QMessageBox.Yes:
                    self.txtZielPfad.setText(shpDirName)
            else:
                self.txtZielPfad.setText(shpDirName)
                





    
    def EZU60469930E88C47F5AC4734E80EDBEBB6(self):        
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        s.setValue( "bGenDar", "Ja" if self.chkDar.isChecked() == True else "Nein")
        s.setValue( "bPrjNeu", "Ja" if self.rBNeu.isChecked() == True else "Nein")
        s.setValue( "iDarGruppe", self.cbGruppe.currentIndex())
        s.setValue( "bDBTab", "Ja" if self.chkGISDB.isChecked() == True else "Nein")
        s.setValue( "bFiltObjKl", "Ja" if self.chkFiltObjKl.isChecked() == True else "Nein")
        s.setValue( "bKeyTab", "Ja" if self.chkKeyTab.isChecked() == True else "Nein")
        s.setValue( "bDarObjKl", "Ja" if self.chkDarObjKl.isChecked() == True else "Nein")
        s.setValue( "bLeer", "Ja" if self.chkLeer.isChecked() == True else "Nein")
        s.setValue( "b3DDar", "Ja" if self.chk3DDar.isChecked() == True else "Nein")
        s.setValue( "bSHPexp", "Ja" if self.chkSHPexp.isChecked() == True else "Nein")
        s.setValue( "bGPKGexp", "Ja" if self.chkGPKGexp.isChecked() == True else "Nein")
        s.setValue( "bSaveDar", "Ja" if self.chkSaveDar.isChecked() == True else "Nein")
        s.setValue( "bOnlyDarField", "Ja" if self.chkOnlyDarField.isChecked() == True else "Nein")
        s.setValue( "bNoGISDBIntern", "Ja" if self.chkNoGISDBIntern.isChecked() == True else "Nein")
       
        s.setValue( "iCodePage", self.cbCharSet.currentIndex())
        s.setValue( "iObjKlasse", self.cbObjKlasse.currentIndex())
        s.setValue( "iKeyTab", self.cbKeyTab.currentIndex())
        s.setValue( "txtCodePage", self.cbCharSet.currentText())
        s.setValue( "txtSHPDir", self.txtZielPfad.text())

    def EZUB1A3A5F021794B749EB473C9B033A214(self, rootname, qry):
        tw = self.twCaigosLayer
        tw.clear()

        newparent = True

        Fachschale = None
        Thema = None
        Gruppe = None
        p_item = QTreeWidgetItem(tw)
        p_item.setText(0, rootname)
        p_item.setCheckState(0,Qt.Unchecked)
        p_item.setExpanded(True)
        p_item.setFlags(p_item.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        while (qry.next()):

            if qry.value(0) != Fachschale:
                newparent=True
                f_item = QTreeWidgetItem(p_item)
                f_item.setText(0, qry.value(0))

                f_item.setCheckState(0,Qt.Unchecked)
                f_item.setFlags(f_item.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)

            if newparent or qry.value(1) != Thema:
                newparent=True
                t_item = QTreeWidgetItem(f_item)
                t_item.setText(0, qry.value(1))
                t_item.setCheckState(0,Qt.Unchecked)
                t_item.setFlags(t_item.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
               
            if newparent or qry.value(2) != Gruppe:
                newparent=True
                g_item = QTreeWidgetItem(t_item)
                g_item.setText(0, qry.value(2))
                g_item.setCheckState(0,Qt.Unchecked)
                g_item.setFlags(g_item.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)  

            e_item = QTreeWidgetItem(g_item)
            e_item.setText(0, qry.value(3))
            e_item.setData(1,0,qry.value(4)) 
            e_item.setCheckState(0,Qt.Unchecked)
            e_item.setFlags(e_item.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)

            Fachschale=qry.value(0)
            Thema=qry.value(1)
            Gruppe=qry.value(2)
            newparent=False
    
    def EZU866EA2C310114D5CA9F718FEC89F651F(self):


        view = self.twCaigosLayer
        Liste=[]
        it = QTreeWidgetItemIterator(view,QTreeWidgetItemIterator.Checked)
        while it.value():
            item = it.value()
            if item.text(1):
                Liste.append (item.text(1))    
            it += 1
        if len(Liste) == 0:
            msgbox("Es wurden keine Ebenen zur Darstellung  ausgewählt") 
            return



        if self.chkSHPexp.isChecked() or self.chkGPKGexp.isChecked():
            ZielPfad=self.txtZielPfad.text()                
            if ZielPfad == "":
                QMessageBox.critical(None, u"SHP-Zielpfad nicht gesetzt", u"Bitte Export-Zielpfad wählen") 
                return
            if ZielPfad[:-1] != "/" and ZielPfad[:-1] != "\\":
                    ZielPfad=ZielPfad + "/"
            if not os.path.exists(ZielPfad):
                QMessageBox.critical(None, u"Export Zielpfad nicht gefunden", ZielPfad)
                return


        super(uiExplorer, self).accept() 
            

    def EZU06A3014A0EC345C9B52BC3ED5D2B05AA(self):
        view = self.twCaigosLayer
        Liste=[]
        it = QTreeWidgetItemIterator(view,QTreeWidgetItemIterator.Checked)
        while it.value():
            item = it.value()
            if item.text(1):
                Liste.append (item.text(1))    
            it += 1

        self.EZU60469930E88C47F5AC4734E80EDBEBB6()
        fObjKl=-1
        if self.chkFiltObjKl.isChecked():
            fObjKl = self.cbObjKlasse.currentIndex()
        
        fKeyTab=-1
        if self.chkKeyTab.isChecked():
            fKeyTab = self.cbKeyTab.currentIndex()


        intExport=0 
        if self.chkSHPexp.isChecked():  intExport=1
        if self.chkGPKGexp.isChecked(): intExport=2
        return Liste, self.chkDar.isChecked(),self.rBNeu.isChecked(), self.cbGruppe.currentIndex(),self.chk3DDar.isChecked(), self.chkGISDB.isChecked(),intExport, self.chkLeer.isChecked(), fObjKl, self.chkDarObjKl.isChecked(), fKeyTab + 1
   
    def EZUCC7E8BA81F14493981479906904576A7(self,qry):
        self.cbObjKlasse.clear
        if qry:
            while (qry.next()):
                self.cbObjKlasse.addItem(qry.value(1))
        else:

            for g in range(255): 
                self.cbObjKlasse.addItem("Objektklasse-" + str(g))
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        iObjKlasse=s.value( "iObjKlasse", 0)
        self.cbObjKlasse.setCurrentIndex(int(iObjKlasse))

    def EZU3B1BBFAC47624AEF82118DE7647883DE(self,rootname,qry):
        self.EZUB1A3A5F021794B749EB473C9B033A214 (rootname,qry)
        result = self.exec_()

        if result==1:
             return self.EZU06A3014A0EC345C9B52BC3ED5D2B05AA()
        else:

            return None,None,None,None,None,None,None,None,None,None,None


        
