#include <vector>
#include <algorithm> 
#ifdef __CINT__
#pragma link C++ class vector<vector<float> >;
#endif

void makeGraph(std::vector<int> eventsVector, std::vector<float> vectorOfInterest, std::string description);

void Analyse()
{
    gROOT->SetStyle("Plain");
    gStyle->SetPadTickX(1);
    gStyle->SetPadTickY(1);
    gStyle->SetPadTopMargin(0.05);
    gStyle->SetPadRightMargin(0.05);
    gStyle->SetPadBottomMargin(0.10);
    gStyle->SetPadLeftMargin(0.10);
    gStyle->SetOptStat(0);
    gStyle->SetOptTitle(0);
    TGaxis::SetMaxDigits(7);

    std::string resultsFile = "AllResults.txt";
    std::ifstream myReadFile;
    myReadFile.open(resultsFile.c_str());

    float run, events, calibrECal, calibrHCalBarrel, calibrHCalEndcap, calibrHCalOther, ecalGeVToMIP, hcalGeVToMIP, muonGeVToMIP, ecalMIPMPV, hcalMIPMPV, ecalToEMGeVCalibration, hcalToEMGeVCalibration, ecalToHadGeVCalibration, hcalToHadGeVCalibration;

    std::vector<int> runVector, eventsVector;
    std::vector<float> runVectorFloat, eventsVectorFloat, calibrECalVector, calibrHCalBarrelVector, calibrHCalEndcapVector, calibrHCalOtherVector, ecalGeVToMIPVector, hcalGeVToMIPVector, muonGeVToMIPVector, ecalMIPMPVVector, hcalMIPMPVVector, ecalToEMGeVCalibrationVector, hcalToEMGeVCalibrationVector, ecalToHadGeVCalibrationVector, hcalToHadGeVCalibrationVector;

    while (myReadFile >> run >> events >> calibrECal >> calibrHCalBarrel >> calibrHCalEndcap >> calibrHCalOther >> ecalGeVToMIP >> hcalGeVToMIP >> muonGeVToMIP >> ecalMIPMPV >> hcalMIPMPV >> ecalToEMGeVCalibration >> hcalToEMGeVCalibration >> ecalToHadGeVCalibration >> hcalToHadGeVCalibration)
    {
        runVector.push_back(floor(run + 0.5));
        runVectorFloat.push_back(run);
        eventsVector.push_back(floor(events + 0.5));
        eventsVectorFloat.push_back(events);
        calibrECalVector.push_back(calibrECal); 
        calibrHCalBarrelVector.push_back(calibrHCalBarrel); 
        calibrHCalEndcapVector.push_back(calibrHCalEndcap); 
        calibrHCalOtherVector.push_back(calibrHCalOther); 
        ecalGeVToMIPVector.push_back(ecalGeVToMIP); 
        hcalGeVToMIPVector.push_back(hcalGeVToMIP); 
        muonGeVToMIPVector.push_back(muonGeVToMIP); 
        ecalMIPMPVVector.push_back(ecalMIPMPV);
        hcalMIPMPVVector.push_back(hcalMIPMPV);
        ecalToEMGeVCalibrationVector.push_back(ecalToEMGeVCalibration);
        hcalToEMGeVCalibrationVector.push_back(hcalToEMGeVCalibration);
        ecalToHadGeVCalibrationVector.push_back(ecalToHadGeVCalibration);
        hcalToHadGeVCalibrationVector.push_back(hcalToHadGeVCalibration);
    }

    std::vector<float> averageCalibrECal;

    std::vector<int> uniqueEventCounter;

    makeGraph(eventsVector, calibrECalVector, "Digitisation Constant ECal");
    makeGraph(eventsVector, calibrHCalBarrelVector, "Digitisation Constant HCal Barrel");
    makeGraph(eventsVector, calibrHCalEndcapVector, "Digitisation Constant HCal Endcap");
    makeGraph(eventsVector, calibrHCalOtherVector, "Digitisation Constant HCal Other");
    makeGraph(eventsVector, ecalGeVToMIPVector, "MIP Scale Pandora ECal");
    makeGraph(eventsVector, hcalGeVToMIPVector, "MIP Scale Pandora HCal");
    makeGraph(eventsVector, muonGeVToMIPVector, "MIP Scale Pandora Muon Chamber");
    makeGraph(eventsVector, ecalMIPMPVVector, "MIP Scale Digitiser ECal");
    makeGraph(eventsVector, hcalMIPMPVVector, "MIP Scale Digitiser HCal");
    makeGraph(eventsVector, ecalToEMGeVCalibrationVector, "EM Scale Pandora ECal");
    makeGraph(eventsVector, hcalToEMGeVCalibrationVector, "EM Scale Pandora HCal");
    makeGraph(eventsVector, ecalToHadGeVCalibrationVector, "Had Scale Pandora ECal");
    makeGraph(eventsVector, hcalToHadGeVCalibrationVector, "Had Scale Pandora HCal");

    //pTGraphErrors->Draw("APL");
/*
    for (vector<int>::iterator it = eventsVector.begin(); it != eventsVector.end(); ++it)
    {
        int eventsNumber = *it;
        
        
    }


    TVectorT<float> tVectorRun(runVectorFloat.size(), &runVectorFloat[0]);
    TVectorT<float> tVectorEvents(eventsVectorFloat.size(), &eventsVectorFloat[0]);
    TVectorT<float> tVectorCalibrECal(calibrECalVector.size(), &calibrECalVector[0]);
    
    TGraph *pTGraph = new TGraph (tVectorEvents,tVectorCalibrECal);
//    pTGraph->SetLineColor(2);
    pTGraph->SetMarkerColor(2);
    pTGraph->SetMarkerStyle(20);
    pTGraph->SetTitle("");
    pTGraph->GetXaxis()->SetTitle("Number Of Events Used In Calibration");
    pTGraph->GetXaxis()->SetLimits(0.0,105.0);
    pTGraph->GetXaxis()->SetRangeUser(0.0,105.0);
    pTGraph->GetYaxis()->SetTitle("CalibrECal");

    TCanvas *pCanvas = new TCanvas("Name","Title",200,10,600,500);
    pCanvas->cd();
    pTGraph->Draw("AP");*/
}

//===========

void makeGraph(std::vector<int> eventsVector, std::vector<float> vectorOfInterest, std::string description)
{
    TGraphErrors *pTGraphErrors = new TGraphErrors();
    TGraphErrors *pTGraphErrorsFrac = new TGraphErrors();

    std::vector<int> uniqueEventNumber;
    std::vector<std::vector<float> > groupedVector;  

    for (std::vector<int>::iterator it = eventsVector.begin(); it != eventsVector.end(); ++it)
    {
        int eventsNumber = *it;
        int position = it - eventsVector.begin();
        float value = vectorOfInterest.at(position);

        if (std::find(uniqueEventNumber.begin(), uniqueEventNumber.end(), eventsNumber) != uniqueEventNumber.end())
        {
            int index = std::find(uniqueEventNumber.begin(), uniqueEventNumber.end(), eventsNumber) - uniqueEventNumber.begin();
            groupedVector.at(index).push_back(value);
        }
        else
        {
            std::vector<float> toPushBack;
            toPushBack.push_back(value);
            groupedVector.push_back(toPushBack);
            uniqueEventNumber.push_back(eventsNumber);
        }
    }

    float bestEstimate(0.f);
    int largestEventNumber(0);
    for (std::vector<int>::iterator it = uniqueEventNumber.begin(); it != uniqueEventNumber.end(); ++it)
    {
        int eventsNumber = *it;
        if (eventsNumber > largestEventNumber)
        {
            largestEventNumber = eventsNumber;
            float sum (0.f);
            int index = std::find(uniqueEventNumber.begin(), uniqueEventNumber.end(), eventsNumber) - uniqueEventNumber.begin();
            for (std::vector<float>::iterator iter = groupedVector.at(index).begin(); iter != groupedVector.at(index).end(); ++iter)
            {
                sum += *iter;
            }
            bestEstimate = sum / (float)(groupedVector.at(index).size());
        }
    }

    for (std::vector<int>::iterator it = uniqueEventNumber.begin(); it != uniqueEventNumber.end(); ++it)
    {
        int eventsNumber = *it;
        int position = it - uniqueEventNumber.begin();
        std::vector<float> values;
        values = groupedVector.at(position);

//        for (int i = 0; i < values.size(); i++)
//        {
//            std::cout << values.at(i) << std::endl;
//        }

        float sum(0.f);
        for (std::vector<float>::iterator iter = values.begin(); iter != values.end(); ++iter)
        {
            float currentValue = *iter;
            sum += currentValue;
        }
        float mean = sum / (float)(values.size());

        float rmsSum(0.f);
        for (std::vector<float>::iterator iter = values.begin(); iter != values.end(); ++iter)
        {
            rmsSum += pow((*iter) - mean,2);
        }
        float rms = pow(rmsSum,0.5) / (float)(values.size());

        int pointsInGraph = pTGraphErrors->GetN();
//        std::cout << "Mean : " << mean << std::endl;
//        std::cout << "RMS  : " << rms << std::endl;
        pTGraphErrors->SetPoint(pointsInGraph,(eventsNumber*1000),mean);
        pTGraphErrors->SetPointError(pointsInGraph,0.f,rms);
        pTGraphErrorsFrac->SetPoint(pointsInGraph,(eventsNumber*1000),((mean - bestEstimate) / bestEstimate));
        // Please do full error analysis here.
        pTGraphErrorsFrac->SetPointError(pointsInGraph,0.f,0.f);
    }

    TCanvas *pTCanvas = new TCanvas("Name", "Title", 500, 600);
    pTCanvas->Divide(1,2);
    pTCanvas->cd(1);

    pTGraphErrors->GetXaxis()->SetTitle("Number of Events Used in Calibration");
    pTGraphErrors->GetYaxis()->SetTitle(description.c_str());
    pTGraphErrors->GetYaxis()->SetTitleOffset(1.25);
    pTGraphErrors->SetMarkerStyle(4);
    pTGraphErrors->Draw("APL");

    pTCanvas->cd(2);
    pTGraphErrorsFrac->GetXaxis()->SetTitle("Number of Events Used in Calibration");
    std::string fracLabel = "Fractional " + description;
    pTGraphErrorsFrac->GetYaxis()->SetTitle(fracLabel.c_str());
    pTGraphErrorsFrac->GetYaxis()->SetTitleOffset(1.25);
    pTGraphErrorsFrac->Draw("APL");

    std::string fileName = description;
    for(int i=0; i<fileName.length(); i++)
    {
        if(fileName[i] == ' ') 
        {
            fileName.erase(i,1);
        }
    }
    fileName = fileName + ".png";
    pTCanvas->SaveAs(fileName.c_str());
}
