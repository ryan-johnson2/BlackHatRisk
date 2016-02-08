from PyQt4 import QtGui, QtCore
import networkItems, resources

#TODO 
#show all the information for links and nodes in the tree

class NetworkItemsTree(QtGui.QTreeWidget):
    """Creates a tree of network items

    Methods:
      initUI: used for initialization
      createTree: used for initializtion
      updateUI: updates the tree in the UI
    """

    def __init__(self, graph):
        """initializes the tree"""
        super(NetworkItemsTree, self).__init__()
        self.graph = graph # will be used to add the ability to add items from the tree
        self.initUI()

    def initUI(self):
        """initialzes the UI for the tree"""
        self.setHeaderHidden(True) # hides the tree header

        protocols = resources.protocols # gets all the protocols from resources
        self.createTree("Protocols", protocols) # creates a protocols tree

        storage = resources.storage # gets all the storage devices
        self.createTree("Storage", storage) # creates storage tree

    def createTree(self, name, items):
        """creates a tree with the name as the root and the items as nodes"""
        treeItem = networkItems.NetworkItem(name) # turns the name into a NetworkItem in order to work in the tree

        for item in items: # turn all the items into NetworkItems and adds them to the tree
            treeItem.addChild(networkItems.NetworkItem(item))

        self.addTopLevelItem(treeItem) # adds the tree to the main tree
        #self.itemDoubleClicked.connect(self.showDialog)

    def updateUI(self):
        """updatse the user interface"""
        self.clear() # clear the tree
        self.initUI() # reinitialize the tree



    




