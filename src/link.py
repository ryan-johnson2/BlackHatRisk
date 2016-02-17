class Link:
    """The Link class is used to create Link objects which are used to store
    information about network links. These Link objects will be the underlying
    data structures stored in the Graph class to access information about
    Link objects. The Link class will also contain a risk algorithm, depent ont
    the information about the link to determine its risk."""
    
    def __init__(self, node1, node2, name, protocol, risk = 5):
        """The __init__ method will be called any time a Link object is instantiated.
        It must take as input two node objects, a name as a string, a protocol as a string
        and currently a default risk value, which will change when the risk algorithm is
        complete. As well there is an additional values dictionary to store any excess
        information about a Link. All of the values are stored in private variables and
        should only be accessed with the provided methods."""
        self._n1 = node1 # private variable storing the first node which is of type Node
        self._n2 = node2 # private variable storing the second node which is of type Node
        self._name = name # private variable storing the name of the link
        self._proto = protocol # private variable storing the protocol of the link
        self._risk = risk # private varibale storing the risk value of the link
        self._additional = {} # private dictionary to store additional data
        #self._riskAlgorithm = ???

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