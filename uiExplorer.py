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
        self.chkSHPexp.clicked.connect(self.EZU663B59541A9B4AC1B23819C4A6E3E89B)  
        self.chkGISDB.clicked.connect(self.EZU663B59541A9B4AC1B23819C4A6E3E89B)      
        self.chkFiltObjKl.clicked.connect(self.EZU663B59541A9B4AC1B23819C4A6E3E89B)
        
        chkurl="http://www.makobo.de/links/Caigos_CheckVersion.php?"
        self.EZU1C9648848F904099A178AD545D77A882()

        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        bGenDar = True  if s.value( "bGenDar", "Ja" )   == "Ja"   else False
        bPrjNeu = True  if s.value( "bPrjNeu", "Ja" )   == "Ja"   else False
        bLeer = False   if s.value( "bLeer", "Nein" )   == "Nein" else True
        bDBTab = False  if s.value( "bDBTab", "Nein" )  == "Nein" else True
        bFiltObjKl = False  if s.value( "bFiltObjKl", "Nein" )  == "Nein" else True
        bDarObjKl = False   if s.value( "bDarObjKl", "Nein" )   == "Nein" else True
        b3DDar = False  if s.value( "b3DDar", "Nein" )  == "Nein" else True
        bSHPexp = False if s.value( "bSHPexp", "Nein" ) == "Nein" else True
        bSaveDar = True if s.value( "bSaveDar", "Ja" )  == "Ja"   else False
        bOnlyDarField = True if s.value( "bOnlyDarField", "Ja" )  == "Ja"   else False
        bNoGISDBIntern = True if s.value( "bNoGISDBIntern", "Ja" )  == "Ja"   else False
        chkurl="http://www.makobo.de/links/Caigos_CheckVersion.php?"   
        iCodePage=s.value( "iCodePage", 0)
        iObjKlasse=s.value( "iObjKlasse", 0)

        self.txtZielPfad.setText(s.value( "txtSHPDir", "" ))
        
        self.cbCharSet.addItems(self.charsetList)
        self.cbCharSet.setCurrentIndex(int(iCodePage))

        self.cbObjKlasse.setCurrentIndex(int(iObjKlasse))        
 
        iGruppe=s.value( "iDarGruppe", 0 )

        self.chkDar.setChecked(bGenDar)
        self.chkGISDB.setChecked(bDBTab)
        self.chkFiltObjKl.setChecked(bFiltObjKl)
        self.chkDarObjKl.setChecked(bDarObjKl)
        self.chkLeer.setChecked(bLeer)
        self.chk3DDar.setChecked(b3DDar)
        self.chkDarObjKl.setChecked(bDarObjKl)
        
        self.chkSHPexp.setChecked(bSHPexp)
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
        

        for g in range(5): 
            self.cbGruppe.addItem("Gruppe-" + str(g))
        self.cbGruppe.setCurrentIndex(iGruppe)  
    
    def EZU1C9648848F904099A178AD545D77A882(self):
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        if (s.value( "status","")==""):
            ret=EZU39041CAE6C224B57B5E3F261A44FA369("http://www.makobo.de/")
            s.setValue("status",ret[0])
            if ret[0]:
                s.setValue("status",ret[1])
        self.setWindowTitle (EZUAC62A428AD734562A807B0FF8D792A61())               
    def EZU663B59541A9B4AC1B23819C4A6E3E89B(self):
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        bGenSHP = self.chkSHPexp.isChecked() 
        bDBTab  = self.chkGISDB.isChecked()
        bFiltObjKl= self.chkFiltObjKl.isChecked()

        self.browseZielPfad.setEnabled(bGenSHP) 
        self.cbCharSet.setEnabled(bGenSHP) 
        self.lbCharSet.setEnabled(bGenSHP) 
        self.chkSaveDar.setEnabled(bGenSHP) 
        self.chkOnlyDarField.setEnabled(bGenSHP) 
        self.chkNoGISDBIntern.setEnabled(bDBTab and bGenSHP) 
        self.cbObjKlasse.setEnabled(bFiltObjKl)
        if bGenSHP:
            self.txtZielPfad.setPlaceholderText(self.tr("Specify destination path")) 
        else:
            self.txtZielPfad.setPlaceholderText("") 
            
        if (s.value( "status","")==''):
            self.chkDar.setEnabled(False)
            self.chkDar.setChecked(False)          
        else:
            self.chkDar.setEnabled(s.value( "status","")==b'ok')
            if (s.value( "status","")!=b'ok'):
                self.chkDar.setChecked(False)    
    
    def EZU5B07B73B000A446CBEFCD87EF2D82514(self):
        self.chkDar.setChecked(True)
        self.chkGISDB.setChecked(False)
        self.chkFiltObjKl.setChecked(False)
        self.chkDarObjKl.setChecked(False)
        self.chkLeer.setChecked(False)
        self.chk3DDar.setChecked(False)
        
        self.chkSHPexp.setChecked(False)
        self.chkSaveDar.setChecked(False)
        self.chkOnlyDarField.setChecked(False)
        self.chkNoGISDBIntern.setChecked(False)
        QSettings("EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA()).setValue("status",'')
        self.EZU1C9648848F904099A178AD545D77A882()
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
        shpDirName = QFileDialog.getExistingDirectory(self, u"Verzeichnis für Shape-Dateien wählen",lastSHPDir,flags)
        if shpDirName != "":
            if len( os.listdir( shpDirName ) ) > 0:
                reply = QMessageBox.question(None, u'Verzeichnis ist nicht leer',u"Namensgleiche Shape-Dateien werden überschrieben", QMessageBox.Yes |  QMessageBox.Cancel, QMessageBox.Cancel)
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
        s.setValue( "bDarObjKl", "Ja" if self.chkDarObjKl.isChecked() == True else "Nein")
        s.setValue( "bLeer", "Ja" if self.chkLeer.isChecked() == True else "Nein")
        s.setValue( "b3DDar", "Ja" if self.chk3DDar.isChecked() == True else "Nein")
        s.setValue( "bSHPexp", "Ja" if self.chkSHPexp.isChecked() == True else "Nein")
        s.setValue( "bSaveDar", "Ja" if self.chkSaveDar.isChecked() == True else "Nein")
        s.setValue( "bOnlyDarField", "Ja" if self.chkOnlyDarField.isChecked() == True else "Nein")
        s.setValue( "bNoGISDBIntern", "Ja" if self.chkNoGISDBIntern.isChecked() == True else "Nein")
       
        s.setValue( "iCodePage", self.cbCharSet.currentIndex())
        s.setValue( "iObjKlasse", self.cbObjKlasse.currentIndex())
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



        if self.chkSHPexp.isChecked():
            ZielPfad=self.txtZielPfad.text()                
            if ZielPfad == "":
                QMessageBox.critical(None, u"SHP-Zielpfad nicht gesetzt", u"Bitte Shape-Zielpfad wählen") 
                return
            if ZielPfad[:-1] != "/" and ZielPfad[:-1] != "\\":
                    ZielPfad=ZielPfad + "/"
            if not os.path.exists(ZielPfad):
                QMessageBox.critical(None, u"Shape Zielpfad nicht gefunden", ZielPfad)
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


        return Liste, self.chkDar.isChecked(),self.rBNeu.isChecked(), self.cbGruppe.currentIndex(),self.chk3DDar.isChecked(), self.chkGISDB.isChecked(),self.chkSHPexp.isChecked(), self.chkLeer.isChecked(), fObjKl, self.chkDarObjKl.isChecked()
   
    def EZUCC7E8BA81F14493981479906904576A7(self,qry):
        self.cbObjKlasse.clear
        while (qry.next()):
            self.cbObjKlasse.addItem(qry.value(1))
        
    def EZU3B1BBFAC47624AEF82118DE7647883DE(self,rootname,qry):
        self.EZUB1A3A5F021794B749EB473C9B033A214 (rootname,qry)
        result = self.exec_()

        if result==1:
             return self.EZU06A3014A0EC345C9B52BC3ED5D2B05AA()
        else:

            return None,None,None,None,None,None,None,None,None,None


        
if __name__ == "__main__":
    uri = QgsDataSourceUri()
    app = QApplication(sys.argv)
    cls=uiExplorer()
    result=cls.exec_()
 
