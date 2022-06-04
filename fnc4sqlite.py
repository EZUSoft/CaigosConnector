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
try:
    from fnc4all import *
    from fnc4CaigosConnector import *
except:
    from .fnc4all import *
    from .fnc4CaigosConnector import *
    
def EZU32315C76E6A04BD1B46E5CB2DE026E79(dbName,sSQL):
    try:
        con = sl.connect(dbName)
        con.row_factory = sl.Row 

        cur = con.cursor()    
        cur.execute(sSQL)
        return cur.fetchall()

    except:
        EZU2CC2ED60E16A4317BA8BEBE4D6120301 ()

    finally:   
        if con:
            con.close()
if __name__ == "__main__":
    sSQL = ('SELECT DBPROJECT_PRJNAME AS prjName, DBCONNECT_SERVERNAME AS pgServer, DBCONNECT_DATABASENAME AS pgDatabase, DBCONNECT_USERNAME AS pgUserName, DBCONNECT_PASSWORD AS pgPasswd '
       'FROM DBPROJECT '
       'INNER JOIN DBCONNECT ON DBPROJECT.DBPROJECT_IDDBCONNECT = DBCONNECT.DBCONNECT_ID WHERE lower([DBCONNECT_PACTORTYPE])="postgresql";')
    dbName='X:\CAIGOS_HOME\CAIGOS_Server\dbdesign.cgbin'
    rs = EZU32315C76E6A04BD1B46E5CB2DE026E79(dbName,sSQL)










