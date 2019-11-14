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













import os.path
try:
    from fnc4all import *
    from fnc4CaigosConnector import *
except:
    from .fnc4all import *
    from .fnc4CaigosConnector import *
import re
import codecs


def EZUEC3EF0E87A7B41F0BCB1C49ECEEDCE0C (VerzNam, Rekursiv=False):
    try:
        if Rekursiv:
            Pfad = ""
            v=VerzNam.replace("\\","/")
            v=v.replace("//","/")
            for p in  v.split("/"):
                Pfad = Pfad  + p + "/"
                if not os.path.exists(Pfad):
                    os.makedirs(Pfad)
        else:
            if not os.path.exists(VerzNam):
                os.makedirs(VerzNam) 
        return True
    except:
        return False

    
def EZUA4E9AB9A09C14707873F50EB1D7815E2 (qDat, zDat, Fill=False):


    if not os.path.isfile(qDat): 
        EZUC8DCB02F1A8145AF82C8A69A43E0529B("CAIGOS Signatur '" + qDat + "'nicht gefunden")
        return False
    
    if (os.path.getsize(qDat) == 0): 
        EZU9AC841489FAD40E4B1A1232B3CA9B315("CAIGOS Signatur '" + qDat + "' leere Datei")
        return False    
    
    try:

        bLW = True
        sEff=""
        def korr(w0,w1): 










            if bLW:



                wt= 1.8 * float(w1)
                if wt < w/100:
                    wt=w/100
                return str(wt)
            else:








                return "1" 
            
        def neg(w, h):
            if w.find("/") != -1:
                v = w.split("/")
                d = float(v[1])
                v[1] = str(h - d)
                return "/".join(v)
            else:
                return str(h-float(w))

        

        iDatNum = EZUA4368C0FEFDC4FC1977350D9EDFD8729(qDat,"r","cp1252")
        


        oDatNum = codecs.open(zDat,"w",'utf-8')
        z=0
        sTrenn = "@"

        for iZeile in iDatNum:
            debuglog(iZeile)
            iZeile=iZeile.replace("\n","")
            if iZeile[:10] == "TOKENCHAR " : 
                sTrenn = iZeile.split()[1]
            if iZeile[:6] == "WIDTH " : 
                w = float(iZeile.split()[1])
            if iZeile[:7] == "HEIGHT " :
                h = float(iZeile.split()[1])
                oDatNum.write("<svg width='" + str(w) + "' height='" + str(h) + "' xmlns='http://www.w3.org/2000/svg'>\n")
            if iZeile[:10] == "LINEWIDTH " : 
                bLW = True if iZeile.split()[1] == "on" else False
                sEff="" if iZeile.split()[1] == "on" else "vector-effect:non-scaling-stroke;"



            if iZeile[:5] == "POLY " :
                v = iZeile.split()
                oZeile = "<polygon points='"
                for i in range(10,len(v)):
                    oZeile = oZeile + neg(v[i], h).replace( "/", ",") + " "

                oDatNum.write(oZeile.strip() + "'\n")
                oDatNum.write("style='" + sEff + "fill-opacity: " + str(abs(1 - int(v[6]))) + ";fill:rgb(" + v[7] + "," + v[8] + "," + v[9] + ");stroke-width:" + korr(w,v[1]) + ";stroke:rgb(" + v[3] + "," + v[4] + "," + v[5] + ")'\n")
                oDatNum.write(" />\n")
            

            if iZeile[:4] == "ARC " :
                v = iZeile.split()
                Fuell=v[6]
                oDatNum.write("<circle cx='" + v[10] + "' cy='" + neg(v[11], h) + "' r='" + v[12] + "'\n")                
                oDatNum.write("style='" + sEff + " fill-opacity: " + str(abs(1 - int(v[6]))) + ";fill:rgb(" + v[7] + "," + v[8] + "," + v[9] + ");stroke-width:" + korr(w,v[1]) + ";stroke:rgb(" + v[3] + "," + v[4] + "," + v[5] + ")'\n")                
                oDatNum.write("/>\n")
            

            if iZeile[:5] == "LINE " :
                v = iZeile.split()
                oDatNum.write("<line x1='" + v[6] + "' y1='" + neg(v[7], h) + "' x2='" + v[8] + "' y2='" + neg(v[9], h) + "'\n")
                oDatNum.write("style='" + sEff + "stroke-linecap:round;stroke-width:" + korr(w,v[1]) + ";stroke:rgb(" + v[3] + "," + v[4] + "," + v[5] + ")'\n")
                oDatNum.write(" />\n")
            

            if iZeile[:4] == "SEG " :
                v = iZeile.split()
                oZeile = "<polyline points='"
                for i in range(10,len(v)):
                    oZeile = oZeile + neg(v[i], h).replace( "/", ",") + " "
                oDatNum.write(oZeile.strip() + "'\n")
                oDatNum.write("style='" + sEff + "stroke-linecap:round;fill:none;stroke-width:" + korr(w,v[1]) + ";stroke:rgb(" + v[3] + "," + v[4] + "," + v[5] + ")'\n")
                oDatNum.write(" />\n")
            

            if iZeile[:5] == "TEXT " :





                v=iZeile.split(sTrenn)

                bZentr=(v[10]=='J') 
                if bZentr:
                    m=float(v[11])
                    fX= str(w/2 - m/2)


                    fY=  str(h/2 - float( v[2])/4)
                else:
                    fX= v[6]
                    fY= str(float(v[7]) - float( v[2]) * 0.9)  

                oDatNum.write("<text x='" + fX + "' y='" + neg(fY, h)  + "'\n")
                oDatNum.write(("style='font-size:%spx;font-family:%s;fill:rgb(%s,%s,%s)'") % (v[2],v[1],v[3],v[4],v[5])) 


                if myqtVersion == 5:
                    oDatNum.write(">"+v[9]+"</text>\n")
                else:
                    oDatNum.write(">"+v[9].decode("cp1252")+"</text>\n")
                

        oDatNum.write("</svg>")
        iDatNum.close()
        oDatNum.close()

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        EZU2CC2ED60E16A4317BA8BEBE4D6120301 (qDat)

    
if __name__ == "__main__":
    test='j'
    bZentr=(test=='J')
    print (bZentr)






 

