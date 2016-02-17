class Link:
    """the datastructure representing a link in the network diagram"""
    
    def __init__(self, node1, node2, name, protocol, sizeOfData, maxFileSize, linkSecurity, peakHours, risk = -1):
        """initialize a link with two nodes, a name, a protocol and a risk value"""
        self._n1 = node1 # private variable storing the first node which is of type Node
        self._n2 = node2 # private variable storing the second node which is of type Node
        self._name = name # private variable storing the name of the link
        self._proto = protocol # private variable storing the protocol of the link
        self._risk = risk # private varibale storing the risk value of the link
        self._size = sizeOfData #size of data sent over the network
        self._max = maxFileSize #largest data that will be tolerated being sent over the link
        self._security = linkSecurity #returns the security used by the protocol, ie. WEP, WPA, WPA2
        self._peak = peakHours #returns boolean value if the link transmits during peak hours
        self._additional = {} # private dictionary to store additional data
                              #by default this includes {numberOfUsers, dataIsSimilar, scanTime, isScanning}


    def getNodes(self):
        """return a tuple of the two nodes assigned to the link"""
        return (self._n1, self._n2)

    def getName(self):
        """return the name of the link"""
        return self._name

    def setName(self, newName):
        """set the name of the link to newName"""
        self._name = newName

    def getProtocol(self):
        """return the protocol of the link"""
        return self._proto

    def setProtocol(self, newProtocol):
        """set the protocol of the link to newProtocol"""
        self._proto = newProtocol

    def getRisk(self):
        """return the risk value of the link"""
        return self._risk

    def getSizeOfData(self):
        "returns the size of data that is being transmitted over the link"
        return self._size

    def getMaxFileSize(self):
        "returns the size of the largest amount of data that will be tolerated being sent over the link"
        return self._max

    def getLinkSecurity(self):
        "returns the security used by the protocol"
        return self._security

    def setSizeOfData(self, newSize):
        "returns the size of data that is being transmitted over the link"
        self._size = newSize

    def setMaxFileSize(self, newMax):
        "returns the size of the largest amount of data that will be tolerated being sent over the link"
        self._max = newMax

    def setLinkSecurity(self, newSecurity):
        "returns the security used by the protocol"
        self._security = newSecurity

    def addAdditional(self, name, value):
        """add the value to the additional dictionary with the key name"""
        self._additional[name] = value

    def getPeakHours(self):
        "gets boolean value if the link transmits during peak hours"
        return self._peak

    def setPeakHours(self, peak):
        "sets the peakHours boolean"
        self._peak = peak

    def getAdditional(self, name):
        """get the value from additional at the key name"""
        return self._additional[name]

    def removeAdditional(self, name):
        """remove the value from additional at the key name"""
        del self._additional[name]