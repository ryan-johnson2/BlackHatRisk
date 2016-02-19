class Node:
    """The Node class is used to create Node objects which are used
    to store information about network nodes. This will be the underlying
    datastructure to access node information in the Graph class. As well 
    Links must contain two node objects"""

    def __init__(self, name, storage):
        """The __init__ method is called any time a Node object is instantiated. It must
        take as input a name as a string and a storage device as a string. These values
        will be stored in private variables and should only be accessed through the provided
        methods. The additional dictionary will allow the user to store any extra information
        about the node using the provided methods."""
        self._name = name # stores the name in a private variable
        self._storage = storage # stores the storage type in a private variable
        self._additional = {} # creates a dictionary for any additional data 

    def getName(self):
        """The getName method takes no input and will return the name of the node as a string"""
        return self._name

    def setName(self, newName):
        """The setName method will take a new name as a string as input and set the name of the node 
        to that new name."""
        self._name = newName

    def getStorage(self):
        """The getStorage method takes no input and will return the storage device as a string"""
        return self._storage

    def setStorage(self, newStorage):
        """The setStorage method will take a new storage device as a string as input and set the storage 
        of the node to that new storage."""
        self._storage = newStorage

    def addAdditional(self, name, value):
        """The addAdditional method will take in a name of the new data and a value to be assigned to that
        name. It will place the input in the additional dictionary with the name as the key and the value 
        as the value in that dictionary pair."""
        self._additional[name] = value

    def getAdditional(self, name):
        """The getAdditional method will take in a name as input. The method will attempt to use the name
        as a key in the additional dictionary to retrieve the value. If the name is found it will return 
        the value otherwise it will return nothing."""
        return self._additional[name]

    def removeAdditional(self, name):
        """The remove additional method will take a name as input. The method will then remove the key value
        pair from the dictionary if the input name is stored already. No action is taken if the name is not
        present as a key in the additional dictionary."""
        del self._additional[name]


