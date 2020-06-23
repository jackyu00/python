import glob
from operator import itemgetter
from itertools import *
def missingFrameFormat(inputList):
    outList=[]
    for k, g in groupby(enumerate(inputList), lambda x:x[0]-x[1]):
        group = list(map(itemgetter(1), g))
        outList.append((group[0], group[-1]))
    return outList
    
target_path = 'X:/FOAU/iRide/mainShow/code/footage/5.7k/full/*'

all_files = glob.glob(target_path)
rangeSerial = range(0,21264)


count = 0
fc = []
for a in all_files:
	serial = a.split('_')[-1].split('.')[0]
	fc.append(int(serial))

missing = list(set(rangeSerial)-set(fc))

print missingFrameFormat(missing)


