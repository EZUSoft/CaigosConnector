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







import re
try:
    from fnc4all import *


except:
    from .fnc4all import *


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
        sVersion = "2016-2020"
    return u"CAIGOS Importer für Version " + sVersion + "   (PlugIn Version " + EZU5067C1BD7E924D33B7D7B27226119B84() + ")" + sStatus
    
if __name__ == "__main__": 

    pass




