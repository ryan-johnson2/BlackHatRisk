from lea import *
from WirelessAlgorithm import * 
from link import *

class BayesLink:
    
    def __init__(self, link):
        self._link = link
        self._intialLinkRisk = wirelessAlgorithm(self._link)
        self._intialAdversaryRisk = .999 #adversaryAlgorithm(***some input***)


        #TODO
        '''
        import tucker's algo, and update within the xml for the comms network
        create lea bool value for that
        [not yet capable] import the adversary risk value from davids alorithm
        to manually modify tuckers algorithm, values can be placed in a text file and imported
        same for David's
        both david and tucker's algo will be first two nodes, of boolean value
        then boolean node for adversary monitoring(fed by adversary capabilites and time of day), followed by comms detected node.
        This feeds to comms IDed as subversive, with another input of amount of similar traffic (high, medium, low may be best)
        this breaks into risk value
        question remains: how to display the value


        Steps: 
        1. [x]Alter tuckers algo to allow values from external source 
        2. []modify links in gui[] and xml/link class [x]
        3. [x]import value from tucker's algo
        4. []rinse, lather, repeat with davids algo
        5. []create lea nodes with both algos
        6. []create model in agenaRisk to confirm results
        6. []create rest of bayes network
        7. []interpret output values



'''
    def showLinkRisk(self):
        print self._intialLinkRisk

    def showTotalRisk(self):
        linkRiskToInt = int(self._intialLinkRisk*1000)
        adversaryRiskToInt = int(self._intialAdversaryRisk*1000)
        bayesAdversaryRisk = Lea.boolProb(adversaryRiskToInt, 1000)
        bayesLinkRisk = Lea.boolProb(linkRiskToInt, 1000)
        #print bayesLinkRisk
        commsDetected = Lea.buildCPT((bayesLinkRisk & ~bayesAdversaryRisk, Lea.boolProb(min(linkRiskToInt+10, 1000), 1000)), (bayesLinkRisk & bayesAdversaryRisk, Lea.boolProb(95,100)), (~bayesLinkRisk & ~bayesAdversaryRisk, False), (~bayesLinkRisk & bayesAdversaryRisk, Lea.boolProb(1,100)))
        print commsDetected
   

def test():
    testLink = Link("n1", "n2", "test1", "802.11A", 256, 1024, "WPA", True)     
    #(self, node1, node2, name, protocol, sizeOfData, maxFileSize, linkSecurity, peakHours, risk = -1)
    testLink.addAdditional("numberOfUsers", 100)
    testLink.addAdditional("dataIsSimiliar", True)
    testLink.addAdditional("scanTime", 800)
    testLink.addAdditional("isScanning", True)
    #{numberOfUsers, dataIsSimiliar, scanTime, isScanning}
    testBayes = BayesLink(testLink)
    #testBayes.showLinkRisk()
    testBayes.showTotalRisk()
    testLink2 = Link("n1", "n2", "test2", "802.11A", 1025, 1024, "WEP", True)     
    #(self, node1, node2, name, protocol, sizeOfData, maxFileSize, linkSecurity, peakHours, risk = -1)
    testLink2.addAdditional("numberOfUsers", 3)
    testLink2.addAdditional("dataIsSimiliar", False)
    testLink2.addAdditional("scanTime", 800)
    testLink2.addAdditional("isScanning", True)
    #{numberOfUsers, dataIsSimiliar, scanTime, isScanning}
    testBayes2 = BayesLink(testLink2)
    #testBayes2.showLinkRisk()
    testBayes2.showTotalRisk()