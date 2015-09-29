#!/bin/bash
#==================================
# 
# Script deigned to run the MyCalibration procedure using a different number of slcio files.  The slcio files are selected randomly and a text file contining the exact files used
# is stored for future reference.
#
#==================================

# Reconstruction parameters
MHHHE="1.0"
ECalBarrelTimeWindowMax="1000000.0"
HCalBarrelTimeWindowMax="1000000.0"
ECalEndcapTimeWindowMax="1000000.0"
HCalEndcapTimeWindowMax="1000000.0"

# Detector parameters
numberOfHCalLayers="48"

# File storage information
generalSlcioPath="/r06/lc/sg568/CalibrationAnalysis/Slcio/"
gearFile="/r06/lc/sg568/CalibrationAnalysis/GearFile/ILD_o1_v06_CalibrationTesting.gear"
slcioFilesUsedRepository="/usera/sg568/ilcsoft_v01_17_08/CalibrationTesting/MarlinSteering/SlcioFileListRepository/"
pandoraSettingsFile="/usera/sg568/ilcsoft_v01_17_08/CalibrationTesting/MarlinSteering/MyCalibration/PandoraSettingsFiles/PandoraSettingsDefault.xml"

# Run
counter=26

# Loop over total number of files you want to run for calibration 
for i in 5 5 5 5 5 10 10 10 10 10 20 20 20 20 20 50 50 50 50 50 100 100 100 100 100 5 5 5 5 5 10 10 10 10 10 20 20 20 20 20 50 50 50 50 50 100 100 100 100 100
do
    cd ${slcioFilesUsedRepository}
    slcioFiles="${slcioFilesUsedRepository}SlcioFiles_Run${counter}_${i}FilesUsed.txt"

    # Define the kaon0L samples to use
    kaon0LSlcioPath="${generalSlcioPath}Kaon0L/"
    ls "${kaon0LSlcioPath}" | grep 130_pdg | sort -R | tail -${i} > tmpKaon0L.txt
    sed 's|^|'${kaon0LSlcioPath}'|' tmpKaon0L.txt >> ${slcioFiles}
    rm tmpKaon0L.txt

    # Define the photon samples to use
    photonSlcioPath="${generalSlcioPath}Photon/"
    ls "${photonSlcioPath}" | grep 22_pdg | sort -R | tail -${i} > tmpPhoton.txt
    sed 's|^|'${photonSlcioPath}'|' tmpPhoton.txt >> ${slcioFiles}
    rm tmpPhoton.txt

    # Define the muon samples to use
    muonSlcioPath="${generalSlcioPath}Muon/"
    ls "${muonSlcioPath}" | grep 13_pdg | sort -R | tail -${i} > tmpMuon.txt
    sed 's|^|'${muonSlcioPath}'|' tmpMuon.txt >> ${slcioFiles}
    rm tmpMuon.txt

    cd ..

    # Run the calibration script
    calibrationResultsPath="/usera/sg568/ilcsoft_v01_17_08/CalibrationTesting/MarlinSteering/CalibrationResults/Run${counter}/"
    mkdir ${calibrationResultsPath}
    cd MyCalibration
    ./Calibrate.sh "${slcioFiles}" "${gearFile}" "${calibrationResultsPath}" "${pandoraSettingsFile}" "${MHHHE}" "${numberOfHCalLayers}" "${ECalBarrelTimeWindowMax}" "${HCalBarrelTimeWindowMax}" "${ECalEndcapTimeWindowMax}" "${HCalEndcapTimeWindowMax}"
    cd ..

    counter=$[$counter +1]
done
