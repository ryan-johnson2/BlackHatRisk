class Node:
    """the datastructure representing a node in the network diagram"""

    def __init__(self, name, storage):
        """initialize the node with a name and storage value"""
        self._name = name # stores the name in a private variable
        self._storage = storage # stores the storage type in a private variable
        self._additional = {} # creates a dictionary for any additional data 

    def getName(self):
        """returns the name of the node"""
        return self._name

    def setName(self, newName):
        """sets the name of the node to newName"""
        self._name = newName

    def getStorage(self):
        """returns the type of storage of the node"""
        return self._storage

    def setStorage(self, newStorage):
        """sets the storage to newStorage"""
        self._storage = newStorage

    def addAdditional(self, name, value):
        """adds an additional piece of data to the additional
        dictionary with a key of name and value of value"""
        self._additional[name] = value

    def getAdditional(self, name):
        """gets the value from the additional dictionary that
        is stored with the key name"""
        return self._additional[name]

    def removeAdditional(self, name):
        """removes the value from the additional dictionary 
        with the key of name"""
        del self._additional[name]


