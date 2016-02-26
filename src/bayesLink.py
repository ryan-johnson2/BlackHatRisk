from lea import *
from WirelessAlgorithm import * 
from link import *
import random


#********************THIS IS A WORK IN PROGRESS


class BayesLink:
    
    def __init__(self, link):
        self._link = link
        self._intialLinkRisk = wirelessAlgorithm(self._link)
        self._intialAdversaryRisk = .8 #adversaryAlgorithm(***some input***)


        #TODO
        '''
        Steps: 
        1. [x]Alter tuckers algo to allow values from external source 
        2. []modify links in gui[] and xml/link class [x]
        3. [x]import value from tucker's algo
        4. []rinse, lather, repeat with davids algo
        5. [x]create lea nodes with both algos
        6. []create model in agenaRisk to confirm results
        6. []create rest of bayes network
        7. [x]interpret output values



'''
    def showLinkRisk(self):
        print self._intialLinkRisk

    def showTotalRisk(self):
        if self._intialLinkRisk == -1: 
            print 0
            return 0
        linkRiskToInt = int(self._intialLinkRisk*1000)
        adversaryRiskToInt = int(self._intialAdversaryRisk*1000)
        bayesAdversaryRisk = Lea.boolProb(adversaryRiskToInt, 1000)
        bayesLinkRisk = Lea.boolProb(linkRiskToInt, 1000)
        randomScan = min(abs(random.normalvariate(500,100)),1000)
        #random risk of being detected at a given chance.  Gives a random value between 0 and 1000 with a mean of 500 and standard variation of 100 
        riskAdversaryScanning = Lea.boolProb(int(randomScan), 1000)
        combinedRisk = Lea.buildCPT((bayesLinkRisk & ~bayesAdversaryRisk, Lea.boolProb(min(linkRiskToInt+30, 1000), 1000)), (bayesLinkRisk & bayesAdversaryRisk, Lea.boolProb(95,100)), (~bayesLinkRisk & ~bayesAdversaryRisk, False), (~bayesLinkRisk & bayesAdversaryRisk, Lea.boolProb(15,100)))
        #compares values given a true or false value of the variables and gives that result a boolean probability.
        #factor in number of users
        commsDetected = Lea.buildCPT((~combinedRisk & riskAdversaryScanning, Lea.boolProb(25,100)), (~combinedRisk & ~riskAdversaryScanning, False), (combinedRisk & ~riskAdversaryScanning, Lea.boolProb(min(linkRiskToInt+10, 1000), 1000)), (combinedRisk & riskAdversaryScanning, Lea.boolProb(95,100)))
        print commsDetected.pmf(True)
   

#use a for loop and change adversary value   

def test():
    testLink = Link("n1", "n2", "test1", "802.11A", 2048, 2048, "WPA", True)     
    #(self, node1, node2, name, protocol, sizeOfData, maxFileSize, linkSecurity, peakHours, risk = -1)
    testLink.addAdditional("numberOfUsers", 100)
    testLink.addAdditional("dataIsSimiliar", True)
    testLink.addAdditional("scanTime", 800)
    testLink.addAdditional("isScanning", True)
    #{numberOfUsers, dataIsSimiliar, isScanning}
    testBayes = BayesLink(testLink)
    #testBayes.showLinkRisk()
    print "Test Link one"
    testBayes.showTotalRisk()

    testLink2 = Link("n1", "n2", "test2", "802.11A", 1025, 1024, "WEP", True)     
    #(self, node1, node2, name, protocol, sizeOfData, maxFileSize, linkSecurity, peakHours, risk = -1)
    testLink2.addAdditional("numberOfUsers", 3)
    testLink2.addAdditional("dataIsSimiliar", True)
    testLink2.addAdditional("isScanning", True)
    #{numberOfUsers, dataIsSimiliar, isScanning}
    testBayes2 = BayesLink(testLink2)
    #testBayes2.showLinkRisk()
    print "\nTest Link 2 same as test 1 but with WEP security, result should be significantly higher than test 1"
    testBayes2.showTotalRisk()

    testLink3 = Link("n1", "n2", "test2", "802.11A", 256, 1024, "WEP", True)     
    #(self, node1, node2, name, protocol, sizeOfData, maxFileSize, linkSecurity, peakHours, risk = -1)
    testLink3.addAdditional("numberOfUsers", 100)
    testLink3.addAdditional("dataIsSimiliar", True)
    testLink3.addAdditional("isScanning", False)
    #{numberOfUsers, dataIsSimiliar, isScanning}
    testBayes3 = BayesLink(testLink3)
    #testBayes2.showLinkRisk()
    print "\nTests isScanning = false  should return 0"
    testBayes3.showTotalRisk()

    testLink4 = Link("n1", "n2", "test1", "802.11B", 2048, 2048, "WPA", True)     
    #(self, node1, node2, name, protocol, sizeOfData, maxFileSize, linkSecurity, peakHours, risk = -1)
    testLink4.addAdditional("numberOfUsers", 100)
    testLink4.addAdditional("dataIsSimiliar", True)
    testLink4.addAdditional("scanTime", 800)
    testLink4.addAdditional("isScanning", True)
    #{numberOfUsers, dataIsSimiliar, isScanning}
    testBayes4 = BayesLink(testLink4)
    #testBayes4.showLinkRisk()
    print "\nTest Link four, should be higher than test 1"
    testBayes4.showTotalRisk()