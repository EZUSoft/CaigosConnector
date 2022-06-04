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





































import xml.etree.cElementTree as ET
import xml.dom.minidom as dom
import tempfile

from qgis.core import * 
try:
    from clsDatenbank import *
    from fnc4all import *
    from fnc4CaigosConnector import *
    from modSig2SVG import *
    from modCGSqlCodes import *
    
except:
    from .clsDatenbank import *
    from .fnc4all import *
    from .fnc4CaigosConnector import *
    from .modSig2SVG import *
    from .modCGSqlCodes import *
    
glTransparentsWert= 200

def EZU8036FC4B199E4EB28331AA7C5EB47DD5(rsAtt):
    ds=""
    s=""
    for f in range(rsAtt.record().count()):
        if type(rsAtt.value(f)) == unicode:
            ds = ds + u"|" + rsAtt.value(f)
        else:
            ds = ds + u"|" + str(rsAtt.value(f))
    return ds
   
def EZU26CBD5108BDC4550825FF167BC244097(cArt):
    if cArt == 0:
        return 8
    if cArt == 1:
        return 5
    if cArt == 2:
        return 2
    if cArt == 3:
        return 7
    if cArt == 4:
        return 4
    if cArt == 5:
        return 1
    if cArt == 6:
        return 6
    if cArt == 7:
        return 3
    if cArt == 8:
        return 0

        
def EZU7B23FA29B95243FEB2001DDB3C1548D5(cgStyle):        










    pass
            
def EZU0F9999059F73494FB256477BA175CB09(cgStyle):








    if cgStyle==0:
        return "solid"
    if cgStyle==1:
        return "dash"
    if cgStyle==2:
        return "dot"
    if cgStyle==3:
        return "dash dot"
    if cgStyle==4:
        return "dash dot dot"

def EZU35D1AFB8945541DAB55B0B01D32E573E(rsParam):



    s=""
    for i in range(10):
        s=s+";"+ str(fncfield(rsParam,"astyle"+str(i)))
    return s[1:]
    
def EZUE76F287F31504DE7A624D52BDFA53817 (Farbe):
    flist=[]
    flist.append (Farbe & 255)
    flist.append ((Farbe // 256) & 255)
    flist.append (Farbe // 65536)
    return flist

def EZU351B42D999B44FC2864B0EAB23A9882F (Farbe,Transparent=False):
    s=str(Farbe & 255)
    s=s+","+str((Farbe // 256) & 255)
    s=s+","+str (Farbe // 65536) 
    if Transparent:
        s=s+","+ str(glTransparentsWert)
    return s
    
def fncfield (rs,FieldName):
    w= rs.value(rs.record().indexOf(FieldName)) 
    if not w is None:
        return w
    else: 
        errlog ("Fehler: " + FieldName)
    
def EZU15860653386141E5B19CCA1A29AFAB44(root_rule,qtyp,rName,Bedingung):

        new_rule = root_rule.children()[0].clone()
        new_rule.setFilterExpression(Bedingung)
        new_rule.setLabel(rName)
        new_rule.setSymbol(None) 
        root_rule.appendChild(new_rule)
        return new_rule
        
def EZUC39B54C5E0F74D3EAF77C5905F21986A(root_rule,Rollenname,Von, Bis):
        rule = root_rule.children()[0].clone()
        rule.setLabel(Rollenname)       
        rule.setScaleMinDenom(Von)
        rule.setScaleMaxDenom(Bis)
        return rule

def EZUBA666A1C25E14A1BBEE2F71BBC47F289 (pSigPath,pSigName):
    sigPfad=EZUEA8B6496E4A94763B4DE5BCE67BA0F14() 

    svgPfad=EZUA6B299741D5D4E39B1F0ADB88AD47F18() 
    
    if pSigPath == "":
        if EZU6F300E76DB074FB99636B535E712DED7() == "V11":
            pSigPath="PRIV:"

        if EZU6F300E76DB074FB99636B535E712DED7() == "V20xx":
            pSigPath="PUB:" + EZU0239CDC0875B4C7B837227F9004BC5D0() + "\\"

        EZU9AC841489FAD40E4B1A1232B3CA9B315(pSigName + ": Kein Signaturverzeichnis : wird durch '" + pSigPath  + "' ersetzt" )
    
    if pSigPath == "PRIV:" and EZU6F300E76DB074FB99636B535E712DED7() == "V20xx":

        pSigPath="PUB:" + EZU0239CDC0875B4C7B837227F9004BC5D0() + "\\"
        EZU9AC841489FAD40E4B1A1232B3CA9B315(pSigName + ": 'PRIV:' : wird durch '" + pSigPath  + "' ersetzt" )
        
    cgPfad=pSigPath.replace("PRIV:",sigPfad).replace("PUB:",sigPfad)


    qDat= cgPfad + pSigName  + ".sig"
    qDat=qDat.replace("\\","/")
    zDat=None
    if svgPfad:
        svgPfad=pSigPath.replace("PRIV:",svgPfad).replace("PUB:",svgPfad)
        zDat = svgPfad + pSigName + ".svg"
        zDat=zDat.replace("\\","/")
    return  svgPfad, qDat, zDat
    
def EZUECF30286359145F8A6FCFF9D953FB103(db, qLayer,AktDefName, Group):
        rsAtt=db.EZUDCF0989FCCB948B08C56317AE7037619(EZU492650E7B7434899B738F74CBB9FD56D(3, AktDefName, Group))
        symbol = QgsSymbolV2.defaultSymbol(QGis.Point)
        symbol.setSize( 0.0 )
        qLayer.setRendererV2( QgsSingleSymbolRendererV2( symbol ) )

        if rsAtt.next():


            QgsPalLayerSettings().writeToLayer( qLayer )
            qLayer.setCustomProperty("labeling","pal")
            qLayer.setCustomProperty("labeling/dataDefined/Rotation","alpha")
            qLayer.setCustomProperty("labeling/displayAll","true")
            qLayer.setCustomProperty("labeling/enabled","true")
            qLayer.setCustomProperty("labeling/fieldName","pstext")
            qLayer.setCustomProperty("labeling/fontBold","True" if rsAtt.value(7) == "J" else "False") 
            qLayer.setCustomProperty("labeling/fontFamily",rsAtt.value(6)) 
            qLayer.setCustomProperty("labeling/fontItalic","True" if rsAtt.value(8) == "J" else "False")
            qLayer.setCustomProperty("labeling/fontUnderline","True" if rsAtt.value(9) == "J" else "False")
            qLayer.setCustomProperty("labeling/fontSize",rsAtt.value(5)) 
            qLayer.setCustomProperty("labeling/fontSizeInMapUnits","true")
            qLayer.setCustomProperty("labeling/obstacle","false")
            qLayer.setCustomProperty("labeling/placement","1")
            qLayer.setCustomProperty("labeling/placementFlags","0")
            qLayer.setCustomProperty("labeling/quadOffset", EZU26CBD5108BDC4550825FF167BC244097(rsAtt.value(11))) 
            qLayer.setCustomProperty("labeling/textColorA","255")
            
            color = EZUE76F287F31504DE7A624D52BDFA53817(rsAtt.value(4)) 
            qLayer.setCustomProperty("labeling/textColorR",color[0])
            qLayer.setCustomProperty("labeling/textColorG",color[1])
            qLayer.setCustomProperty("labeling/textColorB",color[2])

            qLayer.setCustomProperty("labeling/textTransp","0")
            qLayer.setCustomProperty("labeling/upsidedownLabels","2")
            qLayer.setCustomProperty("labeling/wrapChar",r"\n")  

def EZUC7C192F1878045F492C281DD6C4D4621 (eSym,db,AttID,Win, Num, Group):
    rsParam=db.EZUDCF0989FCCB948B08C56317AE7037619(EZU492650E7B7434899B738F74CBB9FD56D(0, AttID , Group))
    rsParam.next()

    qPfad,qDat,zDatOrBase64 = EZUBA666A1C25E14A1BBEE2F71BBC47F289(fncfield(rsParam,"sigpath"),fncfield(rsParam,"signame"))
    if qPfad:
        EZUEC3EF0E87A7B41F0BCB1C49ECEEDCE0C (qPfad, True)
        EZUA4E9AB9A09C14707873F50EB1D7815E2 (qDat,zDatOrBase64)
    else:
        zDatOrBase64 = EZUA4E9AB9A09C14707873F50EB1D7815E2 (qDat,None)


    qmap={'pass':'0','class':'SVGFill','locked':'0'}
    eLayer=ET.SubElement(eSym,"layer",qmap)    
    prop={}
    prop['angle']=str(Win)
    prop['svgFile']=zDatOrBase64
    prop['width']=str(fncfield(rsParam,"wsizemm"))
    prop['pattern_width_unit']="MapUnit"
    for p in prop:
        ET.SubElement(eLayer, "prop",k=p,v=prop[p])
    

    qmap={}   
    qmap['alpha']='1'
    qmap['clip_to_extent']='1'
    qmap['type']='line'
    eSym=ET.SubElement(eLayer,"symbol",qmap)   
    qmap={} 
    qmap={'pass':'0','class':'SimpleLine','locked':'0'}
    eLayer=ET.SubElement(eSym,"layer",qmap)    
    ET.SubElement(eLayer, "prop",k="line_width",v="0")    

    
    return eLayer   
    
def EZUAA5C08AC4E7F456A9AED61FCF8291720 (eSym,db,AttID,qPosition, sUnit, Group, Abstand=None, Start=0, Offset = 0):

        rsParam=db.EZUDCF0989FCCB948B08C56317AE7037619(EZU492650E7B7434899B738F74CBB9FD56D(0, AttID , Group))
        rsParam.next()


        qPfad,qDat,zDatOrBase64 = EZUBA666A1C25E14A1BBEE2F71BBC47F289(fncfield(rsParam,"sigpath"),fncfield(rsParam,"signame"))
        if qPfad:
            EZUEC3EF0E87A7B41F0BCB1C49ECEEDCE0C (qPfad, True)
            EZUA4E9AB9A09C14707873F50EB1D7815E2 (qDat,zDatOrBase64)
        else:
            zDatOrBase64 = EZUA4E9AB9A09C14707873F50EB1D7815E2 (qDat,None)
        


        qmap={'pass':'0','class':'MarkerLine','locked':'0'}
        eLayer=ET.SubElement(eSym,"layer",qmap)    
        prop={}
        if not Abstand is None: 
            prop['interval']=str(Abstand+fncfield(rsParam,"wsizemm"))
            prop['interval_map_unit_scale']='0,0,0,0,0,0'
            prop['interval_unit']="MapUnit" 
        else:

            prop['placement']=qPosition
        


        prop['offset_along_line']=str(Start) 
        prop['offset_along_line_unit']="MapUnit"
        prop['offset']=str(Offset * -1)
        prop['offset_unit']="MapUnit"
        prop['offset_along_line_unit']="MapUnit"
        prop['offset_map_unit_scale']='0,0,0,0,0,0'


        prop['rotate']='1'    
        for p in prop:
            ET.SubElement(eLayer, "prop",k=p,v=prop[p])
        

        qmap={}   
        qmap['alpha']='1'
        qmap['clip_to_extent']='1'
        qmap['type']='marker'
        eSym=ET.SubElement(eLayer,"symbol",qmap)   
        qmap={} 
        qmap={'pass':'0','class':'SvgMarker','locked':'0'}
        eLayer=ET.SubElement(eSym,"layer",qmap)    
        prop={}
        prop['angle']='0' 
        prop['color']='0,0,0,255'
        prop['horizontal_anchor_point']='1'
        prop['name']=zDatOrBase64
        prop['offset']='0,0'
        prop['offset_map_unit_scale']='0,0,0,0,0,0'
        prop['offset_unit']= sUnit
        prop['outline_color']='255,255,255,255'
        prop['outline_width']='0'
        prop['outline_width_map_unit_scale']='0,0,0,0,0,0'
        prop['outline_width_unit']='MM'
        prop['scale_method']='diameter'
        prop['size']=str(fncfield(rsParam,"wsizemm"))
        prop['size_map_unit_scale']='0,0,0,0,0,0'
        prop['size_unit']=sUnit
        prop['vertical_anchor_point']='1'    
        for p in prop:
            ET.SubElement(eLayer, "prop",k=p,v=prop[p])    










def EZU257B2E8C689B476E864807F64F1C77D7 (eSym,rsAtt,Num, Group):
    if fncfield(rsAtt,"fsalign") == 1:

        sWin= '"alphafs"' if Num ==1  else '"alphafs"+90'
    else:

        sWin= str(fncfield(rsAtt,"fsalpha")) if Num ==1  else str(fncfield(rsAtt,"fsalpha")+90)
    qmap={'pass':'0','class':'LinePatternFill','locked':'0'}
    l1=ET.SubElement(eSym,"layer",qmap)                           
    prop={}
    prop['lineangle_expression']=sWin
    prop['color']='0,0,255,255'
    prop['distance']=str(fncfield(rsAtt,"fsabstand" + str(Num)))
    prop['distance_map_unit_scale']='0,0,0,0,0,0'
    prop['distance_unit']='MapUnit'
    prop['line_width']='0.26'
    prop['line_width_map_unit_scale']='0,0,0,0,0,0'
    prop['line_width_unit']='MM'
    prop['offset']='0'
    prop['offset_map_unit_scale']='0,0,0,0,0,0'
    prop['offset_unit']='MM'
    prop['outline_width_map_unit_scale']='0,0,0,0,0,0'
    prop['outline_width_unit']='MM'
    for p in prop:
        ET.SubElement(l1, "prop",k=p,v=prop[p]) 
    return ET.SubElement(l1, "symbol", {'alpha':'1','clip_to_extent':'1','type':'line'})                                                            

            

def EZU352CEF05BE474C37B4809B26B2A75BE7 (eSymbols, symNum,db,qTyp, LinArt, AktAttID, Group, AttNum,eSym = None,fDist = None,fWin = None):

    rsParam=db.EZUDCF0989FCCB948B08C56317AE7037619(EZU492650E7B7434899B738F74CBB9FD56D(1, AktAttID, Group))









    if LinArt=="fill":
        bSchraff=True
        LinArt="line"

    else:    
        bSchraff=False

        



    
    
    if rsParam.size() == 0:
        if LinArt == "outline":

            debuglog( "\nEineStreckeAttributieren: " + str(AttNum) + ";" + LinArt + ";" + AktAttID + ";"+ str(Group) + " kein Attribut")
        else:
            errlog( "\nEineStreckeAttributieren: " + str(AttNum) + ";" + LinArt + ";" + AktAttID + ";"+ str(Group) + " kein Attribut")
    


    if eSym == None:
        qmap={}   
        qmap['alpha']='1'
        qmap['clip_to_extent']='1'
        qmap['type']='line'
        qmap['name']=str(symNum)
        eSym=ET.SubElement(eSymbols,"symbol",qmap)

    
    while rsParam.next(): 


        basemm=fncfield(rsParam,"basemm")
        penType=fncfield(rsParam,"pentype")
        if penType < 5:
            penArt=EZU0F9999059F73494FB256477BA175CB09(penType)
        else:
            penArt=EZU35D1AFB8945541DAB55B0B01D32E573E(rsParam)
            
        unitArt='MapUnit' if fncfield(rsParam,"scrresize") == "J" else "MM"
        
        if basemm > 0:

            qmap={'pass':'0','class':'SimpleLine','locked':'0'}
            eLayer=ET.SubElement(eSym,"layer",qmap)
            prop={}
            prop['capstyle']='square'
            prop['customdash']='5;2'
            prop['customdash_map_unit_scale']='0,0'
            prop['customdash_unit']='MM'
            prop['draw_inside_polygon']='0'
            prop['joinstyle']='bevel'
            prop[LinArt+'_color']=EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"basecolor"),True if fncfield(rsParam,"transparent") == "J" else False)
            prop[LinArt+'_style']='solid'
            prop[LinArt+'_width']=str(fncfield(rsParam,"sizemm") + basemm * 2) 
            prop[LinArt+'_width_unit']=unitArt
            prop['offset']='0'
            prop['offset_map_unit_scale']='0,0'
            prop['offset_unit']='MapUnit'
            prop['use_custom_dash']='0'
            prop['width_map_unit_scale']='0,0'
            for p in prop:
                ET.SubElement(eLayer, "prop",k=p,v=prop[p])


        

        qmap={'pass':'1' if basemm > 0 else '0','class':'SimpleLine','locked':'0'}
        eLayer=ET.SubElement(eSym,"layer",qmap)
        prop={}
        if penType < 5:
            prop["line_style"]=penArt
            prop["use_custom_dash"]=str(0)
        else:
            prop["customdash"]=penArt
            prop["use_custom_dash"]=str(1)

        prop['capstyle']='square'

        prop['customdash_map_unit_scale']='0,0,0,0,0,0'
        prop['customdash_unit']='MM'
        prop['draw_inside_polygon']='0'
        prop['joinstyle']='bevel'
        prop[LinArt+"_color"]=EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"color"),True if fncfield(rsParam,"transparent") == "J" else False)

        prop[LinArt+'_width']=str(fncfield(rsParam,"sizemm"))
        prop[LinArt+'_width_unit']=unitArt
        prop["offset"]=str(fncfield(rsParam,"lineoffset") * (-1 if LinArt=="outline" else 1))
        prop['offset_map_unit_scale']='0,0,0,0,0,0'
        prop['offset_unit']='MapUnit'

        prop['width_map_unit_scale']='0,0,0,0,0,0'
         
        
        if bSchraff:
            prop["distance"]=str(fDist)
            prop["distance_unit"]="MapUnit"      
            prop["outline_style"]='no' 
            prop["angle"]=str(fWin)


        for p in prop:
            ET.SubElement(eLayer, "prop",k=p,v=prop[p])
            





        sUnit='MapUnit'
        if fncfield(rsParam,"sigbeginattr") != "{00000000-0000-0000-0000-000000000000}":    
            EZUAA5C08AC4E7F456A9AED61FCF8291720 (eSym,db,fncfield(rsParam,"sigbeginattr") ,'firstvertex',sUnit, Group)
        if fncfield(rsParam,"sigendattr") != "{00000000-0000-0000-0000-000000000000}":    
            EZUAA5C08AC4E7F456A9AED61FCF8291720 (eSym,db,fncfield(rsParam,"sigendattr") ,'lastvertex',sUnit, Group)
        if fncfield(rsParam,"sigmiddleattr") != "{00000000-0000-0000-0000-000000000000}":    
            EZUAA5C08AC4E7F456A9AED61FCF8291720 (eSym,db,fncfield(rsParam,"sigmiddleattr") ,'centralpoint',sUnit, Group)
        if fncfield(rsParam,"linesigattr") != "{00000000-0000-0000-0000-000000000000}":    
            EZUAA5C08AC4E7F456A9AED61FCF8291720 (eSym,db,fncfield(rsParam,"linesigattr") ,'egal',sUnit, Group,fncfield(rsParam,"linesigofs"),fncfield(rsParam,"linesigbegin"),fncfield(rsParam,"linesigofsline"))
               
    return eSymbols
        
def EZU8EE910E18038480A85D466F9C4F15D48 (eSymbols, symNum,qTyp,rsParam) :










    def EZU3559CBC163424A26BA92C21243D71277(Winkel,AktColor,eSym):

            eLayer=ET.SubElement(eSym,"layer",{'pass':'0','class':'LinePatternFill','locked':'0'})
            prop={}
            prop['angle']=str(Winkel)
            prop['color']=AktColor
            prop['distance']='2.5'
            prop['distance_map_unit_scale']='0,0,0,0,0,0'
            prop['distance_unit']='MM'
            prop['line_width']='0.1'
            prop['line_width_map_unit_scale']='0,0,0,0,0,0'
            prop['line_width_unit']='MM'
            prop['offset']='0'
            prop['offset_map_unit_scale']='0,0,0,0,0,0'
            prop['offset_unit']='MM'
            prop['outline_width_map_unit_scale']='0,0,0,0,0,0'
            prop['outline_width_unit']='MM'
            for p in prop:
                ET.SubElement(eLayer, "prop",k=p,v=prop[p])

            eUSym=ET.SubElement(eLayer,"symbol",{'alpha':'1','clip_to_extent':'1','type':'line'})
            uLayer=ET.SubElement(eUSym,"layer",{'pass':'0','class':'SimpleLine','locked':'0'})
            prop={}
            prop['capstyle']='square'
            prop['customdash']='5;2'
            prop['customdash_map_unit_scale']='0,0,0,0,0,0'
            prop['customdash_unit']='MM'
            prop['draw_inside_polygon']='0'
            prop['joinstyle']='bevel'
            prop['line_color']=AktColor
            prop['line_style']='solid'
            prop['line_width']='0.1'
            prop['line_width_unit']='MM'
            prop['offset']='0'
            prop['offset_map_unit_scale']='0,0,0,0,0,0'
            prop['offset_unit']='MM'
            prop['use_custom_dash']='0'
            prop['width_map_unit_scale']='0,0,0,0,0,0'
            for p in prop:
                ET.SubElement(uLayer, "prop",k=p,v=prop[p])
            return eLayer
            
            
    cgArt=fncfield(rsParam,"brushstyle")

    qmap={}   
    qmap['alpha']='1'
    qmap['clip_to_extent']='1'
    qmap['type']='fill'
    qmap['name']=str(symNum)
    eSym=ET.SubElement(eSymbols,"symbol",qmap)


    if cgArt==0: 

        eLayer=ET.SubElement(eSym,"layer",{'pass':'0','class':'SimpleFill','locked':'0'})        
        prop={}
        prop['border_width_map_unit_scale']='0,0,0,0,0,0'
        prop['color']=EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"brushcolor"),True if fncfield(rsParam,"transparent") == "J" else False)
        prop['joinstyle']='bevel'
        prop['offset']='0,0'
        prop['offset_map_unit_scale']='0,0,0,0,0,0'
        prop['offset_unit']='MM'
        prop['outline_color']='0,0,0,255'
        prop['outline_style']='no'
        prop['outline_width']='0.26'
        prop['outline_width_unit']='MM'
        prop['style']='solid'
        for p in prop:
            ET.SubElement(eLayer, "prop",k=p,v=prop[p])
    if cgArt==1: 
        dummy = ""
    if cgArt==2: 
        eLayer=EZU3559CBC163424A26BA92C21243D71277(0, EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"brushcolor"),True if fncfield(rsParam,"transparent") == "J" else False),eSym)       
    if cgArt==3: 
        eLayer=EZU3559CBC163424A26BA92C21243D71277(90,EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"brushcolor"),True if fncfield(rsParam,"transparent") == "J" else False), eSym)           
    if cgArt==4: 
        eLayer=EZU3559CBC163424A26BA92C21243D71277(135,EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"brushcolor"),True if fncfield(rsParam,"transparent") == "J" else False), eSym)        
    if cgArt==5: 
        eLayer=EZU3559CBC163424A26BA92C21243D71277(45,EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"brushcolor"),True if fncfield(rsParam,"transparent") == "J" else False), eSym)          
    if cgArt==6: 
        eLayer=EZU3559CBC163424A26BA92C21243D71277(0,EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"brushcolor"),True if fncfield(rsParam,"transparent") == "J" else False), eSym)          
        eLayer=EZU3559CBC163424A26BA92C21243D71277(90,EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"brushcolor"),True if fncfield(rsParam,"transparent") == "J" else False), eSym)          
    if cgArt==7: 
        eLayer=EZU3559CBC163424A26BA92C21243D71277(45,EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"brushcolor"),True if fncfield(rsParam,"transparent") == "J" else False), eSym)          
        eLayer=EZU3559CBC163424A26BA92C21243D71277(135,EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"brushcolor"),True if fncfield(rsParam,"transparent") == "J" else False), eSym)            
        
    return  eSym

def EZUB8570788139F4F55BFDC9CB6054BC538 (eSymbols, symNum,  rsParam ) :

    qPfad,qDat,zDatOrBase64 = EZUBA666A1C25E14A1BBEE2F71BBC47F289(fncfield(rsParam,"sigpath"),fncfield(rsParam,"signame"))
    if qPfad:
        EZUEC3EF0E87A7B41F0BCB1C49ECEEDCE0C (qPfad, True)
        EZUA4E9AB9A09C14707873F50EB1D7815E2 (qDat,zDatOrBase64)
    else:
        zDatOrBase64 = EZUA4E9AB9A09C14707873F50EB1D7815E2 (qDat,None)
    

    unitArt='MapUnit' if fncfield(rsParam,"scrresize") == "J" else "MM"
    


    qmap={}   
    qmap['alpha']='1'
    qmap['clip_to_extent']='1'
    qmap['type']='marker'
    qmap['name']=str(symNum)
    eSym=ET.SubElement(eSymbols,"symbol",qmap)
    


    qmap={'pass':'0','class':'SvgMarker','locked':'0'}
    eLayer=ET.SubElement(eSym,"layer",qmap)
    
    prop={}
    prop['angle']='0'
    prop['angle_dd_active']='1'
    prop['angle_dd_expression']='abs(360-alpha )' 
    prop['angle_expression']='abs(360-alpha )'    
    prop['angle_dd_field']=''
    prop['angle_dd_useexpr']='1'
    prop['color']='0,0,0,255'
    prop['horizontal_anchor_point']='1'
    prop['name']=zDatOrBase64
    prop['offset']='0,0'
    prop['offset_map_unit_scale']='0,0,0,0,0,0'
    prop['offset_unit']=unitArt
    prop['outline_color']='0,0,0,255'
    prop['outline_width']='0.2'
    prop['outline_width_map_unit_scale']='0,0,0,0,0,0'
    prop['outline_width_unit']='MM'
    prop['scale_method']='diameter'
    prop['size']=str(fncfield(rsParam,"wsizemm"))
    prop['size_map_unit_scale']='0,0,0,0,0,0'
    prop['size_unit']=unitArt
    prop['vertical_anchor_point']='1'
    for p in prop:
        ET.SubElement(eLayer, "prop",k=p,v=prop[p])
     
    qmap={}
    qmap['size']=str(fncfield(rsParam,"wsizemm"))
    qmap['size_unit']=unitArt
    qmap['name']=zDatOrBase64

    ET.SubElement(eSym,"layer",qmap)
    
    return eSymbols    

def EZU9FE03FB711BE4A2C8B8130D9B8786C9F (eSettings,rsParam,art='e'):


    qmap={}   
    qmap['fontItalic']= "1" if fncfield(rsParam,"italic") == "J" else '0'
    qmap['fontFamily']=fncfield(rsParam,"fontname")
    qmap['fontLetterSpacing']='0'
    qmap['fontUnderline']='0'
    qmap['fontSizeMapUnitMaxScale']='0'
    qmap['fontWeight']='50'
    qmap['fontStrikeout']='0'
    qmap['textTransp']='0'
    qmap['previewBkgrdColor']='#ffffff'
    qmap['fontCapitals']='0'
    qmap["textColor"]= EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"color"))
    qmap['fontSizeMapUnitMinScale']='0'
    qmap['fontSizeInMapUnits']='1' if fncfield(rsParam,"scrresize") == "J" else '0'
    qmap['isExpression']='1'
    qmap['blendMode']='0'

    qmap['fontSize']=str(fncfield(rsParam,"sizemm") * ( 1 if fncfield(rsParam,"scrresize") == "J" else 2 ))
    

    if art == 'e':
        qmap['fieldName']="replace(replace(\"pstext\",'\\\\u','')  ,'\\\\c','')"   


    if art == 'z':
        qmap['fieldName']="replace(replace(case when regexp_match(\"pstext\",'\\\\\\\\n') then regexp_substr(\"pstext\",'.*\\\\\\\\n') else \"pstext\" end,'\\\\u','')  ,'\\\\c','')"   


    if art == 'n':
        qmap['fieldName']="replace(replace(case when regexp_match(\"pstext\",'\\\\\\\\n') then regexp_substr(\"pstext\",'\\\\\\\\n.*')  end,'\\\\u','')  ,'\\\\c','')"   

    
    s='Normal'
    if fncfield(rsParam,"bold")=="J":
        s="Bold"
    if fncfield(rsParam,"italic")=="J":
        s="Italic"  
    if fncfield(rsParam,"bold")=="J" and fncfield(rsParam,"italic")=="J":
        s="Bold Italic"     
    qmap['namedStyle']=s
    qmap['fontWordSpacing']='0'    
    ET.SubElement(eSettings,"text-style",qmap)




    qmap={} 
    qmap['placeDirectionSymbol']='0'
    qmap['multilineAlign']='0'
    qmap['rightDirectionSymbol']='>'
    qmap['multilineHeight']='1'
    qmap['plussign']='0'
    qmap['addDirectionSymbol']='0'
    qmap['leftDirectionSymbol']='&lt;'
    qmap['formatNumbers']='0'
    qmap['decimals']='0'
    qmap['wrapChar']='\\n'
    qmap['reverseDirectionSymbol']='0'
    ET.SubElement(eSettings,"text-format",qmap)
    


    qmap={'repeatDistanceUnit':'1','placement':'0','maxCurvedCharAngleIn':'20','repeatDistance':'0','distMapUnitMaxScale':'0','labelOffsetMapUnitMaxScale':'0','distInMapUnits':'0',
          'labelOffsetInMapUnits':'1','xOffset':'0','predefinedPositionOrder':'TR,TL,BR,BL,R,L,TSR,BSR','preserveRotation':'1','centroidWhole':'0','priority':'0',
          'repeatDistanceMapUnitMaxScale':'0','yOffset':'0','offsetType':'0','placementFlags':'0','repeatDistanceMapUnitMinScale':'0','centroidInside':'0','dist':'0','angleOffset':'0',
          'maxCurvedCharAngleOut':'-20','fitInPolygonOnly':'0','quadOffset':'4','distMapUnitMinScale':'0','labelOffsetMapUnitMinScale':'0'}
    ET.SubElement(eSettings,"placement",qmap)
    


    qmap={'fontMinPixelSize':'3','scaleMax':'0','fontMaxPixelSize':'10000','scaleMin':'0','upsidedownLabels':'2','limitNumLabels':'0','obstacle':'0','obstacleFactor':'1',
          'scaleVisibility':'0','fontLimitPixelSize':'0','mergeLines':'0','obstacleType':'0','labelPerPart':'0','zIndex':'0','maxNumLabels':'2000','displayAll':'1','minFeatureSize':'0'}
    ET.SubElement(eSettings,"rendering",qmap)
    


    eD=ET.SubElement(eSettings,"data-defined")
    
    qmap={} 
    qmap['expr']=''
    qmap['field']='alpha'
    qmap['active']='true'
    qmap['useExpr']='false'
    ET.SubElement(eD,"Rotation",qmap)
        
    qmap={} 
    qmap['expr']= str(EZU26CBD5108BDC4550825FF167BC244097(fncfield(rsParam,"textalign")))
    qmap['field']=''
    qmap['active']='true'
    qmap['useExpr']='true'
    ET.SubElement(eD,"OffsetQuad",qmap)

    qmap={} 


    if art != 'n':
        qmap['expr']= "regexp_match(\"pstext\",'\\\\\\\\u')"
    
    qmap['field']=''
    qmap['active']='true'
    qmap['useExpr']='true'
    ET.SubElement(eD,"Underline",qmap)    

    qmap={} 
    qmap['expr']= ("case %s when strpos(\"pstext\",'\\\\\\\\c') then 'Center' %s else 'Left' %s end") % ( chr(13)+chr(10),chr(13)+chr(10),chr(13)+chr(10))
    qmap['field']=''
    qmap['active']='true'
    qmap['useExpr']='true'
    ET.SubElement(eD,"MultiLineAlignment",qmap)  





    if fncfield(rsParam,"charframetext") == 'J':
        qmap={} 
        qmap['bufferSize']=str(fncfield(rsParam,"charframewidthmm"))
        qmap['bufferNoFill']="0" 
        qmap['bufferSizeUnits']="MapUnit" 
        qmap['bufferOpacity']="0.9" 
        qmap['bufferDraw']="1" 
        qmap['bufferSizeMapUnitScale']="3x:0,0,0,0,0,0" 
        qmap['bufferJoinStyle']="128" 
        qmap['bufferBlendMode']="0" 
        qmap['bufferColor']=EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"charframecolor")) 
        ET.SubElement(eSettings,"text-buffer",qmap)       
    





    bAktiv=(fncfield(rsParam,"freestyle") == "J" or fncfield(rsParam,"frametext") == "J")
    if bAktiv and fncfield(rsParam,"freestyle") == "N":
        bkColor='0'
    else:    
        bkColor = EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"bkcolor"))
    if bAktiv and fncfield(rsParam,"frametext") == "N":
        wRand='0'
    else:    
        wRand=str(fncfield(rsParam,"framewidthmm")/2) 
    qmap={}
    qmap['shapeSizeUnits']='1'
    qmap['shapeType']='0'
    qmap['shapeOffsetMapUnitMinScale']='0'
    qmap['shapeSizeMapUnitMinScale']='0'
    qmap['shapeSVGFile']=''
    qmap['shapeOffsetX']='0'
    qmap['shapeOffsetY']='0'
    qmap['shapeBlendMode']='0'
    qmap['shapeBorderWidthMapUnitMaxScale']='0'
    qmap['shapeFillColor']=bkColor
    qmap['shapeTransparency']='0'
    qmap['shapeSizeType']='0'
    qmap['shapeJoinStyle']='64'
    qmap['shapeDraw']='1' if bAktiv else '0'
    qmap['shapeSizeMapUnitMaxScale']='0'
    qmap['shapeBorderWidthUnits']='2' 
    qmap['shapeSizeX']='0'
    qmap['shapeSizeY']='0'
    qmap['shapeRadiiX']='0'
    qmap['shapeOffsetMapUnitMaxScale']='0'
    qmap['shapeOffsetUnits']='1'
    qmap['shapeRadiiY']='0'
    qmap['shapeRotation']='0'
    qmap['shapeBorderWidth']=wRand
    qmap['shapeRadiiMapUnitMinScale']='0'
    qmap['shapeRadiiMapUnitMaxScale']='0'
    qmap['shapeBorderColor']=EZU351B42D999B44FC2864B0EAB23A9882F(fncfield(rsParam,"framecolor"))
    qmap['shapeRotationType']='0'
    qmap['shapeRadiiUnits']='1'
    qmap['shapeBorderWidthMapUnitMinScale']='0'
    ET.SubElement(eSettings,"background",qmap)



    return eSettings    

class clsRenderingByQML():      
    def EZUD5A9A7B19C594CD5AA23BB973E8B906D(self, AktDB, cgUser, qLayer, cgEbenenTyp, LayerID, bRolle, Group, bDarObjKl): 

        symNum=0
        
        db=AktDB




        eRoot = ET.Element("qgis")
        if bRolle and (cgEbenenTyp == 3):
            eLabeling = ET.SubElement(eRoot,"labeling",{'type':'rule-based'}) 
            eRenderer = ET.SubElement(eRoot,"renderer-v2",{'forceraster':'0','symbollevels':'0','type':'singleSymbol','enableorderby':'0'})
        else:
            eRenderer = ET.SubElement(eRoot,"renderer-v2",{'symbollevels':'0', 'type':'RuleRenderer'})






        if bRolle : 
            if bDarObjKl:

                fobjKlasse=EZUBB67DB325F4F4F50AB72347B87373BAD (db, LayerID)
            else:
                fobjKlasse=None
            rsAttDefs=db.EZUDCF0989FCCB948B08C56317AE7037619(EZU64C9598DF0AB4FADA28872A43F622D0A( cgEbenenTyp, LayerID, bDarObjKl))

            if cgEbenenTyp == 3:
                eRules = ET.SubElement(eLabeling,"rules")
            else:
                eRules = ET.SubElement(eRenderer,"rules")

            eSymbols= ET.SubElement(eRenderer,"symbols")
            

            while (rsAttDefs.next()):

                AktObjKl = rsAttDefs.value(2)
                bIA = False
                if rsAttDefs.value(0) == "{00000000-0000-0000-0000-000000000000}" or rsAttDefs.value(0) == NULL:
                    AktDefID = EZUAFAF458DCD164EA4A76CF69189C827B7(db, LayerID, cgUser, rsAttDefs.value(2))
                    AktDefName=EZUDCADB4666E944E57BEC334CD9635C33E(db, AktDefID)
                else:
                    AktDefID = rsAttDefs.value(0)
                    if rsAttDefs.value(2) == -1:
                        bIA = True
                        AktDefName="IA:"+rsAttDefs.value(1)
                    else:
                        AktDefName="OK" + str(rsAttDefs.value(2)) + ":" + rsAttDefs.value(1)

                    

                rsAtt=db.EZUDCF0989FCCB948B08C56317AE7037619(EZUE46C97B18D5843DFB7668B8846F26976(cgEbenenTyp, AktDefID, Group))
                if (rsAtt== None):
                    print (EZUE46C97B18D5843DFB7668B8846F26976(cgEbenenTyp, AktDefID, Group))

                if rsAtt.size() == 0 :





                    rsLayerName = db.EZUDCF0989FCCB948B08C56317AE7037619(EZU78184C71D89340528FDC57FFA2DEE943(LayerID))
                    rsLayerName.next()
                    EZU9AC841489FAD40E4B1A1232B3CA9B315('Layer: ' + EZU1FCD98CB63A64E32A30A1F171BE370F3(rsLayerName.value(0)) + " /CaigosAD: " + EZU1FCD98CB63A64E32A30A1F171BE370F3(rsAttDefs.value(1)) + 
                       " /QGisAD: "+EZU1FCD98CB63A64E32A30A1F171BE370F3(AktDefName)+" /Typ: " + str(cgEbenenTyp) + " - Kein Attribut gefunden; Erstes Objekt: " + EZU1FCD98CB63A64E32A30A1F171BE370F3(rsAttDefs.value(3)))

                

                qmap={}
                if rsAttDefs.value(0) == NULL:
                    qmap["filter"]= "defid is Null"
                else:
                    if bDarObjKl:
                        if bIA:

                            qmap["filter"]= "defid = '" + rsAttDefs.value(0) + "'"
                        else:
                            if AktObjKl != -1:
                                qmap["filter"]= "defid = '{00000000-0000-0000-0000-000000000000}' AND objclass = " + str(AktObjKl)
                            else:
                                qmap["filter"]= "defid = '" + rsAttDefs.value(0) + "' " + fobjKlasse
                    else:

                        qmap["filter"]= "defid = '" + rsAttDefs.value(0) + "'"

                if cgEbenenTyp == 3:
                    qmap["description"] = AktDefName
                else:
                    qmap["label"] = AktDefName
                eORule = ET.SubElement(eRules,"rule",qmap)

                

                while (rsAtt.next()): 
                    symNum=symNum + 1
                    mMin=fncfield(rsAtt,"MMin")
                    qmap={}
                    qmap["scalemindenom"]= str(1 if mMin==0 else mMin)
                    qmap["scalemaxdenom"] = str(fncfield(rsAtt,"MMax"))
                    if cgEbenenTyp == 3:
                        qmap["description"] = str(fncfield(rsAtt,"AttNum")) + ":" + fncfield(rsAtt,"ATTname")


                    else:
                        qmap["label"] = str(fncfield(rsAtt,"AttNum")) + fncfield(rsAtt,"ATTname")

                    qmap["symbol"] = str(symNum)
                    AktRule=ET.SubElement(eORule,"rule",qmap)
                    if cgEbenenTyp == 0:
                        qTyp=qLayer.geometryType()

                        EZUB8570788139F4F55BFDC9CB6054BC538 (eSymbols, symNum,  rsAtt)
    

                    if cgEbenenTyp == 1: 
                        qTyp = qLayer.geometryType()
                        EZU352CEF05BE474C37B4809B26B2A75BE7 (eSymbols, symNum,  db, qTyp, "line", fncfield(rsAtt,"ATTid"),Group,fncfield(rsAtt,"AttNum") )                     




                    if cgEbenenTyp == 3: 

                        s1  = ET.SubElement(eSymbols, "symbol", {'alpha':'1','clip_to_extent':'1','type':'marker','name':'0'})
                        l1 =  ET.SubElement(s1,       "layer" , {'locked': '0', 'class': 'SimpleMarker', 'pass': '0'})
                        props={'size': '0.0', 'size_unit': 'MM'}
                        for p in props:
                            ET.SubElement(l1, "prop",k=p,v=props[p])
                        

                        eSettings=ET.SubElement(AktRule,"settings")
                        eSettings = EZU9FE03FB711BE4A2C8B8130D9B8786C9F (eSettings,rsAtt,'z' )
                        

                        symNum=symNum+1;qmap["symbol"] = str(symNum);AktRule=ET.SubElement(eORule,"rule",qmap)
                        
                        eSettings=ET.SubElement(AktRule,"settings")                        
                        eSettings = EZU9FE03FB711BE4A2C8B8130D9B8786C9F (eSettings,rsAtt,'n' )                         
 
                    if cgEbenenTyp == 31: 
                        qTyp = qLayer.geometryType()
                        EZU352CEF05BE474C37B4809B26B2A75BE7 (eSymbols, symNum, db, qTyp, "line", fncfield(rsAtt,"lineattr"),Group,fncfield(rsAtt,"AttNum") )                     
 
                    if cgEbenenTyp == 5: 
                        qTyp = qLayer.geometryType()
                        EZU352CEF05BE474C37B4809B26B2A75BE7 (eSymbols, symNum, db, qTyp, "line", fncfield(rsAtt,"lineattr"),Group,fncfield(rsAtt,"AttNum") )                     


                    
                    if cgEbenenTyp == 2 or cgEbenenTyp == 6: 
                        qTyp = qLayer.geometryType()


                        eSym=EZU8EE910E18038480A85D466F9C4F15D48 (eSymbols, symNum,qTyp,rsAtt)
                        
                         





                        if fncfield(rsAtt,"fslineattr1") != "{00000000-0000-0000-0000-000000000000}":
                            s1=EZU257B2E8C689B476E864807F64F1C77D7 (eSym,rsAtt,1, Group)
                            EZU352CEF05BE474C37B4809B26B2A75BE7 (None, 0,  db, qTyp, "line",fncfield(rsAtt,"fslineattr1"),Group,0,s1 )
                            if fncfield(rsAtt,"fslineattr2") != "{00000000-0000-0000-0000-000000000000}":
                                s1=EZU257B2E8C689B476E864807F64F1C77D7 (eSym,rsAtt,2, Group) 
                                EZU352CEF05BE474C37B4809B26B2A75BE7 (None, 0,  db, qTyp, "line",fncfield(rsAtt,"fslineattr2"),Group,0,s1 )



                        if fncfield(rsAtt,"pointattr1") != "{00000000-0000-0000-0000-000000000000}":

                            sWin=abs(360-fncfield(rsAtt,"alpha1"))
                            l1=EZUC7C192F1878045F492C281DD6C4D4621 (eSym,db,fncfield(rsAtt,"pointattr1"),sWin,1,   Group)
                            if fncfield(rsAtt,"pointattr2") != "{00000000-0000-0000-0000-000000000000}":
                                sWin=abs(360-fncfield(rsAtt,"alpha2"))
                                l1=EZUC7C192F1878045F492C281DD6C4D4621 (eSym,db,fncfield(rsAtt,"pointattr2"),sWin,1, Group)
                        

                        EZU352CEF05BE474C37B4809B26B2A75BE7 (None, symNum, db, qTyp, "outline", fncfield(rsAtt,"lineattr"),Group,fncfield(rsAtt,"AttNum"),eSym) 

                        


                  




        
        else:




            AktDefID = EZUAFAF458DCD164EA4A76CF69189C827B7(db, LayerID, cgUser, -1)
            AktDefName=EZUDCADB4666E944E57BEC334CD9635C33E(db, AktDefID)
            EZUECF30286359145F8A6FCFF9D953FB103( db, qLayer,AktDefID, Group)


        tree = ET.ElementTree(eRoot)
        tempName=EZUE2CC6C01835941909C82368EAB1CE1E2() + "tempName.qml"
        if myqtVersion == 5:
            f = open(tempName, "w",encoding='utf-8')
        else:
            f = open(tempName, "w")

        sXML=dom.parseString(
                    ET.tostring(
                      tree.getroot(),
                      'utf-8')).toprettyxml(indent="    ")
        if myqtVersion == 5:
            f.write(sXML)
        else:
            f.write(sXML.encode('utf8'))
        f.close()
        
        qLayer.loadNamedStyle(tempName)
        if not EZUDDCC484E3DC3474889FE69ED76A61E8F():
            try:
                os.remove(tempName)
            except:
                EZUC8DCB02F1A8145AF82C8A69A43E0529B(tr('can not remove: ') + tempName)
    
if __name__ == "__main__":
    LayerID=None
    cgEbenenTyp=None
    AktDefName=None



