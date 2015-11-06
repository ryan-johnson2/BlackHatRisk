from PyQt4 import QtGui, QtCore
import networkItems
import edgeDialog

class NetworkItemsTree(QtGui.QTreeWidget):

    def __init__(self, graph):
        super(NetworkItemsTree, self).__init__()
        self.graph = graph
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
        self.itemDoubleClicked.connect(self.showDialog)

    def addNode(self, nodeName):
        self.graph.addNode(nodeName)

    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter the node name:')

        if ok:
            self.addNode(str(text))



    




