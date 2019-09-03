# -*- coding: utf-8 -*-
"""
/***************************************************************************
 A QGIS plugin
CaigosConnector: Connect CAIGOS-GIS with QGIS
        copyright            : (C) 2019 by EZUSoft
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






def EZUBB35FE2AD3BE43C0BED5E2BB71976827 (Art):
    table=None
    if Art == 0: 
        table="pointssqlspatial"
    if Art == 1: 
        table="linessqlspatial"
    if Art == 2: 
        table="arcssqlspatial"
    if Art == 3: 
        table="textssqlspatial"
    if Art == 31: 
        table="textssqlspatial"
    if Art == 4: 
        table = None
    if Art == 5: 
        table="segssqlspatial"
    if Art == 6: 
        table="polyssqlspatial"    
    return table

def EZU1B44A2C9E7584B0BAEB94E020A2B4139( LayerID):
    sSQL = (u"SELECT dbname  as Fachschale, entityname as Thema, groupname as Gruppe, layername as Layer " 
                "FROM (enttable INNER JOIN grptable ON enttable.entityid = grptable.entityid) "
                "INNER JOIN lyrtable ON (grptable.groupid = lyrtable.groupid) AND (enttable.entityid = lyrtable.entityid) "
                "WHERE layerid='%s'") % (LayerID)
    return sSQL

def EZU97DD9229963D4C40BC10157CE31052F0(LayerList = None, Richtung=''):
    sSQL=""
    if LayerList:
        sSQL = "WHERE layerid In ("
        sSQL = sSQL + LayerList
        sSQL = sSQL + ")"

    sSQL = (u"SELECT dbname  as Fachschale, entityname as Thema, groupname as Gruppe, layername as layer, layerid, layertyp "
                "FROM (enttable INNER JOIN grptable ON enttable.entityid = grptable.entityid) "
                "INNER JOIN lyrtable ON (grptable.groupid = lyrtable.groupid) AND (enttable.entityid = lyrtable.entityid) "
                "%s order by dbname,entityname,groupname,layername %s") % (sSQL, Richtung)
    return sSQL
    
def EZU8738A84187454718A9979A2226387046(UserNum = '000', LayerList = None):
    sSQL=""
    if LayerList:
        if len(LayerList.split(",")) == 1:
            sSQL =   "AND lyrtable.layerid = " + LayerList     
        else:
            sSQL = "AND lyrtable.layerid In ("
            sSQL = sSQL + LayerList
            sSQL = sSQL + ")"

    sSQL = (u"SELECT layername, lyrtable.layerid, lyrtable.layertyp, dbname, priority "
                "FROM prptable INNER JOIN lyrtable ON prptable.layerid = lyrtable.layerid LEFT JOIN frametbltable on lyrtable.tblid = frametbltable.ft_id "
                "WHERE usernr='%s' %s "
                "UNION ALL "
                ""
                "select DISTINCT  layername,T1.layerid, layertyp,  dbname, priority from  ( "
                "SELECT layername || '(RL)' as layername, lyrtable.layerid, 31 as layertyp, ''::text as  dbname, priority FROM prptable INNER JOIN lyrtable ON prptable.layerid = lyrtable.layerid "
                "LEFT JOIN frametbltable on lyrtable.tblid = frametbltable.ft_id WHERE usernr='%s' AND lyrtable.layertyp=3 %s "
                " \n") % (UserNum,sSQL,UserNum, sSQL) 
    
    sSQL = sSQL + ") as T1 inner join "
    sSQL = sSQL + "(SELECT layerid FROM  ( SELECT * FROM (" + EZUE46C97B18D5843DFB7668B8846F26976 ( 3,None, UserNum) + ") AS dummy "
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

def EZU64C9598DF0AB4FADA28872A43F622D0A( Art, LayerID):

    TabName=EZUBB35FE2AD3BE43C0BED5E2BB71976827(Art)
    if TabName:
        return (u"SELECT DISTINCT %s.defid, COALESCE(defname, '        ') as sortdefname FROM %s LEFT JOIN deftable ON %s.defid =deftable.defid where layerid='%s' order by sortdefname") % (TabName,TabName,TabName,LayerID)
    else:
        return None
  
def EZU08438317C6A34E64A6AAB7424525B78B( Art, AktDef=None):


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

def EZUE46C97B18D5843DFB7668B8846F26976 ( Art, AktDef, Group):
    sSQL=EZU08438317C6A34E64A6AAB7424525B78B(Art,AktDef)      
    if Art == 0: 
        sSQL="select * from (" + sSQL +") as dummy inner join pointatttable ON dummy.ATTid = pointatttable.pta_idfa where pointatttable.pta_ag=" + str(Group)  + " order by attnum"  
    if Art == 1: 
        sSQL=sSQL
    if Art == 2: 
        sSQL="select * from (" + sSQL +") as dummy inner join (select * from arcatttable where arcatttable.aa_ag=" + str(Group) + ") as arc ON dummy.ATTid = arc.aa_idfa  inner join polyatttable  ON arc.polyattr = polyatttable.poa_idfa where polyatttable.poa_ag=" + str(Group) + " order by attnum"  
        sSQL = sSQL
    if Art == 3 or Art == 31: 
       sSQL="select * from (" + sSQL +") as dummy inner join textatttable ON dummy.ATTid = textatttable.ta_idfa where textatttable.ta_ag=" + str(Group)  + " order by attnum"  
    if Art == 4: 
        sSQL = sSQL
    if Art == 5: 
        sSQL="select * from (" + sSQL +") as dummy inner join segatttable  ON dummy.ATTid = segatttable.sa_idfa where segatttable.sa_ag=" + str(Group)  + " order by attnum"  
    if Art == 6: 
        sSQL="select * from (" + sSQL +") as dummy inner join polyatttable  ON dummy.ATTid = polyatttable.poa_idfa where polyatttable.poa_ag=" + str(Group) + " order by attnum"  
    return sSQL   

def EZU492650E7B7434899B738F74CBB9FD56D( Art, AktAttID, Group):
    sSQL=None
    if Art == 0: 
        sSQL=("select * from  pointatttable  where pointatttable.pta_idfa = '%s' and  pointatttable.pta_ag=%d") % (AktAttID, Group)

    if Art == 1 or Art == 5: 

        sSQL=("SELECT la_idfa AS st_attid, attrname AS st_attrname, la_linenr, used, color, sizemm, basemm, basecolor, linesigattr, linesigbegin,linesigofs, linesigofsline, "

              "       lineoffset, sigbeginattr, sigmiddleattr, sigendattr, transparent, denyatpercent, penid, basepenid, sigbeginpos, sigendpos, sigmiddlepos, geocolor, "

              "       scrresize, pentable.* "
              "FROM (frameatttable INNER JOIN lineatttable ON frameatttable.fa_id = lineatttable.la_idfa) "
              "INNER JOIN pentable ON lineatttable.penid =pentable.id "
              "WHERE la_idfa='%s' AND used='J' AND la_ag=%i order by la_linenr DESC") %(AktAttID, Group) 

    if Art == 2: 
        sSQL = None
    if Art == 3: 


        sSQL=("SELECT defname, defid , attrname, lineattr, color, sizemm, fontname, bold, italic, "

              "         underline, freestyle, textalign, frametext, framecolor, framewidthmm, bkcolor, lineattr, tabpos1, tabpos2, usememo, blattnord, "

              "         oneline, charframetext, charframecolor, charframewidthmm, quality, ofsalign "
              "  FROM (textatttable INNER JOIN deftable ON textatttable.ta_idfa = deftable.scrattrname1) "
              "        INNER JOIN frameatttable ON textatttable.ta_idfa = frameatttable.fa_id "
              "  WHERE defid='%s' AND textatttable.ta_ag=%i;") % (AktAttID,Group)

    if Art == 4: 
        sSQL = None

    if Art == 6: 
        sSQL=None       
    return sSQL

if __name__ == "__main__":
    pass


