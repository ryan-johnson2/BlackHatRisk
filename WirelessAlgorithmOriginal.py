from link import *

#Algorithm for Wireless Links
#Bluetooth, wifi, etc
"""
TO DO:

	Noise Considerations and Calculations:
		Typical Number of Users for given link
		Is targeted data similiar to typical data on that link?
		Peak hours at start of transfer?

"""

""" Required Information:
		Noise of the Link in Question (Noise defined as amount of traffic on link)
		Signal Strength
		Size / Amount of Data Transferred
		Scanning Capability (Sanning vs Monitoring?)
		Link Speed
		Time Spent on Link (potentially dependant upon Link speed)
	Assumptions:
		Scanning is the ability to detect other Wireless signals.
		Wireless signal strength is determined primarily by distance from beacon.
		Link Speeds are ideal. Future research should be done on more realistic capabilities.
		There is always some risk of being detected. (Risk != 0 unless link not used at all)
	Considerations:
		What if we break up data transfers over the course of a day? A week? 
		How can we account for tunneling and obfuscation attempts by Black Hat? (Consider fragmentation as well)
"""


"""
  readUserRiskValues reads the user configured file for risk values associated with the indivudal fields in a link.
  Defaults are available if not specified by the user for the given iteration. 

"""
def checkUserOverride(link):
  if(link[2] == ""): print('No User Override Detected. Using Default Values')
  else: print('User override detected! Using specific values.')



def wirelessAlgorithm(link):

	#Basic Information From the Link
	risk = 0  #Probability of Being Detected by Unwanted Personnel. 0 - 1
	information = link[2]
	guaranteedDetection = 10 #At which point can just about anyone in the AO detect / sweep the Wireless link we are using?
	print('Beginning Risk Algorithm')
	if(information['isScanning'] == "no"): return "Only risk is in Physical Detection."

	#Begin Calculating Actual Risk Values
	#If the network is not being scanned, then risk is substantially reduced. Only chance of detection occurs if
	#the initiating individual is physically caught utilizing the sending system
	#Awaiting Class Definition of datafields
	if (information['isScanning'] == "yes"):
		numberOfUsers = information['numUsers']
		dataIsSimiliar = information['dataIsSimiliar']
		peakHours = information['peakHours']
		sizeOfData = information['sizeOfTransferredData']
		linkType = information['LinkType']
		maxFileSize = information['maxFileSize']
		linkSecurity = information['linkSecurity']
		scanTime = information['scanTime'] #Time we estimate it takes for 'enemy' to scan their network
		transferTime = 0
		linkSpeed = 0

		if(linkType == "802.11A"): linkSpeed = 54
		elif (linkType == "802.11B"): linkSpeed = 3 #Average of 2-3Mbps
		elif(linkType == "802.11G"): linkSpeed = 20 #Average of 20Mbps
		elif(linkType == "802.11N"): linkSpeed = 600
		elif(linkType == "802.11AC"): linkSpeed = 100 #Average of 70-100Mbps
        elif(linkType == "Bluetooth"): linkSpeed = 1
        else:
          print('Unknown Link Speed. Results will be less accurate.')
          linkSpeed = -1

        if(linkSpeed > 0):
			transferTime = sizeOfData / linkSpeed #All data sent at once. Future TODO: Allow User specified times for transfers.

        if(linkType == "802.11A" or linkType == "802.11B" or linkType == "802.11G" or linkType == "802.11N" or linkType == "802.11AC"):
		  if(linkSecurity == "WEP"): risk += .25
		  elif(linkSecurity == "WPA"): risk += .15
		  elif(linkSecurity == "WPA2"): risk += .10
        else: risk += .25 #To be updated at a later date for Bluetooth, Near Infrared, etc

        if(sizeOfData != -1):
			if(sizeOfData > maxFileSize): 
				return 1
			elif (sizeOfData > (maxFileSize * .75)): 
				risk*=1.2
			elif (sizeOfData > (maxFileSize * .25)): 
				risk*=1.1
        else:
        	print('Size of Data Unknown: Risk Accuracy Degraded')

        if(scanTime != -1):
			if(transferTime >= scanTime):
				return 1;
			elif(transferTime > scanTime * .75):
				risk *= 1.5
			elif(transferTime > scanTime * .25):
				risk *= 1.2
        else: 
			print('Scan Time unknown: Risk Accuracy Degraded')

        if(dataIsSimiliar and peakHours):
			risk *= .5
        elif(dataIsSimiliar and not(peakHours)):
			risk *= .9
        elif(not(dataIsSimiliar) and peakHours):
			risk *= 1.1
        elif(not(dataIsSimiliar) and not(peakHours)):
			risk *= 1.4
        else:
			print('Unknown noise statistics concerning link.')
	return risk

def test():
	test1 = ("","", {"isScanning" : "yes", "sizeOfTransferredData" : 5, "LinkType" : "802.11A", "maxFileSize" : 64, "signalStrength" : 5, "scanTime" : 3600, "numUsers" : 100, "peakHours" : False, "dataIsSimiliar" : True, "linkSecurity" : "WEP"})
	print ('The risk for test link one is: ' + str(wirelessAlgorithm(test1)))
	test2 = ("","", {"isScanning" : "yes", "sizeOfTransferredData" : 1024, "LinkType" : "802.11AC", "maxFileSize" : 64, "signalStrength" : 5, "scanTime" : 3600, "numUsers" : 100, "peakHours" : False, "dataIsSimiliar" : True,"linkSecurity" : "WEP"})
	print ('The risk for test link two is: ' + str(wirelessAlgorithm(test2)))
	test3 = ("","", {"isScanning" : "no", "sizeOfTransferredData" : 5, "LinkType" : "802.11A", "maxFileSize" : 64, "signalStrength" : 5, "scanTime" : 3600, "numUsers" : 100, "peakHours" : False, "dataIsSimiliar" : True,"linkSecurity" : "WEP"})
	print ('The risk for test link three is: ' + str(wirelessAlgorithm(test3)))
	test4 = ("","", {"isScanning" : "yes", "sizeOfTransferredData" : 1024, "LinkType" : "802.11B", "maxFileSize" : 2048, "signalStrength" : 24, "scanTime" : 7200, "numUsers" : 100, "peakHours" : False, "dataIsSimiliar" : True,"linkSecurity" : "WPA2"})
	print ('The risk for test link four is: ' + str(wirelessAlgorithm(test4)))
	test5 = ("","", {"isScanning" : "yes", "sizeOfTransferredData" : 54, "LinkType" : "Bluetooth", "maxFileSize" : 64, "signalStrength" : 5, "scanTime" : 3600, "numUsers" : 100, "peakHours" : False, "dataIsSimiliar" : True,"linkSecurity" : "WPA"})
	print ('The risk for test link five is: ' + str(wirelessAlgorithm(test5)))