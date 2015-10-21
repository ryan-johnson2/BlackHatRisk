from PyQt4 import QtGui
import networkItems

class NetworkItemsTree(QtGui.QTreeWidget):

    def __init__(self):
        super(NetworkItemsTree, self).__init__()

        self.initUI()

    def initUI(self):
        self.setHeaderHidden(True)

        protocols = ["SATCOM", "Courier", "Ethernet", "Plain Text", "Cypher Text"]
        self.createTree("Protocols", protocols)

        hosts = ["Unknown Host", "Router", "Radio"]
        self.createTree("Hosts", hosts)

    def createTree(self, name, items):
        treeItem = networkItems.NetworkItem(name)

        for item in items:
            treeItem.addChild(networkItems.NetworkItem(item))

        self.addTopLevelItem(treeItem)





