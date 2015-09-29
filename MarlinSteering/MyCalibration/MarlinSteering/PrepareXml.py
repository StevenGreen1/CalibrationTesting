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


#===========================
# Input Variables
#===========================

print '===== PrepareXml.py ====='
print sys.argv

particle = sys.argv[1]
energy = sys.argv[2]
slcioTextFile = sys.argv[3]
#slcioPath = sys.argv[3] 
#slcioFormat = sys.argv[4] #'ILD_o1_v06_ENERGY_GeV_energy_PARTICLE_pdg_SN_(.*?).slcio'
gearFile = sys.argv[4]
pandoraSettingsDefault = sys.argv[5]

#===========================

jobName = energy + '_GeV_' + particle

particleNumber=''

if (particle == 'Photon'):
    particleNumber = '22'

elif (particle == 'KaonL'):
    particleNumber = '130'

elif (particle == 'Muon'):
    particleNumber = '13'

#===========================
# Calibration Numbers
#===========================
CalibrECal = sys.argv[6]
CalibrHCalBarrel = sys.argv[7]
CalibrHCalEndcap = sys.argv[8]
CalibrHCalOther = sys.argv[9]
ECalBarrelTimeWindowMax = sys.argv[10]
HCalBarrelTimeWindowMax = sys.argv[11]
ECalEndcapTimeWindowMax = sys.argv[12]
HCalEndcapTimeWindowMax = sys.argv[13]
ECalToMIP = sys.argv[14]
HCalToMIP = sys.argv[15]
MuonToMIP = sys.argv[16]
ECalMIPMPV = sys.argv[17]
HCalMIPMPV = sys.argv[18]
MHHHE = sys.argv[19]
ECalToEm = sys.argv[20]
HCalToEm = sys.argv[21]
ECalToHad = sys.argv[22]
HCalToHad = sys.argv[23]
#===========================

baseFile = os.path.join(os.getcwd(), 'ILD_o1_v06_XX_YY.xml')
baseFileName = 'ILD_o1_v06_XX_YY.xml'
marlinPath = os.getcwd() + '/../MarlinXml'
rootFilePath = os.getcwd() + '/../RootFiles'

jobList = ''

base = open(baseFile,'r')
baseContent = base.read()
base.close()

# Load slcio files
file = open(slcioTextFile, 'r')
slcioFiles = file.readlines()
slcioFiles.sort()

slcioFilesToRun = []

for slcioFile in slcioFiles:
    if (particle == 'Photon' and '22_pdg' in slcioFile) or (particle == 'KaonL' and '130_pdg' in slcioFile) or (particle == 'Muon' and '13_pdg' in slcioFile):
        slcioFilesToRun.append(slcioFile.rstrip())

print 'Slcio files to run : '
print  slcioFilesToRun

slcioFormat = 'ILD_o1_v06_CalibrationTesting_(.*?)_GeV_Energy_(.*?)_SN_(.*?).slcio'

if slcioFilesToRun:
    array_size=len(slcioFilesToRun)
    for nfiles in range (array_size):
        newContent = baseContent
        nextFile = slcioFilesToRun.pop(0)
        (nextFilePath, nextFileName) = os.path.split(nextFile)
        matchObj = re.match(slcioFormat, nextFileName, re.M|re.I)
        if matchObj:
            SN = matchObj.group(3)
            # Marlin Xml and Root File Name
            newFileName = re.sub('XX_YY',jobName + '_SN_' + SN,baseFileName)
            marlinFullPath = os.path.join(marlinPath, newFileName)
            rootFileFullPath = os.path.join(rootFilePath, 'ILD_o1_v06_' + jobName + '_SN_' + SN + '.root')

            # Root Files
            newContent = re.sub('PANDORA_SETTINGS_DEFAULT_ROOT_FILE',rootFileFullPath,newContent)

            # Pandora Settings Files
            newContent = re.sub('PANDORA_SETTINGS_DEFAULT_FILE',pandoraSettingsDefault,newContent)

            # Slcio File
            newContent = re.sub('LCIO_INPUT_FILE',nextFile,newContent)

            # Gear File
            newContent = re.sub('GEAR_FILE',gearFile,newContent)
            
            # Digitisation Constants
            newContent = re.sub('CALIBRECAL_XXXX',CalibrECal,newContent)
            newContent = re.sub('CALIBRHCALBARREL_XXXX',CalibrHCalBarrel,newContent)
            newContent = re.sub('CALIBRHCALENDCAP_XXXX',CalibrHCalEndcap,newContent)
            newContent = re.sub('CALIBRHCALOTHER_XXXX',CalibrHCalOther,newContent)
            newContent = re.sub('CALIBRMUON_XXXX','56.7',newContent)
            newContent = re.sub('ECALBARRELTIMEWINDOWMAX_XXXX',ECalBarrelTimeWindowMax,newContent)
            newContent = re.sub('HCALBARRELTIMEWINDOWMAX_XXXX',HCalBarrelTimeWindowMax,newContent)
            newContent = re.sub('ECALENDCAPTIMEWINDOWMAX_XXXX',ECalEndcapTimeWindowMax,newContent)
            newContent = re.sub('HCALENDCAPTIMEWINDOWMAX_XXXX',HCalEndcapTimeWindowMax,newContent)
            newContent = re.sub('ECALMIPMPV_XXXX',ECalMIPMPV,newContent)
            newContent = re.sub('HCALMIPMPV_XXXX',HCalMIPMPV,newContent)

            # Pandora Settings  
            newContent = re.sub('ECALTOMIP_XXXX',ECalToMIP,newContent)
            newContent = re.sub('HCALTOMIP_XXXX',HCalToMIP,newContent)
            newContent = re.sub('MUONTOMIP_XXXX',MuonToMIP,newContent)

            newContent = re.sub('MHHHE_XXXX',MHHHE,newContent)

            newContent = re.sub('ECALTOEM_XXXX',ECalToEm,newContent)
            newContent = re.sub('HCALTOEM_XXXX',HCalToEm,newContent)
            newContent = re.sub('ECALTOHAD_XXXX',ECalToHad,newContent)
            newContent = re.sub('HCALTOHAD_XXXX',HCalToHad,newContent)

            file = open(marlinFullPath,'w')
            file.write(newContent)
            file.close()
            
            jobList += marlinFullPath
            jobList += '\n'
            del newContent

runFilePath = os.getcwd() + '/Condor'
file = open(runFilePath + '/MarlinRunFile_' + jobName + '.txt','w')
file.write(jobList)
file.close()
