# -*- coding: utf-8 -*-
"""
/***************************************************************************
 modCGSqlCodes: Gemeinsame Basis für QGIS2 und QGIS3
 
 A QGIS plugin
 CAIGOS-PostgreSQL/PostGIS in QGIS darstellen
                              -------------------
        begin                : 2016-04-18
        git sha              : $Format:%H$
        copyright            : (C) 2016 by EZUSoft
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
def GeoTabName4Art (Art):
    table=None
    if Art == 0: # Point      
        table="pointssqlspatial"
    if Art == 1: # Line
        table="linessqlspatial"
    if Art == 2: # Kreis
        table="arcssqlspatial"
    if Art == 3: # Text
        table="textssqlspatial"
    if Art == 31: # Referenzlinie
        table="textssqlspatial"
    if Art == 4: # Bemaßung
        table = None
    if Art == 5: # Polylinie
        table="segssqlspatial"
    if Art == 6: # Fläche
        table="polyssqlspatial"    
    return table

def sqlStruk4Layer( LayerID):
    sSQL = (u"SELECT dbname  as Fachschale, entityname as Thema, groupname as Gruppe, layername as Layer " # , layerid, layertyp "
                "FROM (enttable INNER JOIN grptable ON enttable.entityid = grptable.entityid) "
                "INNER JOIN lyrtable ON (grptable.groupid = lyrtable.groupid) AND (enttable.entityid = lyrtable.entityid) "
                "WHERE layerid='%s'") % (LayerID)
    return sSQL

def sqlStrukAlleLayer(LayerList = None, Richtung=''):
    sSQL=""
    if LayerList:
        sSQL = "WHERE layerid In ("
        sSQL = sSQL + LayerList
        sSQL = sSQL + ")"
    # Alphabetische Reihenfolge für Explorerbaum, dabei Layername DESC, da Einfügereihenfolge über moveLayer umgekeht
    sSQL = (u"SELECT dbname  as Fachschale, entityname as Thema, groupname as Gruppe, layername as layer, layerid, layertyp "
                "FROM (enttable INNER JOIN grptable ON enttable.entityid = grptable.entityid) "
                "INNER JOIN lyrtable ON (grptable.groupid = lyrtable.groupid) AND (enttable.entityid = lyrtable.entityid) "
                "%s order by dbname,entityname,groupname,layername %s") % (sSQL, Richtung)
    return sSQL
    
def sqlAlleLayerByPriAndGISDB(UserNum = '000', LayerList = None):
    sSQL=""
    if LayerList:
        if len(LayerList.split(",")) == 1:
            sSQL =   "AND lyrtable.layerid = " + LayerList     
        else:
            sSQL = "AND lyrtable.layerid In ("
            sSQL = sSQL + LayerList
            sSQL = sSQL + ")"
    # Ebenen nach Prioritäten sortiert
    sSQL = (u"SELECT layername, lyrtable.layerid, lyrtable.layertyp, dbname, priority "
                "FROM prptable INNER JOIN lyrtable ON prptable.layerid = lyrtable.layerid LEFT JOIN frametbltable on lyrtable.tblid = frametbltable.ft_id "
                "WHERE usernr='%s' %s "
                "UNION ALL "
                ""
                "select DISTINCT  layername,T1.layerid, layertyp,  dbname, priority from  ( "
                "SELECT layername || '(RL)' as layername, lyrtable.layerid, 31 as layertyp, ''::text as  dbname, priority FROM prptable INNER JOIN lyrtable ON prptable.layerid = lyrtable.layerid "
                "LEFT JOIN frametbltable on lyrtable.tblid = frametbltable.ft_id WHERE usernr='%s' AND lyrtable.layertyp=3 %s "
                " \n") % (UserNum,sSQL,UserNum, sSQL) # 23.08.16 zusätzlich nach Layertyp (damit bei gleicher Pri Punkte über Flächen liegen)
    
    sSQL = sSQL + ") as T1 inner join "
    sSQL = sSQL + "(SELECT layerid FROM  ( SELECT * FROM (" + sqlAtt4Massstab ( 3,None, UserNum) + ") AS dummy "
    sSQL = sSQL + ("INNER JOIN textatttable ON dummy.ATTid = textatttable.ta_idfa "
            "WHERE textatttable.ta_ag=0 and textatttable.lineattr != '{00000000-0000-0000-0000-000000000000}' ORDER BY attnum\n")
            
    sSQL = sSQL + (") AS t1 "
    "INNER JOIN "
    "  (SELECT DISTINCT textssqlspatial.defid, layerid "
    "   FROM textssqlspatial "
    "   LEFT JOIN deftable ON textssqlspatial.defid =deftable.defid "
    "   WHERE  textssqlspatial.defid != '{00000000-0000-0000-0000-000000000000}' "
    "   UNION ALL SELECT defid, layerid "
    "   FROM prptable "
    "   WHERE usernr='000') AS t2 ON t1.adid = t2.defid) as T2 on T1.layerid = T2.layerid "
    "   ORDER BY priority DESC,layertyp ")
    return sSQL

def sqlAllAttDef4Layer( Art, LayerID):
    # verwendete Objekt-Attributdefinitionen aus der Geometrietabelle holen
    TabName=GeoTabName4Art(Art)
    if TabName:
        return (u"SELECT DISTINCT %s.defid, COALESCE(defname, '        ') as sortdefname FROM %s LEFT JOIN deftable ON %s.defid =deftable.defid where layerid='%s' order by sortdefname") % (TabName,TabName,TabName,LayerID)
    else:
        return None
  
def sqlAtt4Massstab4All( Art, AktDef=None):
    # Art 31 (Referenzpfeil) wird hier auf Text(abfrage) zurückgesetzt
    # Attribute nach Maßstab - Grunddaten für alle Geometriearten gleich
    sFilt = "" if AktDef == None else " deftable.defid='" + AktDef + "' AND "
    sSQL=""
    for i in range(5):
        if i>0:
            sSQL=sSQL + "\nUNION ALL\n"
        sSQL = sSQL + (
"SELECT  %i AS AttNum, deftable.defid AS ADid, defname AS ADname,fa_id AS ATTid, attrname AS ATTname, scrscale%i AS MMin, scrscale%i AS mMax, scrresize "
"FROM deftable INNER JOIN frameatttable ON deftable.scrattrname%i = frameatttable.fa_id where " + sFilt + " attrtype=%i"
) % (i+1,i+1,i+2,i+1,3 if Art==31 else Art)

    return sSQL

def sqlAtt4Massstab ( Art, AktDef, Group):
    sSQL=sqlAtt4Massstab4All(Art,AktDef)      
    if Art == 0: # Point      
        sSQL="select * from (" + sSQL +") as dummy inner join pointatttable ON dummy.ATTid = pointatttable.pta_idfa where pointatttable.pta_ag=" + str(Group)  + " order by attnum"  
    if Art == 1: # Line
        sSQL=sSQL
    if Art == 2: # Kreis
        sSQL="select * from (" + sSQL +") as dummy inner join (select * from arcatttable where arcatttable.aa_ag=" + str(Group) + ") as arc ON dummy.ATTid = arc.aa_idfa  inner join polyatttable  ON arc.polyattr = polyatttable.poa_idfa where polyatttable.poa_ag=" + str(Group) + " order by attnum"  
        sSQL = sSQL
    if Art == 3 or Art == 31: # Text bzz Referenzlinie
       sSQL="select * from (" + sSQL +") as dummy inner join textatttable ON dummy.ATTid = textatttable.ta_idfa where textatttable.ta_ag=" + str(Group)  + " order by attnum"  
    if Art == 4: # Bemaßung
        sSQL = sSQL
    if Art == 5: # Polylinie
        sSQL="select * from (" + sSQL +") as dummy inner join segatttable  ON dummy.ATTid = segatttable.sa_idfa where segatttable.sa_ag=" + str(Group)  + " order by attnum"  
    if Art == 6: # Fläche
        sSQL="select * from (" + sSQL +") as dummy inner join polyatttable  ON dummy.ATTid = polyatttable.poa_idfa where polyatttable.poa_ag=" + str(Group) + " order by attnum"  
    return sSQL   

def sqlAttParam4IDandArt( Art, AktAttID, Group):
    sSQL=None
    if Art == 0: # Point      
        sSQL=("select * from  pointatttable  where pointatttable.pta_idfa = '%s' and  pointatttable.pta_ag=%d") % (AktAttID, Group)

    if Art == 1 or Art == 5: # Strecke, Polylinie
              #                      0                     1           2        3      4       5      6       7              8           9            10          11
        sSQL=("SELECT la_idfa AS st_attid, attrname AS st_attrname, la_linenr, used, color, sizemm, basemm, basecolor, linesigattr, linesigbegin,linesigofs, linesigofsline, "
               #           12            13            14            15          16           17          18       19          20          21          22           23
              "       lineoffset, sigbeginattr, sigmiddleattr, sigendattr, transparent, denyatpercent, penid, basepenid, sigbeginpos, sigendpos, sigmiddlepos, geocolor, "
               #           24
              "       scrresize, pentable.* "
              "FROM (frameatttable INNER JOIN lineatttable ON frameatttable.fa_id = lineatttable.la_idfa) "
              "INNER JOIN pentable ON lineatttable.penid =pentable.id "
              "WHERE la_idfa='%s' AND used='J' AND la_ag=%i order by la_linenr DESC") %(AktAttID, Group) # 22.08.16 Reihenfolge (testweise) umgedreht, damit Symbolde der Baseline zuletzt

    if Art == 2: # Kreis
        sSQL = None
    if Art == 3: # Text
        # nur noch für alte Version Rendering Wien 
              #          0        1       2         3        4       5        6       7      8
        sSQL=("SELECT defname, defid , attrname, lineattr, color, sizemm, fontname, bold, italic, "
              #             9         10          11        12         13             14         15        16       17       18        19       20
              "         underline, freestyle, textalign, frametext, framecolor, framewidthmm, bkcolor, lineattr, tabpos1, tabpos2, usememo, blattnord, "
              #             21          22             23               24            25       26
              "         oneline, charframetext, charframecolor, charframewidthmm, quality, ofsalign "
              "  FROM (textatttable INNER JOIN deftable ON textatttable.ta_idfa = deftable.scrattrname1) "
              "        INNER JOIN frameatttable ON textatttable.ta_idfa = frameatttable.fa_id "
              "  WHERE defid='%s' AND textatttable.ta_ag=%i;") % (AktAttID,Group)
        #sSQL=None # unused
    if Art == 4: # Bemaßung
        sSQL = None

    if Art == 6: # Fläche
        sSQL=None       
    return sSQL



