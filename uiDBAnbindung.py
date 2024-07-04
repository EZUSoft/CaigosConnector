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
    from uiAdminerCopy import uiAdminerCopy
    from clsDatenbank import *
    from clsCaigosConnector import *
    from fnc4all import *
    from fnc4CaigosConnector import *
    from fnc4sqlite import *
    from modDownload import *
except:
    from .uiAdminerCopy import uiAdminerCopy
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
        chkurl="https://www.makobo.de/links/Caigos_CheckVersion.php?"
        
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        self.cbServerArt.setCurrentIndex(s.value( "cgserverart", 0 ))
        self.EZU87A85E77E1144493A3CBE98594204B87()
        
        self.leAktDatName.setText(s.value( "admindatei", "" ))
        
        bpwdauslesen = True if s.value( "pwdauslesen", "Nein" ) == "Ja" else False
        self.chkPwdAuslesen.setChecked(bpwdauslesen)
        self.EZUF8D2E5B23A7A4EDAA256EC4C159D54B2()
        
        self.cbVersion.setCurrentIndex(s.value( "cgversion", 0 ))
        self.EZUB154CA6169DE4C0784D284B246CC18EA()
        
        self.leSERVICE.setText( s.value( "service", "" ) )
        self.leHostServer.setText( self.deftext (s.value( "host"), "localhost" ) )
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
        self.btnMSSQLViews.clicked.connect(self.EZU3DD852D4A69E4CEF9411FBC7E1012503) 
        
        self.btnDatAuswahl.clicked.connect(self.EZU3A211ED24CAE49969D3BF8E83949FD61)
        self.chkManuel.clicked.connect(self.EZUF8D2E5B23A7A4EDAA256EC4C159D54B2)
        self.chkPwdAuslesen.clicked.connect(self.EZUF8D2E5B23A7A4EDAA256EC4C159D54B2)
        self.cbVersion.currentIndexChanged.connect(self.EZUB154CA6169DE4C0784D284B246CC18EA)
        self.cbProjektAusAdm.currentIndexChanged.connect(self.EZU6C39AF46E86A4103A0BD15324E9F61EA)
        self.cbServerArt.currentIndexChanged.connect(self.EZU87A85E77E1144493A3CBE98594204B87)
        
        EZU1C9648848F904099A178AD545D77A882()
        self.setWindowTitle (EZUAC62A428AD734562A807B0FF8D792A61())

    def EZU6438B2850C414D7C8F6A74E455C1C648(self, dbName):
        prjList = [""]
        sSQL = ('SELECT DBPROJECT_PRJNAME AS prjName '
                'FROM DBPROJECT '
                'INNER JOIN DBCONNECT ON DBPROJECT.DBPROJECT_IDDBCONNECT = DBCONNECT.DBCONNECT_ID '
                'WHERE lower([DBCONNECT_PACTORTYPE])="postgresql" or lower([DBCONNECT_PACTORTYPE])="mssql" '
                'order by DBPROJECT_PRJNAME')

        if dbName == "":
            return False

        if not os.path.isfile (dbName):
            errbox("SQLite-Datei:\n" + dbName + "\nnicht gefunden")
            return False
        
        if EZUDE54B9C460DD4EE199CA6B2F9CAE4144 (dbName):
            errbox("SQLite-Datei:\n" + dbName + "\nim WAL-Modus")
            return False
            
        rs = EZU32315C76E6A04BD1B46E5CB2DE026E79(dbName,sSQL, False)
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
    
    def EZU87A85E77E1144493A3CBE98594204B87 (self):

        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        s.setValue( "cgserverart", self.cbServerArt.currentIndex() )

        if self.cbServerArt.currentIndex() == 0:
            self.lbHostServer.setText('Host')
            self.leSERVICE.show()
            self.lbSERVICE.show()
            self.lePORT.show()
            self.lbPORT.show()

        if self.cbServerArt.currentIndex() == 1:
            self.lbHostServer.setText('Server')
            self.leSERVICE.hide()
            self.lbSERVICE.hide()
            self.lePORT.hide()
            self.lbPORT.hide()
            self.btnMSSQLViews.setText("Abfragen (neu) generieren")

        self.btnMSSQLViews.setVisible(self.cbServerArt.currentIndex() == 1)
        self.EZUF8D2E5B23A7A4EDAA256EC4C159D54B2()   

    
    def EZU6C39AF46E86A4103A0BD15324E9F61EA (self):
        prjName= self.cbProjektAusAdm.currentText()
        dbName = self.leAktDatName.text()
        if prjName == "":
            return False
        
        sSQL = ('SELECT DBPROJECT_PRJNAME AS prjName, DBCONNECT_SERVERNAME AS pgServer, DBCONNECT_DATABASENAME AS pgDatabase, '
                'DBCONNECT_USERNAME AS pgUserName, DBCONNECT_PASSWORD AS pgPasswd, DBPROJECT_REFSYSTEM AS txtEPSG, DBCONNECT.DBCONNECT_PACTORTYPE as artServer '
                'FROM DBPROJECT '
                'INNER JOIN DBCONNECT ON DBPROJECT.DBPROJECT_IDDBCONNECT = DBCONNECT.DBCONNECT_ID '
                'WHERE DBPROJECT_PRJNAME=\'' + prjName + '\';')
        
        if EZUDE54B9C460DD4EE199CA6B2F9CAE4144 (dbName):
            errbox("SQLite-Datei:\n" + dbName + "\nim WAL-Modus")
            return False
            
        rs = EZU32315C76E6A04BD1B46E5CB2DE026E79(dbName,sSQL, False)
        if rs is None:
            if len(EZU03F45B01171E465F835613DBEE097689()) > 0:
                errbox("\n\n".join(EZU03F45B01171E465F835613DBEE097689()))
                EZU0BAA4CE0798E48099454390EF2BC83A4()   
                
        for row in rs:
            if row["artServer"].upper() == 'POSTGRESQL'.upper():self.cbServerArt.setCurrentIndex(0)
            if row["artServer"].upper() == 'MSSQL'.upper():self.cbServerArt.setCurrentIndex(1)
            if row["artServer"].upper() == 'ORACLE'.upper():
                msgbox ("Oracle wird noch nicht unterstützt")
            self.leCGProjektName.setText(prjName)
            v = row["pgServer"].split(":")
            if len(v) == 1:
                self.leHostServer.setText(row["pgServer"])
                self.lePORT.setText('0')
            else:
                self.leHostServer.setText(row["pgServer"].split(":")[0])
                self.lePORT.setText(row["pgServer"].split(":")[1])
            
            self.leDBNAME.setText(row["pgDatabase"])
            self.leUID.setText(row["pgUserName"])
            



            print (len(row["pgPasswd"]),self.cbVersion.currentIndex())

            
            if len(row["pgPasswd"]) == 96 and self.cbVersion.currentIndex() != 2:
                self.cbVersion.setCurrentIndex (2)
                msgbox ('Wechsel auf Version: ' + self.cbVersion.currentText())
            if len(row["pgPasswd"]) != 96 and self.cbVersion.currentIndex() != 1:
                self.cbVersion.setCurrentIndex (1)
                msgbox ('Wechsel auf Version: ' + self.cbVersion.currentText())
            
            if len(row["pgPasswd"]) != 96:
                self.lePWD.setText(row["pgPasswd"])
                
            self.leEPSG.setText(row["txtEPSG"])
            
    def EZUB154CA6169DE4C0784D284B246CC18EA(self):

        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        s.setValue( "cgversion", self.cbVersion.currentIndex() )
        

        self.leEPSG.setEnabled(self.cbVersion.currentIndex() == 0)
        
        self.cbProjektAusAdm.setVisible(self.cbVersion.currentIndex() >= 1)    
        self.lbProjektAusADM.setVisible(self.cbVersion.currentIndex() >= 1)  
        

        self.chkPwdAuslesen.setEnabled (not (self.cbVersion.currentIndex() == 2))
        self.chkPwdAuslesen.setChecked (not (self.cbVersion.currentIndex() == 2))

        
        
        
        self.setWindowTitle (EZUAC62A428AD734562A807B0FF8D792A61(self.cbVersion.currentIndex()))
        if self.cbVersion.currentIndex() == 0:
            self.lbProjektOrDB.setText(u"Ausgewählte database.ini")
            self.leAktDatName.setText("")
            self.leCGSignaturPfad.setText( QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() ).value( "cgsignaturpfad", "") ) 
            

        if self.cbVersion.currentIndex() >= 1: 
            self.lbProjektOrDB.setText(u"Ausgewählte Administrationsdatenbank")  


            lastAdmDat=self.leAktDatName.text().strip()
            if lastAdmDat == '':
                return False
                

            if lastAdmDat == EZU1530D0D3A4E04F2D931FB43613DB642F():

                if (not os.path.isfile (lastAdmDat)):
                    errbox("Temporäre Kopie der Adminer DB nicht gefunden")
                    self.leAktDatName.setText('')
                    return False
                else:    
                    lastAdmDat, unused = EZU031BEC08077544EEB1B60AD776DF6A77 (EZU1530D0D3A4E04F2D931FB43613DB642F() + '.meta')
                    if lastAdmDat == '#LEER#': # zugehörige Metadatei konnte nicht gelesen werden
                        self.leAktDatName.setText('')
                        errbox("Temporäre Kopie der Adminer DB unvollständig")
                        return False
            else:

                if (not os.path.isfile (lastAdmDat)):
                    errbox("Adminer DB:\n" + lastAdmDat + "\nnicht gefunden")
                    self.leAktDatName.setText('')
                    return False            

            self.leCGSignaturPfad.setText(os.path.dirname(lastAdmDat)+'/signaturen/')
            if self.leAktDatName.text() != "":
                if not os.path.isfile (self.leAktDatName.text()):
                    errbox("SQLite-Datei:\n" + self.leAktDatName.text() + "\nnicht gefunden")
                    self.leAktDatName.setText("")
                    self.leCGSignaturPfad.setText("")
                    QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() ).setValue( "admindatei", "" )
                    return False
            

            self.EZU6438B2850C414D7C8F6A74E455C1C648(self.leAktDatName.text())


        self.EZUF8D2E5B23A7A4EDAA256EC4C159D54B2()
        
    def EZUF8D2E5B23A7A4EDAA256EC4C159D54B2(self):
        bFrei= self.chkManuel.isChecked()
        self.leSERVICE.setEnabled(bFrei)
        self.leHostServer.setEnabled(bFrei)
        self.lePORT.setEnabled(bFrei)
        self.leDBNAME.setEnabled(bFrei)
        self.leUID.setEnabled(bFrei)
        self.lePWD.setEnabled(bFrei or (not self.chkPwdAuslesen.isChecked()))
        self.leCGSignaturPfad.setEnabled(bFrei)
        self.leCGProjektName.setEnabled(bFrei) 
        self.cbServerArt.setEnabled(bFrei)

    
    def EZU54ECA169849940E5896CAB681E8B2FB9(self,IniDatNam):
        try:
            Fehler=""
            iDatNum = open(IniDatNam)

            for iZeile in iDatNum:
                iZeile=iZeile.replace("\n","").strip()
                if iZeile[:12] == "_PactorType=" :
                    if iZeile[12:].strip().upper() == ("PostgreSQL").upper():self.cbServerArt.setCurrentIndex(0)
                    if iZeile[12:].strip().upper() == ("MSSQL").upper():  

                        msgbox ("MSSQL wird erst ab CAIGOS 2016 unterstützt")
                        iDatNum.close()
                        return None
                    if iZeile[12:].strip().upper() == ("Oracle").upper(): 
                        msgbox ("Oracle wird noch nicht unterstützt")
                        iDatNum.close()
                        return None
                    self.EZU87A85E77E1144493A3CBE98594204B87()
            iDatNum.close()
               

            iDatNum = open(IniDatNam)
            for iZeile in iDatNum:
                iZeile=iZeile.replace("\n","").strip()
                if iZeile[:12] == "SERVER NAME=" :
                    if self.cbServerArt.currentIndex() == 0:  

                        v = iZeile[12:].split(":")
                        if len(v) != 2:
                            Fehler=Fehler + "\nFehler Servername:\n Erwartet: SERVER NAME=<rechner>:<port> \n Gelesen: " + iZeile[:12]
                        else:
                            self.leHostServer.setText(v[0].strip())
                            self.lePORT.setText(v[1].strip())
                    
                    if self.cbServerArt.currentIndex() == 1:  

                        v = iZeile[12:].split(":")
                        if len(v) == 2:
                            self.leHostServer.setText(v[0].strip())
                            self.lePORT.setText(v[1].strip())
                        else:
                            self.leHostServer.setText(iZeile[12:].strip())
                            self.lePORT.setText('0')
                            
                if iZeile[:14] == "DATABASE NAME=" :
                    self.leDBNAME.setText(iZeile[14:].strip())
                if iZeile[:10] == "USER NAME=" :
                    self.leUID.setText(iZeile[10:].strip())             
                if iZeile[:9] == "PASSWORD=" :
                    self.lePWD.setText(iZeile[9:].strip()) 
            self.leCGSignaturPfad.setText(os.path.dirname(IniDatNam)+'/signatur/')  
            iDatNum.close()
            if Fehler:
                QMessageBox.critical( None, u"Es sind Fehler aufgetreten", Fehler )
            else:
                return True
        except: 
            EZU2CC2ED60E16A4317BA8BEBE4D6120301 ()
    
    def EZU6A6AAFC991224C2EA82940C59868EADF(self,AdmDatNam, prjName):
        try:
            Fehler=""
            iDatNum = open(IniDatNam)
            for iZeile in iDatNum:
                iZeile=iZeile.replace("\n","")
                if iZeile[:12] == "SERVER NAME=" :
                    v = iZeile[12:].split(":")
                    if len(v) != 2:
                        Fehler=Fehler + "\nFehler Servername:\n Erwartet: SERVER NAME=<rechner>:<port> \n Gelesen: " + iZeile[:12]
                    else:
                        self.leHostServer.setText(v[0].strip())
                        self.lePORT.setText(v[1].strip())
                if iZeile[:14] == "DATABASE NAME=" :
                    self.leDBNAME.setText(iZeile[14:].strip())
                if iZeile[:10] == "USER NAME=" :
                    self.leUID.setText(iZeile[10:].strip())             
                if iZeile[:9] == "PASSWORD=" :
                    self.lePWD.setText(iZeile[9:].strip()) 
            iDatNum.close()


            
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
                iDatNum.close()
                if PrjName == "":
                   Fehler="Projektname konnte nicht ermittelt werden.\nEs wird der Datenbankname benutzt"
            if Fehler:
                QMessageBox.critical( None, u"Es sind Fehler aufgetreten", Fehler )
        except: 
            EZU2CC2ED60E16A4317BA8BEBE4D6120301 () 
        return PrjName
        
    def EZU3A211ED24CAE49969D3BF8E83949FD61(self):
        dummy="https://www.makobo.de/links/Caigos_CheckImport.php?"
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
                    if not self.EZU54ECA169849940E5896CAB681E8B2FB9(iniDat):
                        return False
                    

                    prjDat=""
                    for f in os.listdir(os.path.dirname(iniDat)):
                        if f.lower().endswith(".prj"):
                             prjDat=os.path.dirname(iniDat) + "/" + f
                    PrjName=self.EZUF74320A59E5B4F2D9CC6820DC6325122(prjDat)
                    if PrjName == "":
                       PrjName=self.leDBNAME.text().strip() 
                    
                    self.leCGProjektName.setText(EZUF0AF6D30C6EB4BE8A558B27DA05DBD21(PrjName))
                    self.leAktDatName.setText(iniDat)
                    
            if self.cbVersion.currentIndex() >= 1:


                if self.leAktDatName.text().strip() == "":
                    lastAdmDat = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() ).value( "admindatei", "" )
                else:
                    lastAdmDat = self.leAktDatName.text().strip()

                if lastAdmDat == EZU1530D0D3A4E04F2D931FB43613DB642F():
                    lastAdmDat, unused = EZU031BEC08077544EEB1B60AD776DF6A77 (EZU1530D0D3A4E04F2D931FB43613DB642F() + '.meta')
                if myqtVersion == 4:
                    admDat = QFileDialog.getOpenFileName(None, 'Administrationsdatenbank  im CAIGOS-Server Ordner', 
                             lastAdmDat , "database (*.cgbin)")
                else:
                    admDat = QFileDialog.getOpenFileName(self, 'Administrationsdatenbank  im CAIGOS-Server Ordner', 
                             lastAdmDat , "database (*.cgbin);; Sicherung (*.bak);;Alle Dateien (*.*)")[0]

                if admDat:

                    self.leCGSignaturPfad.setText(os.path.dirname(admDat)+'/signaturen/')
                    servEXE=os.path.dirname(admDat) + r'\PACTOR_Service.exe'
                    vEXE='#'
                    if os.path.isfile(servEXE):
                        vEXE, dEXE = EZU7E0D638197C34356A2E45006516F0C4F(servEXE)
                        try:
                            s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
                            if (s.value( "status","") != "false"):
                                check= dummy  + EZU11DE7CED39F2439E803B738E6E678716() + "|" + str(EZUC86841CA58BC4846B265D42D4397141D()) + ":" + EZUF9FB4AE0A2B44C8B8313441BFB307407() + ":EXE=" + dEXE + '_' + vEXE
                                EZUC8D59B20568948389B1274373D8E0990(check,EZUE2CC6C01835941909C82368EAB1CE1E2()+'test.zip')
                        except:
                            pass

                    
                    if EZUDE54B9C460DD4EE199CA6B2F9CAE4144 (admDat):
                        cls=uiAdminerCopy(admDat)
                        cls.exec_()
                        Antw=cls.EZU5FD59B408C704253BE664AD8D5A06359()

                        if Antw == '#ABBRUCH#' or Antw == '#Kopieren#':
                            return False
                        else:
                            admDat = Antw
                            
                    if self.EZU6438B2850C414D7C8F6A74E455C1C648 (admDat):
                        self.leAktDatName.setText(admDat)
                    if vEXE == '19.3' and self.cbVersion.currentIndex() != 2:
                        self.cbVersion.setCurrentIndex (2)
                        msgbox ('Wechsel auf Version: ' + self.cbVersion.currentText())
                    if vEXE == '19.2' and self.cbVersion.currentIndex() != 1:
                        self.cbVersion.setCurrentIndex (1)
                        msgbox ('Wechsel auf Version: ' + self.cbVersion.currentText())
  





        
        except Exception as e:
            EZU2CC2ED60E16A4317BA8BEBE4D6120301 ()
    
    def deftext(self,Wert,DefWert):


        if Wert == None:
            return DefWert        
        if str(Wert).strip() == "":
            return DefWert
        else:
            return str(Wert)

















    def EZU32A31DECC681474E9B2AFD4A5DC1958A(self, error=True):
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        s.setValue( "cgversion", self.cbVersion.currentIndex() )
        s.setValue( "cgserverart", self.cbServerArt.currentIndex() )
        if self.cbVersion.currentIndex() == 0:
            s.setValue( "dbinidatei", self.leAktDatName.text().strip() )
        if self.cbVersion.currentIndex() >= 1:
            s.setValue( "admindatei", self.leAktDatName.text().strip() )
  
        s.setValue( "service", self.leSERVICE.text().strip() )
        s.setValue( "host", self.leHostServer.text().strip() )
        s.setValue( "port", self.lePORT.text().strip() )
        s.setValue( "dbname", self.leDBNAME.text().strip() )
        s.setValue( "uid", self.leUID.text().strip() )
        s.setValue( "pwd", self.lePWD.text().strip() )
        s.setValue( "pwdauslesen", "Ja" if self.chkPwdAuslesen.isChecked() == True else "Nein")      
        s.setValue( "epsg", self.leEPSG.text().strip() )
        s.setValue( "cgsignaturpfad", self.leCGSignaturPfad.text().strip() )
        s.setValue( "cgprojektname", EZUF0AF6D30C6EB4BE8A558B27DA05DBD21(self.leCGProjektName.text().strip()) )        


    def EZU3DD852D4A69E4CEF9411FBC7E1012503(self):
        service = self.leSERVICE.text().strip()
        host = self.leHostServer.text().strip()
        port = self.lePORT.text().strip()
        dbname = self.leDBNAME.text().strip()
        uid = self.leUID.text().strip()
        pwd = self.lePWD.text().strip()
        db = pgOpenDatabase(service, host, port, dbname, uid, pwd)
        if EZUC0AEDD5F47634D6B97D2BEF91F31FEC1 (db):
            msgbox ("Abfragen wurden generiert")
        else:
            if len(EZU03F45B01171E465F835613DBEE097689()) > 0:
                Quelle='uiDBAnbindung(' + str(sys._getframe(0).f_lineno) + ') '
                errbox("* " + "\n* ".join(EZU03F45B01171E465F835613DBEE097689()),Quelle) 
                EZU0BAA4CE0798E48099454390EF2BC83A4()
                
    def EZU181874100A5A4980BD95DAA0A4F1AFA8(self):
        service = self.leSERVICE.text().strip()
        host = self.leHostServer.text().strip()
        port = self.lePORT.text().strip()
        dbname = self.leDBNAME.text().strip()
        uid = self.leUID.text().strip()
        pwd = self.lePWD.text().strip()
        chkDB = pgOpenDatabase(service, host, port, dbname, uid, pwd)
        chkDB.EZU8011F18E65644E5D9231765F31D7EE19(self.cbVersion.currentIndex(), self.leEPSG.text().strip(),self.leCGSignaturPfad.text().strip(),
                             EZUF0AF6D30C6EB4BE8A558B27DA05DBD21(self.leCGProjektName.text().strip()),None, False) 

    def EZU0F29DFD759404DC0AD7127E7983E3254(self):

        self.EZU32A31DECC681474E9B2AFD4A5DC1958A()
        

        if self.cbServerArt.currentIndex() == 1:
            bMSQLFehlt=False 
            db=pgCurrentDB()
            if db.EZU8011F18E65644E5D9231765F31D7EE19(None,None,None,None, None, True):
                iServer=EZU50464908A0F8417AA7B9045C4E9B1F6A() 
                if iServer == 1:
                    if not EZUDFCE1DA9263240889EF03443BF48E294 (db):
                        if len(EZU03F45B01171E465F835613DBEE097689()) > 0:
                            errbox(EZU03F45B01171E465F835613DBEE097689())
                            EZU0BAA4CE0798E48099454390EF2BC83A4()
                        else:
                            bMSQLFehlt=True
                        db=None  
            if bMSQLFehlt:
                s = "Die MSSQL-Abfragen wurden nicht (vollständig) generiert"


                sHinweis="In der MSQL-Datenbank müssen Sichten (VIEW) erzeugt werden,\n"
                sHinweis=sHinweis + "um mit QGIS auf die Geodaten zugreifen zu können.\n\n"
                sHinweis=sHinweis + "Sollen die Abfragen jetzt erzeugt werden?"
                reply = QMessageBox.question(None, s,sHinweis, QMessageBox.Yes |  QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.EZU3DD852D4A69E4CEF9411FBC7E1012503()


        QDialog.accept(self) 


 


























