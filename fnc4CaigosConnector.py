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







import re, os, datetime
try:
    from PyQt5.QtNetwork import QNetworkRequest
    from qgis.core import QgsNetworkAccessManager
    from PyQt5.QtCore import QUrl, QEventLoop, QTimer,Qt
except:
    from PyQt4.QtNetwork import QNetworkAccessManager, QNetworkRequest
    from PyQt4.QtCore import QUrl, QEventLoop, QTimer,Qt
try:
    from fnc4all import *

except:
    from .fnc4all import *

from os import path, remove
def EZU4F19AB03FE56453BBF806D186556FE91 (EZU4A245AA773D54F9EB8FE4C76EEB8A78E, LokFileName):









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

def EZU2CC2ED60E16A4317BA8BEBE4D6120301(Sonstiges = None, bOnline=True):


    dummy= 'https://www.makobo.de/links/Caigos_Fehler.php?'
    try:
        QgsMessageLog.logMessage( traceback.format_exc().replace("\n",chr(9))+ (chr(9) + Sonstiges if Sonstiges else ""), u'EZUSoft:Error' )
        print ("LZF:" + traceback.format_exc().replace("\n",chr(9)) + (chr(9) + Sonstiges if Sonstiges else ""))
    except:
        pass

    try:
        if bOnline:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            tb_lineno=exc_tb.tb_lineno
            sFehler = fname +'$' + str(tb_lineno) + '$' + str(exc_obj) + ('$' + Sonstiges if Sonstiges else '')
            sFehler=sFehler.replace(" ",'_')
            
            check= dummy  + EZU11DE7CED39F2439E803B738E6E678716() + "|" + str(EZUC86841CA58BC4846B265D42D4397141D()) + ":" + EZUF9FB4AE0A2B44C8B8313441BFB307407() + ":" + sFehler
            EZU4F19AB03FE56453BBF806D186556FE91(check,EZUE2CC6C01835941909C82368EAB1CE1E2()+'test.zip')
    except:
        pass
    EZUC8DCB02F1A8145AF82C8A69A43E0529B ("LZF:" + traceback.format_exc().replace("\n",chr(9)) + (chr(9) + Sonstiges if Sonstiges else ""))   

def EZU765F003A443242CFAC8F3F367CC94165 (sSQL):
    s=sSQL.replace("||","+")
    s=s.replace('!=','<>')
    s=re.sub('cast(\((.*?)\))', '\'XXX\'',s) 
    return s
    
def EZU3311744BFDFB478CBE981B15F33460B0 (sSQL):
    s=sSQL.replace("||","+")
    return s

def EZUC7AA96B394624996A75241F4F6A0A0C2 (sSQL):
    s=sSQL.replace("TOP 100 PERCENT","")
    return s    
    
    
def EZU50464908A0F8417AA7B9045C4E9B1F6A():


    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    try:
        return int(s.value( "cgserverart"))
    except:
        return 0

def EZU51B3FDFA62764BDA9B7CED2681A70937():


    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    try:
        if int(s.value( "cgserverart")) == 0: return ("Postgres")
        if int(s.value( "cgserverart")) == 1: return ("MSSQL")
        if int(s.value( "cgserverart")) == 2: return ("ORACLE")
    except:
        return ("Postgres")
        
def EZU366C2CC3BAD145709B8EEEB611D1D6AA():
    return "CAIGOS-Konnektor" + str(myqtVersion)
    
def EZU5067C1BD7E924D33B7D7B27226119B84():
    return "V " + EZUF9FB4AE0A2B44C8B8313441BFB307407()
    
def EZUDDCC484E3DC3474889FE69ED76A61E8F(): 
    if (os.path.exists(os.path.dirname(__file__) + '/00-debug.txt')): 
        return True
    else:
        return False
    
def EZU11DE7CED39F2439E803B738E6E678716():
    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    s.setValue( "-id-", EZU6F6315D895BC410ABCE5C02C6E0C5F14((EZU366C2CC3BAD145709B8EEEB611D1D6AA() + "ID=%02i%02i%02i%02i%02i%02i") % (time.localtime()[0:6])) )
    return s.value( "–id–", "" ) 
    
def tr( message):
    return message  
 
    
def EZUAC62A428AD734562A807B0FF8D792A61(intCG = None,sStatus = None):
    s = QSettings( "EZUSoft", EZU366C2CC3BAD145709B8EEEB611D1D6AA() )
    sVersion = "-"
    if not sStatus:
        sStatus = " - Onlineversion"
        if (s.value( "status","")==''):
            sStatus = " - Offlineversion"   
        else:
            if (s.value( "status","")==b'man'):
                sStatus = " - Lizenzversion" 
            else:
                if (s.value( "status","")!=b'ok'):
                    sStatus = " - Demoversion"
    if not intCG :
        intCG = int(s.value( "cgversion",-1))
    if intCG == 0:
        sVersion = "11.2"
    if intCG == 1:        
        sVersion = "16-19.2"
    if intCG == 2:        
        sVersion = "19.3"
    return u"CAIGOS Importer für Version " + sVersion + "   (PlugIn Version " + EZU5067C1BD7E924D33B7D7B27226119B84() + ")" + sStatus



def EZU6703A5CA606B48D3823A591742FCA367(fname):







    try:
        import win32api
    except:
        return None
    propNames = ('Comments', 'InternalName', 'ProductName',
        'CompanyName', 'LegalCopyright', 'ProductVersion',
        'FileDescription', 'LegalTrademarks', 'PrivateBuild',
        'FileVersion', 'OriginalFilename', 'SpecialBuild')

    props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}

    try:

        fixedInfo = win32api.GetFileVersionInfo(fname, '\\')
        props['FixedFileInfo'] = fixedInfo
        props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536,
                fixedInfo['FileVersionMS'] % 65536, fixedInfo['FileVersionLS'] / 65536,
                fixedInfo['FileVersionLS'] % 65536)



        lang, codepage = win32api.GetFileVersionInfo(fname, '\\VarFileInfo\\Translation')[0]




        strInfo = {}
        for propName in propNames:
            strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)

            strInfo[propName] = win32api.GetFileVersionInfo(fname, strInfoPath)

        props['StringFileInfo'] = strInfo
    except:
        EZU2CC2ED60E16A4317BA8BEBE4D6120301()

    return props  
    
def EZU7E0D638197C34356A2E45006516F0C4F (servEXE):
    try:
        sFileDate= datetime.datetime.fromtimestamp(float(os.path.getmtime(servEXE))).strftime("%Y%m%d")
        sV=EZU6703A5CA606B48D3823A591742FCA367(servEXE)
        if sV:
            sV=sV['StringFileInfo'][ 'FileVersion']
            ss = sV.split('.')
            return ss[0] + '.' + ss[1], sFileDate
        else:
            return 'API_FEHLER', sFileDate
    except:
        EZU2CC2ED60E16A4317BA8BEBE4D6120301()
        return 'FEHLER', sFileDate

