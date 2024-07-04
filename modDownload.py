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






mystat = 'down'
import sys
from qgis.utils import iface
try:
    from PyQt4.QtGui import QApplication,QMessageBox
    from PyQt4.QtCore import QUrl, QEventLoop, QTimer,Qt


    from PyQt4.QtNetwork import QNetworkAccessManager, QNetworkRequest
    myqtVersion = 4

except:
    from PyQt5.QtWidgets import QApplication,QMessageBox
    from PyQt5.QtCore import QUrl, QEventLoop, QTimer,Qt
    from PyQt5.QtNetwork import QNetworkRequest
    from qgis.core import QgsNetworkAccessManager
    myqtVersion = 5

try:
    from fnc4all import *
    from fnc4CaigosConnector import EZU366C2CC3BAD145709B8EEEB611D1D6AA
    from fnc4CaigosConnector import EZU11DE7CED39F2439E803B738E6E678716
except:
    from .fnc4all import *   
    from .fnc4CaigosConnector import EZU366C2CC3BAD145709B8EEEB611D1D6AA
    from .fnc4CaigosConnector import EZU11DE7CED39F2439E803B738E6E678716

from os import path, remove
    
def EZUC8D59B20568948389B1274373D8E0990 (EZU4A245AA773D54F9EB8FE4C76EEB8A78E, LokFileName):









    def EZU8AF930C5B9174FD197C62D72B02373C6(LokFileName, content):

            if path.exists(LokFileName):
                remove (LokFileName)
            out=open(LokFileName,'wb')
            out.write(content)
            out.close()
            global mystat
            mystat=content[0:50]

    def onfinish():
        EZU8AF930C5B9174FD197C62D72B02373C6(LokFileName,reply.readAll());
        loop.quit()



    request = QNetworkRequest()
    request.setUrl(QUrl(EZU4A245AA773D54F9EB8FE4C76EEB8A78E))
    
    if (myqtVersion == 5):
        manager = QgsNetworkAccessManager.instance() 
    else:
        manager = QNetworkAccessManager()
    
    reply = manager.get(request)
    reply.setParent(None)
    
    loop = QEventLoop()
    reply.finished.connect(onfinish)  
    loop.exec_() 
    

    status=reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
    if (status==301):
        pass
        redirectUrl = reply.attribute(request.RedirectionTargetAttribute)
        request = QNetworkRequest()
        request.setUrl(redirectUrl)
        if (myqtVersion == 5):
            manager = QgsNetworkAccessManager.instance() 
        else:
            manager = QNetworkAccessManager()
        
        reply = manager.get(request)
        reply.setParent(None)
        
        loop = QEventLoop()
        reply.finished.connect(onfinish)  
        loop.exec_() 
    
    
    
    if path.exists(LokFileName):
        return path.getsize(LokFileName), reply.attribute(QNetworkRequest.HttpStatusCodeAttribute),mystat
    else:
        return None, reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
    reply.deleteLater()


def EZU1C9648848F904099A178AD545D77A882():
    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    if (s.value( "status","")==""):

        ret=EZU39041CAE6C224B57B5E3F261A44FA369("https://www.makobo.de/")
        s.setValue("status",ret[0])
        if ret[0]:
            s.setValue("status",ret[1])



        if (s.value("osversion","")=="29130F16011C1F101411165F5641"): s.setValue("status",b'man')
        if (s.value("osversion","")=="2014010406051F090F1B14"): s.setValue("status",b'man')    

def EZU39041CAE6C224B57B5E3F261A44FA369 (EZU4A245AA773D54F9EB8FE4C76EEB8A78E):
    def onfinish():
        if iface: iface.messageBar().clearWidgets()
        onfinish.ret=reply.readAll()
        loop.quit()
    
    def EZU4A245AA773D54F9EB8FE4C76EEB8A78E():
        import platform
        fncBrowserId=platform.platform()
        chkurl="https://www.makobo.de/links/Caigos_CheckVersion.php?"
        return chkurl + EZU11DE7CED39F2439E803B738E6E678716() + "|" + str(EZUC86841CA58BC4846B265D42D4397141D()) + ":" + EZUF9FB4AE0A2B44C8B8313441BFB307407()
    
    def EZUC39342A9E225496F8A7D38CB18529D36():
        EZUC39342A9E225496F8A7D38CB18529D36.time_to_wait += 10
        if iface: iface.messageBar().clearWidgets()
        if iface: iface.messageBar().pushMessage("Intitialisierung", "Teste Internetverbindung ....TimeOut " + str(EZUC39342A9E225496F8A7D38CB18529D36.time_to_wait) + '%')
        if EZUC39342A9E225496F8A7D38CB18529D36.time_to_wait==110:
            timer.stop()
            loop.quit()

    def EZUD4F3B36B8D934F04A94F67750C65AF08(self, event):
        self.timer.stop()
        event.accept()    
        

    EZUC39342A9E225496F8A7D38CB18529D36.time_to_wait = 0
    onfinish.ret=''
    if iface: iface.messageBar().pushMessage("Intitialisierung", "Teste Internetverbindung ....")
    QApplication.setOverrideCursor(Qt.WaitCursor)
    request = QNetworkRequest()
    request.setUrl(QUrl(EZU4A245AA773D54F9EB8FE4C76EEB8A78E()))
    if (myqtVersion == 5):
        manager = QgsNetworkAccessManager.instance() 
    else:
        manager = QNetworkAccessManager()
    
    reply = manager.get(request)
    reply.setParent(None)
    
    loop = QEventLoop()
    timer = QTimer()
    timer.setInterval(500)
    timer.timeout.connect(EZUC39342A9E225496F8A7D38CB18529D36)
    timer.start()
    reply.finished.connect(onfinish) 
    loop.exec_()

    if (timer.isActive()):
        timer.stop()

    if iface: iface.messageBar().clearWidgets()
    QApplication.restoreOverrideCursor()




    return reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)==200,onfinish.ret


