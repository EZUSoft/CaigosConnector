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
    from PyQt5 import QtGui, uic
    from PyQt5.QtCore import  QDir
    from PyQt5.QtWidgets import *
    myqtVersion = 5
except:
    from PyQt4 import QtGui, uic
    from PyQt4.QtCore import  QDir, QT_VERSION_STR
    from PyQt4.QtGui  import *
    myqtVersion = 4
    def QgsDataSourceUri():
        return QgsDataSourceURI()

try:
    from clsDatenbank import *
    from clsCaigosConnector import *
    from fnc4all import *
    from fnc4CaigosConnector import *
    from fnc4sqlite import *
    from modDownload import *
except:
    from .clsDatenbank import *
    from .clsCaigosConnector import *
    from .fnc4all import *
    from .fnc4CaigosConnector import *
    from .fnc4sqlite import *
    from .modDownload import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'uiDBAnbindung.ui'))



class uiDBAnbindung(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(uiDBAnbindung, self).__init__(parent)
        self.setupUi(self)
        chkurl="http://www.makobo.de/links/Caigos_CheckVersion.php?"
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        self.cbVersion.setCurrentIndex(s.value( "cgversion", 0 ))
        self.EZUB154CA6169DE4C0784D284B246CC18EA()
        
        self.leSERVICE.setText( s.value( "service", "" ) )
        self.leHOST.setText( self.deftext (s.value( "host"), "localhost" ) )
        self.lePORT.setText( self.deftext (s.value( "port"), "5432") ) 
        self.leDBNAME.setText( s.value( "dbname", "" ) )
        self.leUID.setText( s.value( "uid", "" ))
        self.lePWD.setText( s.value( "pwd", "" ))
        self.leEPSG.setText( self.deftext(s.value( "epsg"), "25833" ) )
        self.leCGSignaturPfad.setText( s.value( "cgsignaturpfad", "") )
        self.leCGProjektName.setText( s.value( "cgprojektname", "") )
        
        self.bb.accepted.connect(self.EZU0F29DFD759404DC0AD7127E7983E3254) 
        self.bb.rejected.connect(self.reject)    
        self.btnTest.clicked.connect(self.EZU181874100A5A4980BD95DAA0A4F1AFA8) 
        self.btnDatAuswahl.clicked.connect(self.EZU3A211ED24CAE49969D3BF8E83949FD61)
        self.chkManuel.clicked.connect(self.EZUF8D2E5B23A7A4EDAA256EC4C159D54B2)
        self.cbVersion.currentIndexChanged.connect(self.EZUB154CA6169DE4C0784D284B246CC18EA)
        self.cbProjektAusAdm.currentIndexChanged.connect(self.EZU6C39AF46E86A4103A0BD15324E9F61EA)
        if (s.value( "status","")==""):
            ret=EZU39041CAE6C224B57B5E3F261A44FA369("http://www.makobo.de/")
            s.setValue("status",ret[0])
            if ret[0]:
                s.setValue("status",ret[1])

    def EZU6438B2850C414D7C8F6A74E455C1C648(self, dbName):
        prjList = [""]
        sSQL = ('SELECT DBPROJECT_PRJNAME AS prjName '
                'FROM DBPROJECT '
                'INNER JOIN DBCONNECT ON DBPROJECT.DBPROJECT_IDDBCONNECT = DBCONNECT.DBCONNECT_ID WHERE lower([DBCONNECT_PACTORTYPE])="postgresql";')
        if dbName == "":
            return False

        if not os.path.isfile (dbName):
            errbox("SQLite-Datei:\n" + dbName + "\nnicht gefunden")
            return False
        
        rs = EZU32315C76E6A04BD1B46E5CB2DE026E79(dbName,sSQL)
        if rs is None:
            if len(EZU03F45B01171E465F835613DBEE097689()) > 0:
                errbox("\n\n".join(EZU03F45B01171E465F835613DBEE097689()))
                EZU0BAA4CE0798E48099454390EF2BC83A4()
        else:
            for row in rs:
                prjList.append (row["prjName"])

        

        self.cbProjektAusAdm.setEnabled(len(prjList) > 0)
        if len(prjList) > 0:            

            self.cbProjektAusAdm.clear()
            self.cbProjektAusAdm.addItems(prjList)
        
        return True        
    
    def EZU6C39AF46E86A4103A0BD15324E9F61EA (self):
        prjName= self.cbProjektAusAdm.currentText()
        dbName = self.leAktDatName.text()
        if prjName == "":
            return False
        
        sSQL = ('SELECT DBPROJECT_PRJNAME AS prjName, DBCONNECT_SERVERNAME AS pgServer, DBCONNECT_DATABASENAME AS pgDatabase, DBCONNECT_USERNAME AS pgUserName, DBCONNECT_PASSWORD AS pgPasswd, DBPROJECT_REFSYSTEM AS txtEPSG '
                'FROM DBPROJECT '
                'INNER JOIN DBCONNECT ON DBPROJECT.DBPROJECT_IDDBCONNECT = DBCONNECT.DBCONNECT_ID '
                'WHERE DBPROJECT_PRJNAME=\'' + prjName + '\';')

        rs = EZU32315C76E6A04BD1B46E5CB2DE026E79(dbName,sSQL)
        if rs is None:
            if len(EZU03F45B01171E465F835613DBEE097689()) > 0:
                errbox("\n\n".join(EZU03F45B01171E465F835613DBEE097689()))
                EZU0BAA4CE0798E48099454390EF2BC83A4()   
                
        for row in rs:
            self.leCGProjektName.setText(prjName)
            self.leHOST.setText(row["pgServer"].split(":")[0])
            self.lePORT.setText(row["pgServer"].split(":")[1])
            self.leDBNAME.setText(row["pgDatabase"])
            self.leUID.setText(row["pgUserName"])
            self.lePWD.setText(row["pgPasswd"])
            self.leEPSG.setText(row["txtEPSG"])
            
    def EZUB154CA6169DE4C0784D284B246CC18EA(self):

        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        s.setValue( "cgversion", self.cbVersion.currentIndex() )
        
        self.setWindowTitle (EZUAC62A428AD734562A807B0FF8D792A61(self.cbVersion.currentIndex()))
        if self.cbVersion.currentIndex() == 0:
            self.lbProjektOrDB.setText(u"Ausgewählte database.ini")
            self.leAktDatName.setText("")
            self.leCGSignaturPfad.setText( QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() ).value( "cgsignaturpfad", "") ) 
            

        if self.cbVersion.currentIndex() == 1: 
            self.lbProjektOrDB.setText(u"Ausgewählte Administrationsdatenbank")  
            admDat = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() ).value( "admindatei", "" )
            self.leAktDatName.setText( admDat) 
            self.leCGSignaturPfad.setText(os.path.dirname(admDat)+'/signaturen/')
            if self.leAktDatName.text() != "":
                if not os.path.isfile (self.leAktDatName.text()):
                    errbox("SQLite-Datei:\n" + self.leAktDatName.text() + "\nnicht gefunden")
                    self.leAktDatName.setText("")
                    self.leCGSignaturPfad.setText("")
                    QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() ).setValue( "admindatei", "" )
                    return False
            
            self.EZU6438B2850C414D7C8F6A74E455C1C648(self.leAktDatName.text())

         
        self.cbProjektAusAdm.setVisible(self.cbVersion.currentIndex() == 1)    
        self.lbProjektAusADM.setVisible(self.cbVersion.currentIndex() == 1)    
        self.leEPSG.setEnabled(self.cbVersion.currentIndex() == 0)
        
    def EZUF8D2E5B23A7A4EDAA256EC4C159D54B2(self):
        bFrei= self.chkManuel.isChecked()
        self.leSERVICE.setEnabled(bFrei)
        self.leHOST.setEnabled(bFrei)
        self.lePORT.setEnabled(bFrei)
        self.leDBNAME.setEnabled(bFrei)
        self.leUID.setEnabled(bFrei)
        self.lePWD.setEnabled(bFrei)
        self.leCGSignaturPfad.setEnabled(bFrei)
        self.leCGProjektName.setEnabled(bFrei) 
    
    def EZU54ECA169849940E5896CAB681E8B2FB9(self,IniDatNam):
        try:
            Fehler=""
            iDatNum = open(IniDatNam)
            z=0
            for iZeile in iDatNum:
                iZeile=iZeile.replace("\n","")
                if iZeile[:12] == "SERVER NAME=" :
                    v = iZeile[12:].split(":")
                    if len(v) != 2:
                        Fehler=Fehler + "\nFehler Servername:\n Erwartet: SERVER NAME=<rechner>:<port> \n Gelesen: " + iZeile[:12]
                    else:
                        self.leHOST.setText(v[0].strip())
                        self.lePORT.setText(v[1].strip())
                if iZeile[:14] == "DATABASE NAME=" :
                    self.leDBNAME.setText(iZeile[14:].strip())
                if iZeile[:10] == "USER NAME=" :
                    self.leUID.setText(iZeile[10:].strip())             
                if iZeile[:9] == "PASSWORD=" :
                    self.lePWD.setText(iZeile[9:].strip()) 
            self.leCGSignaturPfad.setText(os.path.dirname(IniDatNam)+'/signatur/')                    
            if Fehler:
                QMessageBox.critical( None, u"Es sind Fehler aufgetreten", Fehler )
        except: 
            EZU2CC2ED60E16A4317BA8BEBE4D6120301 ()
    
    def EZU6A6AAFC991224C2EA82940C59868EADF(self,AdmDatNam, prjName):
        try:
            Fehler=""
            iDatNum = open(IniDatNam)
            z=0
            for iZeile in iDatNum:
                iZeile=iZeile.replace("\n","")
                if iZeile[:12] == "SERVER NAME=" :
                    v = iZeile[12:].split(":")
                    if len(v) != 2:
                        Fehler=Fehler + "\nFehler Servername:\n Erwartet: SERVER NAME=<rechner>:<port> \n Gelesen: " + iZeile[:12]
                    else:
                        self.leHOST.setText(v[0].strip())
                        self.lePORT.setText(v[1].strip())
                if iZeile[:14] == "DATABASE NAME=" :
                    self.leDBNAME.setText(iZeile[14:].strip())
                if iZeile[:10] == "USER NAME=" :
                    self.leUID.setText(iZeile[10:].strip())             
                if iZeile[:9] == "PASSWORD=" :
                    self.lePWD.setText(iZeile[9:].strip()) 


            
            if Fehler:
                QMessageBox.critical( None, u"Es sind Fehler aufgetreten", Fehler )
        except: 
            EZU2CC2ED60E16A4317BA8BEBE4D6120301 ()

    def EZUF74320A59E5B4F2D9CC6820DC6325122(self,PrjDatNam):
        PrjName=""
        try:
            Fehler=""
            if PrjDatNam == "":
                Fehler = "Keine Projektdatei *.prj gefunden.\nEs wird der Datenbankname benutzt"
            else:
                iDatNum = EZUA4368C0FEFDC4FC1977350D9EDFD8729(PrjDatNam,"r","cp1252")
                PrjName =""
                for iZeile in iDatNum:
                    iZeile=iZeile.replace("\n","")
                    if iZeile[:12] == "ProjectName=" :
                        PrjName=iZeile[12:].strip()                               

                if PrjName == "":
                   Fehler="Projektname konnte nicht ermittelt werden.\nEs wird der Datenbankname benutzt"
            if Fehler:
                QMessageBox.critical( None, u"Es sind Fehler aufgetreten", Fehler )
        except: 
            EZU2CC2ED60E16A4317BA8BEBE4D6120301 () 
        iDatNum.close()
        return PrjName
        
    def EZU3A211ED24CAE49969D3BF8E83949FD61(self):
        try:
            if self.cbVersion.currentIndex() == 0:

                if self.leAktDatName.text().strip() == "":
                    vDat = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() ).value( "dbinidatei", "" )
                else:
                    vDat = self.leAktDatName.text().strip()
                if vDat == "":
                    vDat="database.ini"
                if myqtVersion == 4:
                    iniDat = QFileDialog.getOpenFileName(None, 'database.ini im Projektordner des CAIGOS-SQL-Projektes', 
                             vDat , "database (*.ini)")
                else:
                    iniDat = QFileDialog.getOpenFileName(None, 'database.ini im Projektordner des CAIGOS-SQL-Projektes', 
                             vDat , "database (*.ini)")[0]

                if iniDat:
                    self.EZU54ECA169849940E5896CAB681E8B2FB9(iniDat)
                    

                    prjDat=""
                    for f in os.listdir(os.path.dirname(iniDat)):
                        if f.lower().endswith(".prj"):
                             prjDat=os.path.dirname(iniDat) + "/" + f
                    PrjName=self.EZUF74320A59E5B4F2D9CC6820DC6325122(prjDat)
                    if PrjName == "":
                       PrjName=self.leDBNAME.plainText() 
                    self.leCGProjektName.setText(EZUF0AF6D30C6EB4BE8A558B27DA05DBD21(PrjName))
                    self.leAktDatName.setText(iniDat)
                    
            if self.cbVersion.currentIndex() == 1:


                if myqtVersion == 4:
                    admDat = QFileDialog.getOpenFileName(None, 'Administrationsdatenbank  im CAIGOS-Server Ordner', 
                             self.leAktDatName.text().strip() , "database (*.cgbin)")
                else:
                    admDat = QFileDialog.getOpenFileName(None, 'Administrationsdatenbank  im CAIGOS-Server Ordner', 
                             self.leAktDatName.text().strip() , "database (*.cgbin)")[0]
                
                if admDat:
                    if self.EZU6438B2850C414D7C8F6A74E455C1C648 (admDat):
                        self.leAktDatName.setText(admDat)
                        self.leCGSignaturPfad.setText(os.path.dirname(admDat)+'/signaturen/') 

        except Exception as e:
            EZU2CC2ED60E16A4317BA8BEBE4D6120301 ()
    
    def deftext(self,Wert,DefWert):

        if Wert == None:
            return DefWert        
        if Wert.strip() == "":
            return DefWert
        else:
            return Wert

















    def EZU32A31DECC681474E9B2AFD4A5DC1958A(self, error=True):
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        s.setValue( "cgversion", self.cbVersion.currentIndex() )
        if self.cbVersion.currentIndex() == 0:
            s.setValue( "dbinidatei", self.leAktDatName.text().strip() )
        if self.cbVersion.currentIndex() == 1:
            s.setValue( "admindatei", self.leAktDatName.text().strip() )
  
        s.setValue( "service", self.leSERVICE.text().strip() )
        s.setValue( "host", self.leHOST.text().strip() )
        s.setValue( "port", self.lePORT.text().strip() )
        s.setValue( "dbname", self.leDBNAME.text().strip() )
        s.setValue( "uid", self.leUID.text().strip() )
        s.setValue( "pwd", self.lePWD.text().strip() )
        s.setValue( "epsg", self.leEPSG.text().strip() )
        s.setValue( "cgsignaturpfad", self.leCGSignaturPfad.text().strip() )
        s.setValue( "cgprojektname", EZUF0AF6D30C6EB4BE8A558B27DA05DBD21(self.leCGProjektName.text().strip()) )        


    def EZU181874100A5A4980BD95DAA0A4F1AFA8(self):
        service = self.leSERVICE.text().strip()
        host = self.leHOST.text().strip()
        port = self.lePORT.text().strip()
        dbname = self.leDBNAME.text().strip()
        uid = self.leUID.text().strip()
        pwd = self.lePWD.text().strip()
        chkDB = pgOpenDatabase(service, host, port, dbname, uid, pwd)
        chkDB.EZU8011F18E65644E5D9231765F31D7EE19(self.cbVersion.currentIndex(), self.leEPSG.text().strip(),self.leCGSignaturPfad.text().strip(),
                             EZUF0AF6D30C6EB4BE8A558B27DA05DBD21(self.leCGProjektName.text().strip()),None, False) 

    def EZU0F29DFD759404DC0AD7127E7983E3254(self):    
        self.EZU32A31DECC681474E9B2AFD4A5DC1958A()
        QDialog.accept(self) 


 
if __name__ == "__main__":
    uri = QgsDataSourceUri()
    app = QApplication(sys.argv)


    cls=uiDBAnbindung()
    result=cls.exec_()
 
