# -*- coding: UTF-8 -*-

from multiprocessing import Pool, TimeoutError
import time
import os, shutil
import subprocess 
import locale

#sourceFo = '//10.100.10.69/媒體設計專區/媒體設計部/Film Project/P0004_i-Ride Australia/Master/Video/full/tiffirideaus_00000_18600/'
sourceFo = '//10.100.10.69/媒體設計專區/媒體設計部/Film Project/P0004_i-Ride Australia/Master/Video/tiff_4K/'
sourceFo = unicode(sourceFo , "utf8")

outputFo = '//10.100.10.73/Project/FOAU/iRide/mainShow/code/footage/5.7k/full_imagemagick/'
masterFo = '//10.100.10.73/Project/FOAU/iRide/mainShow/code/footage/5.7k/master_imagemagick/'
slaveFo = '//10.100.10.73/Project/FOAU/iRide/mainShow/code/footage/5.7k/slave_imagemagick/'

#prefix= 'FOCH_iRideMainShow_v002.' 
prefix= 'FOAU_iRideMainShow_v001.'
suffix = '.tif' 

#fPreFix = 'FOCH_iRideMainShow_v002_'
fPreFix = 'irideaus_'
fSuffix = '.tiff'

converC = '//10.100.10.73/Utility/imagemagick/magick.exe'

totalF = 18600 
#for i in range(3000, 3100):
#for i in range(0, int(totalF * 0.5)):
#for i in range(int(totalF * 0.5), totalF):
for i in range(19932, 21264):
    n = i 
    imageN = str(n).zfill(5)
    print 'processing on the %s file'%imageN
    srcFile = sourceFo + prefix + imageN + suffix
    desFile = outputFo + fPreFix + imageN + fSuffix
    scaleOp = ' -quality 100 -resize 8192x4320 -depth 8 -type trueColor -compress "none" '
    #step 1, scale to 8192*4320
    cmdS = '"' + converC + '" "' + srcFile + '"'  + scaleOp +  '"' + desFile + '"' 

    cmdS = cmdS.encode(locale.getdefaultlocale()[1])
    subprocess.call(cmdS, shell = True)
 
    #step 2, crop to left side(master)
    masterCropOps = ' -crop 3840x4320+1216+0' + ' +repage -depth 8 -type trueColor -compress "none" '
    masterDesFile = masterFo + fPreFix + imageN + fSuffix
    
    cmdS = converC + ' "' + desFile + '" ' +  masterCropOps  + '"' + masterDesFile + '"' 
    cmdS = cmdS.encode(locale.getdefaultlocale()[1])
    subprocess.call(cmdS, shell = True)
 
    #step 3, crop to right side(slave)
    slaveCropOps = ' -crop 3840x4320+3136+0' + ' +repage -depth 8 -type trueColor -compress "none" '
    slaveDesFile = slaveFo + fPreFix + imageN + fSuffix
    
    cmdS = converC + ' "' + desFile + '" ' +  slaveCropOps  + '"' + slaveDesFile + '"' 
    cmdS = cmdS.encode(locale.getdefaultlocale()[1])
    subprocess.call(cmdS, shell = True)
    


#"//10.100.10.73/Utility/imagemagick/magick.exe" "//10.100.10.69/媒體設計專區/媒體設計部/Film Project/P0004_i-Ride Australia/Master/Video/full/tiffirideaus_00000_18600/irideaus_02580.tif" -quality 100 -resize 8192x4320  "//10.100.10.73/Project/FOAU/iRide/mainShow/code/footage/5.7k/full_imagemagick/irideaus_02580.tiff"