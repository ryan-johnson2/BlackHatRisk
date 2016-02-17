from Lea import *
from WirelessAlgorithm import * 
from link import *

class bayesLink:
    
    def __init__(self, link):
        self._link = link
        self._intialRisk = WirelessAlgorithm.wirelessAlgorithm(self._link)


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
        6. []create rest of bayes network
        7. []interpret output values



'''

        