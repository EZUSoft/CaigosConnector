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
from qgis.utils import os, sys
from itertools import cycle

     
try:
    from PyQt5 import QtGui
    from PyQt5.QtCore import QSettings
    from PyQt5.QtWidgets import QApplication,QMessageBox
    from configparser import ConfigParser
    
    def EZUC86841CA58BC4846B265D42D4397141D():
        return Qgis.QGIS_VERSION_INT
    myqtVersion = 5


except:
    from PyQt4 import QtGui
    from PyQt4.QtCore import QSettings
    from PyQt4.QtGui import QMessageBox,QApplication
    from ConfigParser import ConfigParser
    
    def EZUC86841CA58BC4846B265D42D4397141D():
        return QGis.QGIS_VERSION_INT
    myqtVersion = 4


try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = type(str)
    
    
import re
import time 
import os
import getpass
import traceback
import tempfile
import codecs
from glob import glob



def EZUA7F0526153984F32B32657FEE7904ECD (FullNode, Start = None):
    if Start is None: Start=QgsProject.instance().layerTreeRoot()
    if type(FullNode) == type([]):
        sNode=FullNode
    else:
        sNode=FullNode.split("\t")
    Gefunden=None
    for node in Start.children():
        if str(type(node))  == "<class 'qgis._core.QgsLayerTreeGroup'>":
            if node.name() == sNode[0]:
                if len(sNode) > 1:
                    Gefunden = EZUA7F0526153984F32B32657FEE7904ECD(sNode[1:], node)
                else:
                    Gefunden = node
    return Gefunden             


def EZU02B97863D0C3442985D82A8D462A6AE1 (FullNode, Start = None):



    ToDo=0
    if Start is None: Start=QgsProject.instance().layerTreeRoot()
    if type(FullNode) == type([]):
        sNode=FullNode
    else:
        sNode=FullNode.split("\t")
    Found=False
    for node in Start.children():
        if str(type(node))  == "<class 'qgis._core.QgsLayerTreeGroup'>":
            if node.name() == sNode[0]: 
                Found=True
                break
    if not Found: node=Start.addGroup(sNode[0]);ToDo=ToDo+1
    if len(sNode) > 1:
        node, ReToDo = EZU02B97863D0C3442985D82A8D462A6AE1 (sNode[1:],node)
        ToDo=ToDo+ReToDo
    return node, ToDo

def EZUFF9716E6E37C4D918ABCC8056B2F036E (FullNode, Start = None):
    if Start is None: Start=QgsProject.instance().layerTreeRoot()
    if type(FullNode) == type([]):
        sNode=FullNode
    else:
        sNode=FullNode.split("\t")
    delNodeName=sNode[-1:][0]
    if len(sNode) > 1:
        parent=EZUA7F0526153984F32B32657FEE7904ECD (sNode[:-1],Start)
    else:
        parent=Start
    if not parent: return False
    for node in parent.children():
        if str(type(node))  == "<class 'qgis._core.QgsLayerTreeGroup'>":
            if node.name() == delNodeName:
                parent.removeChildNode(node)
                return True


def EZUC936D29251B44D4E994497BF023338C7(text):





    if myqtVersion == 4 and type(text) == QString:
        return unicode(text)
    if (type(text) == str and sys.version[0] == "2"):
        return text.decode("utf8")
    else:
        return text
    
glFehlerListe=[]
glHinweisListe=[]
def EZUC8DCB02F1A8145AF82C8A69A43E0529B (Fehler): 
    glFehlerListe.append (EZUC936D29251B44D4E994497BF023338C7(Fehler))
def EZU03F45B01171E465F835613DBEE097689() :
    return glFehlerListe
def EZU0BAA4CE0798E48099454390EF2BC83A4() :
    global glFehlerListe
    glFehlerListe = []  
def EZU9AC841489FAD40E4B1A1232B3CA9B315 (Hinweis):
    glHinweisListe.append (EZUC936D29251B44D4E994497BF023338C7(Hinweis))
def EZUC4078FFEC92741969D3834F8CE89E164() :
    try:
        return u"\n".join(glHinweisListe)
    except:
        return "\n".join(glHinweisListe)

def EZU9D0157F9BB984DE991CEB81C700FA02B() :
    return glHinweisListe
def EZU275D7392321740A3AA8EFCD92E2B011B() :
    global glHinweisListe
    glHinweisListe = [] 

def EZUF9FB4AE0A2B44C8B8313441BFB307407():
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__),'metadata.txt'))



    return config.get('general', 'version')
    









def cut4view (fulltext,zeichen=1500,zeilen=15,anhang='\n\n                  ............. and many more .........\n'):
    try:
        cut = False
        ctext=fulltext
        if len(fulltext) > zeichen:
            cut=True
            ctext=ctext[:zeichen]
        
        arr=ctext.split('\n')
        if len(arr) > zeilen:
            cut = True
            ctext= '\n'.join(arr[:zeilen])
        if cut:
            ctext=ctext + anhang
        return ctext
    except:
        EZU2CC2ED60E16A4317BA8BEBE4D6120301 ()
        return '#FEHLER#cut4view'
def errbox (text, Quelle=''):
    su= EZUC936D29251B44D4E994497BF023338C7(text)

    try:
        QMessageBox.critical(None, Quelle + "PlugIn Error: ", cut4view(su))
        QgsMessageLog.logMessage( su, u'EZUSoft:Error' )
    except:
        QgsMessageLog.logMessage( '#Fehler errbox#', u'EZUSoft:Hinweise' )
        print("FEHLER:",text)        



def msgbox (text):
    su= EZUC936D29251B44D4E994497BF023338C7(text)
    try:
        QMessageBox.information(None, "PlugIn Hinweis", cut4view(su))
        QgsMessageLog.logMessage( su, u'EZUSoft:Hinweise' )
    except:
        QgsMessageLog.logMessage( '#Fehler Textanzeige#', u'EZUSoft:Hinweise' )



def errlog(text, DebugMode = False):
    su= EZUC936D29251B44D4E994497BF023338C7(text)   
    if DebugMode:
        QMessageBox.information(None, "DEBUG:", su)
    
    try:
        QgsMessageLog.logMessage( su, u'EZUSoft:Fehler' )
    except:
        pass
        pass

def EZU7134CD8D717449148C4836EBEB211A29(All=None):
    Feh=0
    Loe=0
    tmp=EZUE2CC6C01835941909C82368EAB1CE1E2()
    if All:
        for dat in glob(tmp +'*.*'):
            try:
                os.remove(dat)
                Loe+=1
            except:
                Feh+=1
    else:
        for shp in glob(tmp +'*.shp'):
            try:
                os.remove(shp)
                Loe+=1
                for rest in glob(shp[0:-4] + '.*'):
                    os.remove(rest)
                    Loe+=1
            except:
                Feh+=1
                
    return Loe, Feh

def EZU1FCD98CB63A64E32A30A1F171BE370F3 (wert):
    if wert==None:
        return ("#undef#")
    else:
        return (wert)
        
def EZUE2CC6C01835941909C82368EAB1CE1E2():

    tmp=(tempfile.gettempdir()).replace("\\","/") + "/{D5E6A1F8-392F-4241-A0BD-5CED09CFABC7}/"
    if not os.path.exists(tmp):
        os.makedirs(tmp) 
    if os.path.exists(tmp):
        return tmp
    else:
        QMessageBox.critical(None,tr("Program termination"), tr("Temporary directory\n%s\ncan not be created")%tmp)
        return None

def debuglog(text,DebugMode=False):
    if DebugMode:
        su= EZUC936D29251B44D4E994497BF023338C7(text)   
        try:
            QgsMessageLog.logMessage( su, 'EZUSoft:Debug' )
        except:
            pass

def hinweislog(text,p=None):
        su= EZUC936D29251B44D4E994497BF023338C7(text)   
        try:
            QgsMessageLog.logMessage( su, 'Comments' )
        except:
            pass
    
def printlog(text,p=None):
    su= EZUC936D29251B44D4E994497BF023338C7(text)        
    try:
        print ("log1",su)
    except:
        try:
            print ("log2",su.encode("utf-8"))
        except:
            print ("log3",tr("printlog:Tip can not view"))

def EZUF0AF6D30C6EB4BE8A558B27DA05DBD21 (OrgName,Ersatz="_"):
    NeuTex=""
    for i in range(len(OrgName)):
        if re.search("[/\\\[\]:*?|!=]",OrgName[i]):
            NeuTex=NeuTex+Ersatz
        else:
            NeuTex=NeuTex+OrgName[i]
    return NeuTex      
    
def EZUD387D432776647B8BC2C8B379B01E3C1():
    lt = time.localtime()
    return ("%02i%02i%02i") % (lt[0:3])  

def EZU6F6315D895BC410ABCE5C02C6E0C5F14(message, key=None):
    if key==None:
        key=EZUD387D432776647B8BC2C8B379B01E3C1()
    return  ''.join(("%0.1X" % (ord(c)^ord(k))).zfill(2) for c,k in zip(message, cycle(key)))


def EZUEAA9C2F7A165491B918953D7518D8009(uText):
    try:
        for char in uText:
            if(ord(char))> 128:
              return False   
        return True
    except:
        return False 
    
def EZU9A25B96EF34E432F8B39C40EA0D860A6(uText):








    try:
        a=""
        for char in uText:
            a= a + chr(ord(char))
        return a.decode("utf8")
    except:
        return uText    
        
def EZUEAEC23599FD84BC88D09503D1DC0F1D2(txt,sCharset):
    if myqtVersion == 5: 
        try:
            return str(bytes(txt,"utf8").decode(sCharset) )
        except:
            return txt
    try:
        re=txt.decode( sCharset) 
        return re
    except:
        return '#decodeerror4#'    

def EZU0937D041C39145ACBD91A5117C5C6F09(Verz):
    for dat in glob(Verz +'*.*'):
        try:
            os.remove(dat)
        except:
            return False
    return True
    
def EZUE7D17250C3C7421C9D8813540A672DFC (OrgName):
    v=OrgName.replace("\\","/")
    return v.replace("//","/")

def EZUAC460E6F0D4B49ABBAC60E8D53FD6A34(tmpDat, qlrDat, PathAbsolute):


        subPath=EZUE7D17250C3C7421C9D8813540A672DFC(PathAbsolute + "/") 
        iDatNum = open(tmpDat)
        oDatNum = open(qlrDat,"w")
        for iZeile in iDatNum:
            s1=iZeile.replace('source="' + subPath,'source="./') 
            s1=s1.replace('k="name" v="' + subPath,'k="name" v="./') 
            s1=s1.replace('<datasource>' + subPath,'<datasource>./') 
            oDatNum.write(s1)
        iDatNum.close()
        oDatNum.close()
        os.remove(tmpDat)

def EZU94C6C3886ADC4AC4818CDC56A88AEC89(DatName,sEncode):




    if myqtVersion == 5:
        tmp = open(DatName, "r", encoding=sEncode)
    else:
        tmp = open(DatName, "r")
    tmpArray =tmp.readlines()
    tmp.close()
    return tmpArray

def EZU71B6BE8C89A64C1E952E8EBE887EF2FF(DatName, Art, zArray,sEncode):




    if myqtVersion == 5:
        tmp = open(DatName, Art, encoding=sEncode)
    else:
        tmp = open(DatName, Art)
    tmp.writelines(zArray)
    tmp.close()
    
def EZUA4368C0FEFDC4FC1977350D9EDFD8729 (DatName, Art, sEncode):
    if myqtVersion == 5:
        tmp = open(DatName, Art, encoding=sEncode)
    else:
        tmp = open(DatName, Art)
    return tmp
        
