from PyQt4 import QtGui, QtCore
import networkItems
import resources

class NetworkItemsTree(QtGui.QTreeWidget):

    def __init__(self, graph):
        super(NetworkItemsTree, self).__init__()
        self.graph = graph
        self.initUI()

    def initUI(self):
        self.setHeaderHidden(True)

        protocols = resources.protocols
        self.createTree("Protocols", protocols)

        storage = resources.storage
        self.createTree("Storage", storage)

    def createTree(self, name, items):
        treeItem = networkItems.NetworkItem(name)

        for item in items:
            treeItem.addChild(networkItems.NetworkItem(item))

        self.addTopLevelItem(treeItem)
        #self.itemDoubleClicked.connect(self.showDialog)



    




