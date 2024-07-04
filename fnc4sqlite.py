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





import sqlite3 as sl
import shutil
import os.path
from datetime import datetime

try:
    from fnc4all import *
    from fnc4CaigosConnector import *
except:
    from .fnc4all import *
    from .fnc4CaigosConnector import *
    
def EZU32315C76E6A04BD1B46E5CB2DE026E79(dbName, sSQL, byURI):
    try:
        con = sl.connect(dbName, uri=byURI)
        con.row_factory = sl.Row 

        cur = con.cursor()    
        cur.execute(sSQL)
        return cur.fetchall()

    except:
        EZU2CC2ED60E16A4317BA8BEBE4D6120301 ()


    finally:   
        if con:
            con.close()
def EZU0D7899E839A5452EA745118B43BC46E3 (sQuelle, sZiel):








    if not os.path.isfile(sQuelle):
        return False
    
    
    if os.path.isfile(sZiel):
        os.remove(sZiel)
    if os.path.isfile(sZiel + '.meta'):
        os.remove(sZiel + '.meta')
        
    if os.path.isfile(sZiel + '-wal'):
        os.remove(sZiel + '-wal')
    if os.path.isfile(sQuelle + '-wal'):
        shutil.copyfile(sQuelle + '-wal', sZiel + '-wal')

    if os.path.isfile(sZiel + '-shm'):
        os.remove(sZiel + '-shm')
    if os.path.isfile(sQuelle + '-shm'):
        shutil.copyfile(sQuelle + '-shm', sZiel + '-shm')      
    
    if os.path.isfile(sQuelle):
        shutil.copyfile(sQuelle, sZiel)
        EZU2949ABF9619F4BBAB9A00B54887EF428 (sQuelle, sZiel + '.meta')
    return True

def EZU2949ABF9619F4BBAB9A00B54887EF428 (sQuelle, sZielMetaDat):
    now = datetime.datetime.now()
    oDat = open(sZielMetaDat,'w')
    dt_string = now.strftime("%d.%m.%Y %H:%M:%S")
    oDat.write(EZU3186DBC2C1074DC7A251155BCDCCC0A1(sQuelle) + '|' + dt_string)
    oDat.close()

def EZU031BEC08077544EEB1B60AD776DF6A77 (sZielMetaDat):
    try:
        oDat = open(sZielMetaDat,'r')
        data = oDat.readlines()[0].split('|')
        oDat.close()

        return EZU3186DBC2C1074DC7A251155BCDCCC0A1(data[0].strip()),data[1].strip()
    except:
        return '#LEER#',''
    
def EZUDE54B9C460DD4EE199CA6B2F9CAE4144 (dbName):
    return os.path.isfile(dbName + '-wal')
    
def EZUAA2C88E3693A4E14B6D07A46386BBB1E (dbName, byURI):

    try:
        con = sl.connect(dbName, uri=byURI)
        cur = con.cursor()    
        con.execute('pragma journal_mode=delete')
        return True

    except:
        EZU2CC2ED60E16A4317BA8BEBE4D6120301 ()


    finally:   
        if con:
            con.close()
def EZU3186DBC2C1074DC7A251155BCDCCC0A1(Pfad):
    if not Pfad:
        return '#None#'
    sPfad = os.path.normpath(Pfad)
    if os.name == 'nt':
        sPfad = sPfad.upper()
    return sPfad

def EZU1530D0D3A4E04F2D931FB43613DB642F():
    tmp=EZUE2CC6C01835941909C82368EAB1CE1E2() + "adm/"
    if not os.path.exists(tmp):
        os.makedirs(tmp) 
    if os.path.exists(tmp):
        return tmp + 'dbdesign.db' 
    else:
        QMessageBox.critical(None,tr("Program termination"), tr("Temporary directory\n%s\ncan not be created")%tmp)
        return None

    











































































