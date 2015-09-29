#!/usr/bin/env python

from DIRAC.Core.Base import Script
Script.parseCommandLine()
 
#----------------------------------------------------------------------------------------------------
# User Input
#----------------------------------------------------------------------------------------------------

mokkaVersion    = '0804'
jobGroup        = 'HCalStudiessg568'

detectorModel   = 'ILD_o1_v06'
physicsList     = 'QGSP_BERT'
eventsPerJob    = 1000
geometry="""
"""
# My own HEPEvt files have been uploaded for the single particle energies
eventsToSimulate = [ #{ 'EventType': "Kaon0L"  , 'Energies':  [20]                                },  
                     #{ 'EventType': "Z_uds"   , 'Energies':  [91, 200, 360, 500, 1000]           },
                     { 'EventType': "Photon"  , 'Energies':  [10]                                },
                     { 'EventType': "Muon"    , 'Energies':  [10]                                }
                     #{ 'EventType': "Z_uds"   , 'Energies':  [750, 2000, 3000]                   }
                   ]

# Defaults
defaultHCalAbsorberMaterial         = 'Iron'        # or 'WMod'
defaultNumberHCalLayers             = 48            #
defaultHCalCellSize                 = 30            #
defaultHCalAbsorberLayerThickness   = 20            #
defaultHCalSCintillatorThickness    = 3             #
defaultCoilExtraSize                = 1522          #
defaultDetailedShowerMode           = 'true'        #
defaultBField                       = 3.5           # Strength of B field in tracker
defaultTPCOuterRadius               = 1808          # Outer radius of the tracker/ inner radius of the ECal

identifier = "CalibrationTesting"

from HCalStudiesCalibration import HCalSubmission
    
myJobs = HCalSubmission(MokkaVersion=mokkaVersion,
                    JobIdentificationString=jobGroup,
                    EventsPerJob=eventsPerJob,
                    GeometryAdaption=geometry,
                    EventSelection=eventsToSimulate,
                    MaxNumberOfJobs=-1,
                    PhysicsList = physicsList,
                    HCalAbsorberMaterial = defaultHCalAbsorberMaterial,
                    HCalAbsorberLayerThickness = defaultHCalAbsorberLayerThickness,
                    HCalScintillatorThickness = defaultHCalSCintillatorThickness,
                    CoilExtraSize = defaultCoilExtraSize,
                    DetailedShowerMode = defaultDetailedShowerMode,
                    Identifier = identifier,
                    NumberHCalLayers = defaultNumberHCalLayers,
                    HCalCellSize = defaultHCalCellSize,
                    BField = defaultBField,
                    TPCOuterRadius = defaultTPCOuterRadius,
                    DetectorModel = detectorModel
                    )

myJobs.submitJobs()

#----------------------------------------------------------------------------------------------------
# End User Input
#----------------------------------------------------------------------------------------------------
