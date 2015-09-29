#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

allResults = open("AllResults.txt", "w")

numberOfEventsList = [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100] 

for counter in range(75):
    run = counter + 1
    allResults.write("%s\t" % run)
    numberOfEvents = numberOfEventsList[counter]
    allResults.write("%s\t" % numberOfEvents)

    resultsFilePath = '/usera/sg568/ilcsoft_v01_17_08/CalibrationTesting/MarlinSteering/CalibrationResults/Run' + str(run) + '/Final_Calibration.txt'

    calibrECal = ''
    calibrHCalBarrel = ''
    calibrHCalEndcap = ''
    calibrHCalOther = ''
    ecalGeVToMIP = ''
    hcalGeVToMIP = ''
    muonGeVToMIP = ''
    ecalMIPMPV = ''
    hcalMIPMPV = ''
    ecalToEMGeVCalibration = ''
    hcalToEMGeVCalibration = ''
    ecalToHadGeVCalibration = ''
    hcalToHadGeVCalibration = ''

    calibrationNumbers = []

    with open(resultsFilePath) as resultsFile:
        for line in resultsFile:
            if 'CalibrECAL' in line:
                words = line.split()
                calibrECal = words[5]
                calibrationNumbers.append(calibrECal)
            elif 'CalibrHCALBarrel' in line:
                words = line.split()
                calibrHCalBarrel = words[5]
                calibrationNumbers.append(calibrHCalBarrel)
            elif 'CalibrHCALEndcap' in line:
                words = line.split()
                calibrHCalEndcap = words[5]
                calibrationNumbers.append(calibrHCalEndcap)
            elif 'CalibrHCALOther' in line:
                words = line.split()
                calibrHCalOther = words[5]
                calibrationNumbers.append(calibrHCalOther)
            elif 'ECalGeVToMIP' in line:
                words = line.split()
                ecalGeVToMIP = words[5]
                calibrationNumbers.append(ecalGeVToMIP)
            elif 'HCalGeVToMIP' in line:
                words = line.split()
                hcalGeVToMIP = words[5]
                calibrationNumbers.append(hcalGeVToMIP)
            elif 'MuonGeVToMIP' in line:
                words = line.split()
                muonGeVToMIP = words[5]
                calibrationNumbers.append(muonGeVToMIP)
            elif 'ECalMIPMPV' in line:
                words = line.split()
                ecalMIPMPV = words[9]
                calibrationNumbers.append(ecalMIPMPV)
            elif 'HCalMIPMPV' in line:
                words = line.split()
                hcalMIPMPV = words[9]
                calibrationNumbers.append(hcalMIPMPV)
            elif 'ECalToEMGeVCalibration' in line:
                words = line.split()
                ecalToEMGeVCalibration = words[5]
                calibrationNumbers.append(ecalToEMGeVCalibration)
            elif 'HCalToEMGeVCalibration' in line:
                words = line.split()
                hcalToEMGeVCalibration = words[5]
                calibrationNumbers.append(hcalToEMGeVCalibration)
            elif 'ECalToHadGeVCalibration' in line:
                words = line.split()
                ecalToHadGeVCalibration = words[5]
                calibrationNumbers.append(ecalToHadGeVCalibration)
            elif 'HCalToHadGeVCalibration' in line:
                words = line.split()
                hcalToHadGeVCalibration = words[5]
                calibrationNumbers.append(hcalToHadGeVCalibration)

    print calibrationNumbers

    for item in calibrationNumbers:
        allResults.write("%s\t" % item)
    allResults.write("\n")
allResults.close()
sys.exit()

#CalibrECAL was found to be:                         1 2.0
#CalibrHCALBarrel was found to be:                   1
#CalibrHCALEndcap was found to be:                   1
#CalibrHCALOther was found to be:                    1
#ECalGeVToMIP was found to be:                       1
#HCalGeVToMIP was found to be:                       1
#MuonGeVToMIP was found to be:                       1
#HCalMIPMPV (adc not calo hit) was found to be:      1
#MaxHCalHitHadronicEnergy was found to be:           2
#ECalToEMGeVCalibration was found to be:             1
#HCalToEMGeVCalibration was found to be:             3
#ECalToHadGeVCalibration was found to be:            1
#HCalToHadGeVCalibration was found to be:            3
#ECALBarrelTimeWindowMax is:                         1
#HCALBarrelTimeWindowMax is:                         1
#ECALEndcapTimeWindowMax is:                         1
#HCALEndcapTimeWindowMax is:                         1

