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















from qgis.core import *
from qgis.gui import *
from qgis.utils import *
try:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
    from PyQt5.QtWidgets import *
    myqtVersion = 5
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    myqtVersion = 4
    
try:
    if myqtVersion == 4:
        from resourcesqt4 import *
    else:
        from resources import *
    from fnc4all import *
    from fnc4CaigosConnector import *
    from uiExplorer import uiExplorer
    from uiAbout import uiAbout
    from uiDBAnbindung import *
    from clsDatenbank import *
    from modCGSqlCodes import *
    from clsQGISAction import clsQGISAction

except:
    if myqtVersion == 4:
        from .resourcesqt4 import *
    else:
        from .resources import *
        
    from .fnc4all import *
    from .fnc4CaigosConnector import *
    from .uiExplorer import uiExplorer
    from .uiAbout import uiAbout
    from .uiDBAnbindung import *
    from .clsDatenbank import *
    from .modCGSqlCodes import *
    from .clsQGISAction import clsQGISAction




import webbrowser
import os
import getpass

      

class clsCaigosConnector:

    
    def __init__(self, iface):








        self.iface = iface
        try:
            userO=getpass.getuser()
        except:
            userO='#FEHLER#'
        sysO='USERDOMAIN'

        self.plugin_dir = os.path.dirname(__file__)


















        


        user0="QGIS"
        sys0="SYSTEM"
        self.actions = []
        self.menu = self.tr(u'&CAIGOS Datenprovider')
        s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
        s.setValue( "–id–", EZU6F6315D895BC410ABCE5C02C6E0C5F14( str(userO) + '|' + str(os.getenv(sysO)) ))
        s.setValue( "status", "")


    def tr(self, message):











        return QCoreApplication.translate('clsCaigosConnector', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):


        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_menu:
            self.iface.addPluginToDatabaseMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):


        icon_path = ':/plugins/CaigosConnector/m_icon.png'
        
        self.add_action(
            icon_path,
            text=self.tr(u'CAIGOS SQL Layer einbinden'),
            callback=self.EZU4B07243EE7524760AD9AFF93D330E846,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path,
            text=self.tr(u'CAIGOS SQL Datenbankverbindung anpassen'),
            callback=self.EZU54AB60ED8F1742F0AB1ED9921AEF0FEB,
            parent=self.iface.mainWindow())

        self.add_action(
            icon_path,
            text=self.tr(u'Onlinedokumentation'),
            callback=self.EZU700DA696BF2940D5A93583D248106E9E,
            parent=self.iface.mainWindow())
        
        self.add_action(
            icon_path,
            text=self.tr(u'Über das Programm'),
            callback=self.EZU8BD78EB47C554BA49C0622728DB4FA30,
            parent=self.iface.mainWindow())
            
    def unload(self):

        for action in self.actions:
            self.iface.removePluginDatabaseMenu(
                self.tr(u'&CAIGOS Datenprovider'),
                action)
         





        
    def EZU8BD78EB47C554BA49C0622728DB4FA30(self): 

        cls=uiAbout()
        cls.exec_()
    
    def EZU700DA696BF2940D5A93583D248106E9E(self): 

        webbrowser.open_new_tab("https://www.makobo.de/links/Dokumentation_CaigosConnector.php?id=" + EZU11DE7CED39F2439E803B738E6E678716())

    def EZU4B07243EE7524760AD9AFF93D330E846(self):
        EZU0BAA4CE0798E48099454390EF2BC83A4()
        EZU275D7392321740A3AA8EFCD92E2B011B()
        User = '000'
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
        else:
            db=None
           

        
        cls=uiExplorer()

        if db :
            qry = db.EZUDCF0989FCCB948B08C56317AE7037619(EZU97DD9229963D4C40BC10157CE31052F0())
            projekt=EZU0239CDC0875B4C7B837227F9004BC5D0()

            cls.EZUCC7E8BA81F14493981479906904576A7(db.EZUDCF0989FCCB948B08C56317AE7037619(EZUF218A9CE2308409D9617A675D4D9DC80()))

            guiListe, bGenDar, bPrjNeu, iGruppe, b3DDar, bDBTab, intExport, bLeer, intObjKlasse, bDarObjKl, intKeyTab = cls.EZU3B1BBFAC47624AEF82118DE7647883DE(projekt, qry)
            if guiListe:
                InStr = "','".join(guiListe)
                InStr = "'" + InStr + "'"
                qry = db.EZUDCF0989FCCB948B08C56317AE7037619(EZU97DD9229963D4C40BC10157CE31052F0(InStr,'DESC'))
                if not qry: print(db.EZU03F45B01171E465F835613DBEE097689())
                pri_gisdb = db.EZUDCF0989FCCB948B08C56317AE7037619(EZU8738A84187454718A9979A2226387046(User,InStr))
                if not pri_gisdb: print(db.EZU03F45B01171E465F835613DBEE097689())


                c = clsQGISAction()
                c.EZU9569D8F0E36C44ACB766DB0A73364BC3(db,User,projekt,pri_gisdb,qry, bGenDar, bPrjNeu,iGruppe, b3DDar, bDBTab, intExport, bLeer, intObjKlasse, bDarObjKl, intKeyTab)


        else:  
            if bMSQLFehlt:
                s = "Die MSSQL-Abfragen wurden nicht (vollständig) generiert"
            else:
                s = "Fehler beim Datenbankanbindung"
            reply = QMessageBox.question(None, s,"Soll der Dialog \n'CAIGOS Datenbankverbindung anpassen'\naufgerufen werden", QMessageBox.Yes |  QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.EZU54AB60ED8F1742F0AB1ED9921AEF0FEB()


    def EZU54AB60ED8F1742F0AB1ED9921AEF0FEB(self):
        cls=uiDBAnbindung()
        cls.exec_()    
  
  













