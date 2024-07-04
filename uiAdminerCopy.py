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
    from PyQt5.QtWidgets import QDialog
    from PyQt5.QtCore import Qt
except:
    from PyQt4 import QtGui, uic
    from PyQt4.QtCore import  QDir
    from PyQt4.QtGui  import QDialog

try:
    from fnc4all import *
    from fnc4CaigosConnector import *
    from fnc4sqlite import *
except:
    from .fnc4all import *
    from .fnc4CaigosConnector import *
    from .fnc4sqlite import *

d = os.path.dirname(__file__)
QDir.addSearchPath( "CaigosConnector", d )
uiAdminerCopyBase = uic.loadUiType( os.path.join( d, 'uiAdminerCopy.ui' ) )[0]

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'uiAdminerCopy.ui'))
   

class uiAdminerCopy(QDialog, FORM_CLASS):
    def __init__(self, admDat, parent=None):

        super(uiAdminerCopy, self).__init__(parent)






        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)


        self.setupUi(self)
        self.lbDB.setText(admDat)
        self.cmdAbbrechen.clicked.connect(self.EZU2AE65B9BF2234AB9B44DAA36BDDE4BB2)
        self.cmdKopieren.clicked.connect(self.EZUD6F0BD47726E4BECA56133297246EA0C)
        self.cmdVerwenden.clicked.connect(self.EZU02BF43C77AEC41EFB3AC6D5E747FE90E)
        

        sPath='#KEINE#'
        if os.path.isfile(EZU1530D0D3A4E04F2D931FB43613DB642F()): 
            sPath, sDate = EZU031BEC08077544EEB1B60AD776DF6A77 (EZU1530D0D3A4E04F2D931FB43613DB642F()  + '.meta' )

        if EZU3186DBC2C1074DC7A251155BCDCCC0A1(sPath) == EZU3186DBC2C1074DC7A251155BCDCCC0A1(admDat):
            self.lbLastKopie.setText(sDate)
        self.lbLastKopie.setVisible (EZU3186DBC2C1074DC7A251155BCDCCC0A1(sPath) == EZU3186DBC2C1074DC7A251155BCDCCC0A1(admDat))
        self.cmdVerwenden.setVisible (EZU3186DBC2C1074DC7A251155BCDCCC0A1(sPath) == EZU3186DBC2C1074DC7A251155BCDCCC0A1(admDat))
        
    def EZU2AE65B9BF2234AB9B44DAA36BDDE4BB2(self):
        self.lbDB.setText('#ABBRUCH#')
        self.close()
        
    def EZU02BF43C77AEC41EFB3AC6D5E747FE90E(self):
        self.lbDB.setText(EZU1530D0D3A4E04F2D931FB43613DB642F())
        self.close()
        
    def EZUD6F0BD47726E4BECA56133297246EA0C(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        liveDB=self.lbDB.text().strip()
        self.lbDB.setText('#Kopieren#')
        
        if EZU0D7899E839A5452EA745118B43BC46E3(liveDB,EZU1530D0D3A4E04F2D931FB43613DB642F()):
            if EZUAA2C88E3693A4E14B6D07A46386BBB1E(EZU1530D0D3A4E04F2D931FB43613DB642F(), False):
                self.lbDB.setText(EZU1530D0D3A4E04F2D931FB43613DB642F())
        QApplication.restoreOverrideCursor()
        self.close()
    
    def EZU5FD59B408C704253BE664AD8D5A06359(self):
        return self.lbDB.text().strip()









