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
except:
    from PyQt4 import QtGui, uic
    from PyQt4.QtCore import  QDir
    from PyQt4.QtGui  import QDialog

try:
    from fnc4all import *
    from fnc4CaigosConnector import *
except:
    from .fnc4all import *
    from .fnc4CaigosConnector import *

d = os.path.dirname(__file__)
QDir.addSearchPath( "CaigosConnector", d )
uiAboutBase = uic.loadUiType( os.path.join( d, 'uiAbout.ui' ) )[0]

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'uiAbout.ui'))
   

class uiAbout(QDialog, FORM_CLASS):
    def __init__(self, parent=None):

        super(uiAbout, self).__init__(parent)





        self.setupUi(self)

        s=self.lblLink.text()
        s=s.replace("$$Homepage$$","https://www.makobo.de/links/Home_CaigosConnector.php?id=" + EZU11DE7CED39F2439E803B738E6E678716())
        s=s.replace("$$Daten$$","https://www.makobo.de/links/Daten_CaigosConnector.php?id=" + EZU11DE7CED39F2439E803B738E6E678716())
        s=s.replace("$$Forum$$","https://www.makobo.de/links/Forum_CaigosConnector.php?id=" + EZU11DE7CED39F2439E803B738E6E678716())
        s=s.replace("$$Doku$$","https://www.makobo.de/links/Dokumentation_CaigosConnector.php?id=" + EZU11DE7CED39F2439E803B738E6E678716())
        self.lblLink.setText(s)
  
