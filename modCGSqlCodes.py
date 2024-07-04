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











try:
    from fnc4CaigosConnector import *

except:
    from .fnc4CaigosConnector import *

    
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
        table = "meterssqlspatial"
    if Art == 5: 
        table="segssqlspatial"
    if Art == 6: 
        table="polyssqlspatial"    
    return table



def EZUDFCE1DA9263240889EF03443BF48E294 (db):



    qList=("ezu_qry_lines4qgis","ezu_qry_textedelta4qgis","ezu_qry_texte4qgis","ezu_qry_texteref4qgis","ezu_qry_polylines4qgis","ezu_qry_polys4qgis")
    sSQL="SELECT cast(OBJECT_ID('dbo.ezu_qry_points4qgis','V') as bigint)"
    for sQry in qList:
        sSQL=sSQL + ("+ OBJECT_ID('dbo.%s','V')") % (sQry)
    db.Open()
    qry = db.EZUDCF0989FCCB948B08C56317AE7037619(sSQL) 
    if (qry):
        qry.next()
        if (qry.value(0)):
            return True
    else:
        EZUC8DCB02F1A8145AF82C8A69A43E0529B(db.EZU03F45B01171E465F835613DBEE097689())
    return False
    
def EZUC0AEDD5F47634D6B97D2BEF91F31FEC1 (db):
    bFehler=False
    db.Open()
    def EZU37AEC7700A494C7784C3BDE0362794C2(sQry,sql):
        sCreate="CREATE VIEW " + sQry + " AS " + sql
        qry = db.EZUCCB71BB19D114085A02FD5CFC412C1AB(sCreate)
        if not(qry):
            bFehler=True
            EZUC8DCB02F1A8145AF82C8A69A43E0529B(db.EZU03F45B01171E465F835613DBEE097689())     
    

    qList=("ezu_qry_points4qgis","ezu_qry_lines4qgis","ezu_qry_textedelta4qgis","ezu_qry_texte4qgis","ezu_qry_texteref4qgis","ezu_qry_polylines4qgis","ezu_qry_polys4qgis")
    for sQry in qList:
        sSQL=("IF OBJECT_ID('dbo.%s','V') IS NOT NULL \nDROP VIEW  dbo.%s \n") % (sQry,sQry)
        qry = db.EZUCCB71BB19D114085A02FD5CFC412C1AB(sSQL) 
        if not(qry):
            bFehler=True
            EZUC8DCB02F1A8145AF82C8A69A43E0529B(db.EZU03F45B01171E465F835613DBEE097689())



    sSQL=("SELECT ROW_NUMBER() OVER (ORDER BY ObjID) AS ezu_id,* "
          ", geometry::STGeomFromText('POINT(' + str([shape].STX+[DeltaR],15,3)  + str([shape].STY+[DeltaH],15,3) + str([shape].Z,10,3) + ')',[shape].STSrid) as geom "
          ",[shape].STX as x,[shape].STY as y ,[shape].Z as z "
          "FROM [dbo].[POINTSSQLSPATIAL] ")
    EZU37AEC7700A494C7784C3BDE0362794C2 ("ezu_qry_points4qgis",sSQL)

    sSQL="SELECT ROW_NUMBER() OVER (ORDER BY ObjID) AS ezu_id, *,shape as geom from linessqlspatial"
    EZU37AEC7700A494C7784C3BDE0362794C2 ("ezu_qry_lines4qgis",sSQL)

    sSQL="SELECT ROW_NUMBER() OVER (ORDER BY ObjID) AS ezu_id, *,shape as geom from textssqlspatial"
    EZU37AEC7700A494C7784C3BDE0362794C2 ("ezu_qry_texte4qgis",sSQL)

    sSQL="SELECT ROW_NUMBER() OVER (ORDER BY ObjID) AS ezu_id, *,geometry::STGeomFromText('POINT(' + str([shape].STX+[DeltaR],15,3)  + str([shape].STY+[DeltaH],15,3) + str([shape].Z,10,3) + ')',[shape].STSrid) as geom from textssqlspatial"
    EZU37AEC7700A494C7784C3BDE0362794C2 ("ezu_qry_textedelta4qgis",sSQL)
    
    sShape = "shape.ShortestLineTo(geometry::STGeomFromText('POINT(' + str([shape].STX+[DeltaR],15,3)  + str([shape].STY+[DeltaH],15,3) + str([shape].Z,10,3) + ')',[shape].STSrid))"
    sSQL="SELECT ROW_NUMBER() OVER (ORDER BY ObjID) AS ezu_id, *," + sShape  + " as geom from textssqlspatial  WHERE isdelta = 'J' and (deltar * deltah) != 0"
    EZU37AEC7700A494C7784C3BDE0362794C2 ("ezu_qry_texteref4qgis",sSQL)

    sSQL="SELECT ROW_NUMBER() OVER (ORDER BY ObjID) AS ezu_id, *,shape as geom from segssqlspatial"
    EZU37AEC7700A494C7784C3BDE0362794C2 ("ezu_qry_polylines4qgis",sSQL)
    
    sSQL="SELECT ROW_NUMBER() OVER (ORDER BY ObjID) AS ezu_id, *,shape as geom from polyssqlspatial"   
    EZU37AEC7700A494C7784C3BDE0362794C2 ("ezu_qry_polys4qgis",sSQL)    
    
    return not (bFehler)

    
def EZUF218A9CE2308409D9617A675D4D9DC80():
    return "SELECT ('x' || (substr(id,6,4)))::bit(16)::int -1 as objKl,alias, visible FROM objclasstable order by objKl" 

def EZUC919609B70974C769FCCE8339E252DC9( LayerID):
    sSQL = (u"SELECT layername from lyrtable WHERE layerid='%s'") % (LayerID)
    return sSQL
    
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

    sSQL = (u"SELECT layername, lyrtable.layerid, lyrtable.layertyp, dbname, priority \n" 
                "FROM (prptable INNER JOIN lyrtable ON prptable.layerid = lyrtable.layerid) LEFT JOIN frametbltable on lyrtable.tblid = frametbltable.ft_id \n"
                "WHERE usernr='%s' %s \n"
                "UNION ALL \n"
                "SELECT DISTINCT TLayer.layername, TLayer.layerid, TLayer.layertyp, TLayer.dbname, TLayer.priority from  ( \n"
                "SELECT layername || '(RL)' as layername, lyrtable.layerid, 31 as layertyp, cast(''as char) as  dbname, priority FROM (prptable INNER JOIN lyrtable ON prptable.layerid = lyrtable.layerid) \n"
                "LEFT JOIN frametbltable on lyrtable.tblid = frametbltable.ft_id WHERE usernr='%s' AND lyrtable.layertyp=3 %s \n)"
                " \n") % (UserNum,sSQL,UserNum, sSQL) 

    
    
    sSQL = sSQL + " as TLayer inner join \n"
    
    sSQL = sSQL + "(SELECT layerid FROM  \n"
    sSQL = sSQL + "  ( SELECT TOP 100 PERCENT adid FROM (" 
    sSQL = sSQL +  EZUE46C97B18D5843DFB7668B8846F26976 ( 3,None, UserNum) + ") AS TScreenAtt \n"
    sSQL = sSQL + ("INNER JOIN textatttable ON TScreenAtt.ATTid = textatttable.ta_idfa \n"
            "WHERE textatttable.ta_ag=0 and textatttable.lineattr != '{00000000-0000-0000-0000-000000000000}' ORDER BY attnum\n")
            
    sSQL = sSQL + (") AS t1 \n"
    "INNER JOIN "
    "  (SELECT DISTINCT textssqlspatial.defid, layerid \n"
    "   FROM textssqlspatial "
    "   LEFT JOIN deftable ON textssqlspatial.defid =deftable.defid \n"
    "   WHERE  textssqlspatial.defid != '{00000000-0000-0000-0000-000000000000}' \n"
    "   UNION ALL SELECT defid, layerid \n"
    "   FROM prptable \n"
    "   WHERE usernr='000') AS t2 ON t1.adid = t2.defid \n"
    "   ) as T2 on TLayer.layerid = T2.layerid \n"
    "   ORDER BY priority DESC,layertyp ")
    if EZU50464908A0F8417AA7B9045C4E9B1F6A() == 0:
        sSQL=EZUC7AA96B394624996A75241F4F6A0A0C2(sSQL)
    if EZU50464908A0F8417AA7B9045C4E9B1F6A() == 1:
        sSQL=EZU3311744BFDFB478CBE981B15F33460B0(sSQL)

    
    return sSQL

def EZU64C9598DF0AB4FADA28872A43F622D0A( Art, LayerID, bDarObjKl):




    TabName=EZUBB35FE2AD3BE43C0BED5E2BB71976827(Art)
    zSQL=""
    if bDarObjKl:
        zSQL=("UNION select DISTINCT defid,objclassindex as objklasse, 'ObjKlasse: ' || objclassindex as oneObjID from loctable where layerid='%s' ") % (LayerID)
    if TabName:
        sSQL=(u"select DISTINCT ID.defid, COALESCE(defname, '        ') as sortdefname , ID.objklasse, ID.oneObjID "
               " FROM (select defid,-1 as objklasse, min(objid) as oneObjID from %s where layerid='%s' group by defid "
               "     %s) as ID "
               " LEFT JOIN deftable "
               " ON ID.defid =deftable.defid "
               " order by sortdefname") % (TabName,LayerID,zSQL)
        return sSQL
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
        sSQL="select TOP 100 PERCENT * from (" + sSQL +") as TAtt4Ma inner join pointatttable ON TAtt4Ma.ATTid = pointatttable.pta_idfa where pointatttable.pta_ag=" + str(Group)  + " order by attnum"  
    if Art == 1: 
        sSQL=sSQL
    if Art == 2: 
        sSQL="select TOP 100 PERCENT * from (" + sSQL +") as TAtt4Ma inner join (select * from arcatttable where arcatttable.aa_ag=" + str(Group) + ") as arc ON TAtt4Ma.ATTid = arc.aa_idfa  inner join polyatttable  ON arc.polyattr = polyatttable.poa_idfa where polyatttable.poa_ag=" + str(Group) + " order by attnum"  
        sSQL = sSQL
    if Art == 3 or Art == 31: 
       sSQL="select TOP 100 PERCENT * from (" + sSQL +") as TAtt4Ma inner join textatttable ON TAtt4Ma.ATTid = textatttable.ta_idfa where textatttable.ta_ag=" + str(Group)  + " order by attnum"  
    if Art == 4: 
        sSQL = sSQL
    if Art == 5: 
        sSQL="select TOP 100 PERCENT * from (" + sSQL +") as TAtt4Ma inner join segatttable  ON TAtt4Ma.ATTid = segatttable.sa_idfa where segatttable.sa_ag=" + str(Group)  + " order by attnum"  
    if Art == 6: 
        sSQL="select TOP 100 PERCENT * from (" + sSQL +") as TAtt4Ma inner join polyatttable  ON TAtt4Ma.ATTid = polyatttable.poa_idfa where polyatttable.poa_ag=" + str(Group) + " order by attnum"  
    
    if EZU50464908A0F8417AA7B9045C4E9B1F6A() == 0:
        sSQL=EZUC7AA96B394624996A75241F4F6A0A0C2(sSQL)
    if EZU50464908A0F8417AA7B9045C4E9B1F6A() == 1:
        sSQL=EZU3311744BFDFB478CBE981B15F33460B0(sSQL)
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

