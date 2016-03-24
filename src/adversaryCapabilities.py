from link import * 
#Bud is using Lea to conduct probabilistic math
    #//update// nope, not using Lea anymore because it is stupid slow 20MAR2016

#Algorithm for Cacluation Adversary Capabilites Risks

"""
TO DO:
    - Allow the user to input values pretaining to the capabilities of adversaries
    - If no input given, generate randomly distrubted capabilities values
    - Have these values reflect real-life scenarios
    - Testing suite to ensure algorithm supports all valid inputs
"""

"""
    Assumptions:
     - Target has some form of network set up with valuable information the host wishes to preserve and/or deny from public access

    Considerations:
    - How will we be able to accurately assess HUMINT factors of the network? How do we integrate this information with the algorithm itself?
    - Calibrations and standardization of numerical values to be of significance. 0-1.000

"""

def obtainCapabilitiesConfig(): #user specifies a file outline adversary capabilities
    configFile = input('Enter Adversary ConfigFile: ')
    print('Adversary ConfigFile at: ' + configFile)

"""
Considerations 2: Adversary Capabilities are based off of two major factors SIGINT as the latent capabilities of our adversary. HUMINT as a multiplying factor (which could be anything from 0-inifinity) that can either hinder or increase the effectivness/efficiency at which exploitation has been comprimised

*note* with the current implementation, we are assuming that the adversary is using only one layer of IDS. As a result, this IDS schema will be applied at the outermost portion of the network with uniform rules applied to the entire network. This is operating with the assumption that the network we are exploiting from is large enough that smaller and more less strict IDS rule set become "statistically insignificant" when juxtapose with more strict IDS rules
"""
print('starting up adverse capability...')
SIGINT_RiskValue = 1.00    ##SIGINT Factors##
trans_type = "undefined"    #Type of Transmission
                                #Divide calculations into separate transmissions and have the ability to assign specific values of enemy capabilities.
trans_ConfigFile = "transmission_config.txt"    #configuration file with specified transmition infrastructure detection config. In this file, we will mostly likely just store "true/false" values whether or not IDS is implemented on that transmission

IDS_isOn = True             #Infrastructure set for dection (is there an IDS?)
CyberSecTeam_isActive = True#Is there a CySec Team, real humans looking at network security?

specialRulesFile = "specialRulesFile.txt"       #What IDS rules are there? Special option for later
IDS_strictness = 0.005      #some arbituary value to be further determined by parsing/considering 'specialRules'
IDS_RiskValue = 1.00

sizeOfTarget = 1.00            #number of nodes to secure in network
advrsy_NetworkMapValue = 1.00  #Adversary Mapping Capabilities/Limits Net Value, the likelihood it to be 100% perfect
advrsy_OutdoorMapValue = True        #Have they mapped outdoors perimeter?
advrsy_IndoorMapValue = True         #Have they mapped within perimeter?
indoorMap_completed = 0.01            #How much of the network has been mapped? (percentage)
outdorMap_completed = 1.00
### postponed for future considerations               #man-hours
### postponed for future considerations               #IT Level?
mapAccuracyValue_open = 1.00            #How accurate is the map? (ratio between open/closed)
mapAccuracyValue_closed = 1.00
mapValue_open = 1.00                  #public open source network map (measured by number of nodes?)
mapValue_close = 1.00                 #private closed internal map
mapValue_lastUpdate_open = 1.00            #Last network map update (time since last update)
mapValue_lastUpdate_closed = 1.0

HUMINT_RiskValue = 1.00    ##HUMINT Factors##
languageLimits = False    #Does a language barrier exist in interpreting data?
numSupport = 17.    #How many people are on NetworkSec/IT Team
last_spyCaught = 200.0   #date
num_spyDeployed = 100.0
num_spyCaught = 2.0
advrsy_HUMthreatValue = 0.01    #this is kept separate from the rest of the threatValue because it because too complicated trying to decide whether SIGINT drives HUMINT or HUMINT triggers SIGINT. We are going to assume they are spontaneous and there for mutually exclusive.

### postponed for future considerations         #budgetEconomies
### postponed for future considerations         #leadershipStructure
detectionSkillLevel = 1.00    #skillLevel ratio between probing success/fail
probe_successNum = 1.0        #success/failed probing recons
probe_failNum = 2000.0       
advrsy_defenseThreatValue = 10.00    #ThreatLevel - readiness posture in target's security, probability to detect next attack
advrsy_huntModeOn = False        #Are they looking for us?
advrsy_lastAttack = 100.0           #Time elapsed since detected attack on target
advrsy_frequencyATT = 10.0        #How often does the target get attacked?
eventChance = 1.00  #likelihood that an event will occur, default set at 1.00

def conditionalProbability(prob_A, prob_B, prob_scenario): #prob_scenario is the likelihood any of this occurs at all, default value is 1
#MA255 refresher: P(A|B) = P(A and B) / P(B)   https://en.wikipedia.org/wiki/Conditional_probability
#                 P(AorB) = P(A) + P(B) - P(AandB)   https://people.richland.edu/james/lecture/m170/ch05-rul.html
    print('Given probability of A' + str(prob_A))
    print('Given probability of B' + str(prob_B))
    print('Probability of any event' + str(prob_scenario))
    prob_AandB = ((prob_scenario - prob_A) - prob_B) * (-1.0)
    probA_given_probB = prob_AandB / prob_B     #fancy value of the calculated probability
    print('Conditional probability of A given B' + str(probA_given_probB))
    return probA_given_probB

def parseTransmissionType(t_confFile, target_transmission):
    print('Pulling from configuration file: '+ t_confFile)
    
    #>>matching loop here will go through and find the appropriate target_trans value in the file and pull it
    print('Transmission '+target_transmission+' IDS_risk value: '+ str(1)) #for testing we will set everything as true
    return 1 #normally we would pull the value and store it locally, the cached value would be return here


def detIDS_RiskValue():
    sp_configFile = input('Enter adversary special_IDS ConfigFile: ')   #asking for the special IDS rules file here
    ###error checking
    #    if sp_configFile is not empty
    #    specialRulesFile = sp_configFile
    print('special_IDS ConfigFile at: ' + specialRulesFile)
    IDS_strictness = parse_IDSrules(specialRulesFile)
    n_size = normalizeSizeValue(sizeOfTarget)
    IDS_RiskValue = (IDS_strictness*(detNetworkMapRisk())) / n_size
    return IDS_RiskValue

def normalizeMapValue(m_Status, m_Complete, m_Accuracy, m_nodes, m_update): #generates a normalized value depicting P(perfect map)
    ###not quite sure how to do this part yet...think...
    ####
    return 1

def detNetworkMapRisk(): #    likelihood of 100% mapping (p_A) likelihood of historyInterceptReadiness (p_B)
    publicMapValue = normalizeMapValue(advrsy_OutdoorMapValue, outdorMap_completed, mapAccuracyValue_open, mapValue_open, mapValue_lastUpdate_open)
    privatMapValue = normalizeMapValue(advrsy_IndoorMapValue, indoorMap_completed, mapAccuracyValue_closed, mapValue_close, mapValue_lastUpdate_closed)
    detThreatLevel_SIGINT()
    advrsy_NetworkMapValue = conditionalProbability(privatMapValue, publicMapValue, eventChance) #given the outside mapping, what is the probability they have the closed map fully mapped
    return conditionalProbability(advrsy_NetworkMapValue, advrsy_defenseThreatValue, eventChance) #we assume that this is the the whole scenario and no other probabilities need to be considered. The conditions will not change.

def detThreatLevel_SIGINT():
    detectionSkillLevel = (probe_successNum/probe_failNum) #this allows us to have a multiplying factor if they are able to detect more effective than fail to detect
    n_date = normalizeDate(advrsy_lastAttack)
    if (advrsy_huntModeOn):
        advrsy_defenseThreatValue = conditionalProbability(detectionSkillLevel, (n_date * advrsy_frequencyATT), eventChance) #probably need to normalize the frequence of attacks too
    else:
        advrsy_defenseThreatValue = detectionSkillLevel * (advrsy_frequencyATT) ##not too sure about this, need to think through the math

def detThreatLevel_HUMNINT():
    #language barrier consideration goes here !!<<
    spyCatchSkill = (num_spyCaught/num_spyDeployed) #positive number will mean there are false positives, but it also indicates a heightened security level, this is okay for our model
    n_spyDateCatch = normalizeDate(last_spyCaught)
    advrsy_HUMthreatValue = conditionalProbability(spyCatchSkill, n_spyDateCatch * numSupport, eventChance)
    return advrsy_HUMthreatValue

def normalizeDate(abnormal_date):
    #normalizing function
    normal_Date = abnormal_date * 2
    return normal_Date

def normalizeSizeValue(abnormalSize):
    #normalizing function
    normalizedSize = abnormalSize / 100 #for generalizing purposes
    return normalizedSize

def parse_IDSrules(specialRules_IDS):
    #some special parsing algorithm goes here that looks through specialRules_IDS[file] and adjusts the IDS_strictness value
    strictValue = 1.00
    return strictValue

def calculateSIGINT():
    print('Calculating SIGINT risk value of network: ')
    SIGINT_RiskValue = parseTransmissionType(trans_ConfigFile, trans_type) * detIDS_RiskValue() #combines the risk value of the IDS and whether or not the transmission_type has been implemented under the IDS schema
    print('New SIGINT risk value: '+ str(SIGINT_RiskValue))
    return SIGINT_RiskValue


def calculateHUMINT():
    HUMINT_RiskValue = detThreatLevel_HUMNINT()
    return HUMINT_RiskValue


def get_AdCapabilityValue():
    SIGINT_RiskValue = calculateSIGINT()
    HUMINT_RiskValue = calculateHUMINT()
    return conditionalProbability(HUMINT_RiskValue, SIGINT_RiskValue, eventChance) #decided to make this conditional with the focus action on human intelligence  because the marriage of human intelligence with signal intelligence will drive the action of adversaries. The sensitivity of human interaction is critical to passing of all information. ie, if humans don't care then whatever signals generated by machines can be assumed to be ignored. This is also in line with determining whether or not a transmission becomes subverted when it is detected (e.g., adversary may just overlook incidents)

    #return SIGINT_RiskValue + HUMINT_RiskValue

def parseConfigFile(): #input will be a XML file
    return 0
    ###just hard cord conditional probability into here. do math

print('current SIGINT Risk: ' + str(SIGINT_RiskValue))
print('current HUMINT Risk: ' + str(HUMINT_RiskValue))
print('running algorithm...')
eny_capability = get_AdCapabilityValue()
print('Adversary Capability Value: ' + str(eny_capability))
print('hello i work!')