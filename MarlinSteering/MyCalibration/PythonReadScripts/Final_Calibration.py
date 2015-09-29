# -*- coding: utf-8 -*-
import os
import re
import random
import dircache
import sys

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ''

#======================
# Calibration Constants
#======================

print '===== Final_Calibration.py ====='
print sys.argv

CalibrECal_Input = sys.argv[1]
CalibrECal_Input2 = 2 * float(CalibrECal_Input)
CalibrECal = str(CalibrECal_Input) + ' ' + str(CalibrECal_Input2)
CalibrHCalBarrel = sys.argv[2]
CalibrHCalEndCap = sys.argv[3]
CalibrHCalOther = sys.argv[4]
CalibrMuon = '56.7'
ECALBarrelTimeWindowMax = sys.argv[5]
HCALBarrelTimeWindowMax = sys.argv[6]
ECALEndcapTimeWindowMax = sys.argv[7]
HCALEndcapTimeWindowMax = sys.argv[8]

ECalGeVToMIP = sys.argv[9]
HCalGeVToMIP = sys.argv[10]
MuonGeVToMIP = sys.argv[11]
ECalMIPMPV = sys.argv[12]
HCalMIPMPV = sys.argv[13]

MHHHE = sys.argv[14]

ECalToEm = sys.argv[15]
HCalToEm = sys.argv[16]
ECalToHad = sys.argv[17]
HCalToHad = sys.argv[18]

#======================
# Output Path
#======================

outputPath = sys.argv[19]

#======================

outputString = ''

outputString += 'CalibrECAL was found to be:                         '
outputString += str(CalibrECal) + '\n'

outputString += 'CalibrHCALBarrel was found to be:                   '
outputString += str(CalibrHCalBarrel) + '\n'

outputString += 'CalibrHCALEndcap was found to be:                   '
outputString += str(CalibrHCalEndCap) + '\n'

outputString += 'CalibrHCALOther was found to be:                    '
outputString += str(CalibrHCalOther) + '\n'

outputString += 'ECalGeVToMIP was found to be:                       '
outputString += str(ECalGeVToMIP) + '\n'

outputString += 'HCalGeVToMIP was found to be:                       '
outputString += str(HCalGeVToMIP) + '\n'

outputString += 'MuonGeVToMIP was found to be:                       '
outputString += str(MuonGeVToMIP) + '\n'

outputString += 'ECalMIPMPV (adc not calo hit) was found to be:      '
outputString += str(ECalMIPMPV) + '\n'

outputString += 'HCalMIPMPV (adc not calo hit) was found to be:      '
outputString += str(HCalMIPMPV) + '\n'

outputString += 'MaxHCalHitHadronicEnergy was found to be:           '
outputString += str(MHHHE) + '\n'

outputString += 'ECalToEMGeVCalibration was found to be:             '
outputString += str(ECalToEm) + '\n'

outputString += 'HCalToEMGeVCalibration was found to be:             '
outputString += str(HCalToEm) + '\n'

outputString += 'ECalToHadGeVCalibration was found to be:            '
outputString += str(ECalToHad) + '\n'

outputString += 'HCalToHadGeVCalibration was found to be:            '
outputString += str(HCalToHad) + '\n'

outputString += 'ECALBarrelTimeWindowMax is:                         '
outputString += str(ECALBarrelTimeWindowMax) + '\n'

outputString += 'HCALBarrelTimeWindowMax is:                         '
outputString += str(HCALBarrelTimeWindowMax) + '\n'

outputString += 'ECALEndcapTimeWindowMax is:                         '
outputString += str(ECALEndcapTimeWindowMax) + '\n'

outputString += 'HCALEndcapTimeWindowMax is:                         '
outputString += str(HCALEndcapTimeWindowMax) + '\n'

outputFile = os.path.join(outputPath,'Final_Calibration.txt')
file = open(outputFile,'w')
file.write(outputString)
file.close()
