class Link:
    """the datastructure representing a link in the network diagram"""
    
    def __init__(self, node1, node2, name, protocol, risk = 5):
        """initialize a link with two nodes, a name, a protocol and a risk value"""
        self._n1 = node1 # private variable storing the first node which is of type Node
        self._n2 = node2 # private variable storing the second node which is of type Node
        self._name = name # private variable storing the name of the link
        self._proto = protocol # private variable storing the protocol of the link
        self._risk = risk # private varibale storing the risk value of the link
        self._additional = {} # private dictionary to store additional data

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

    def addAdditional(self, name, value):
        """add the value to the additional dictionary with the key name"""
        self._additional[name] = value

    def getAdditional(self, name):
        """get the value from additional at the key name"""
        return self._additional[name]

    def removeAdditional(self, name):
        """remove the value from additional at the key name"""
        del self._additional[name]