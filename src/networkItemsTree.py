from PyQt4 import QtGui, QtCore
import networkItems

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
        treeItem = QtGui.QTreeWidgetItem(name)

        for item in items:
            treeItem.addChild(QtGui.QTreeWidgetItem(item))

        self.addTopLevelItem(treeItem)
        self.connect(QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*)"), self.processItem)

    def processItem(self, currTreeItem):
        print currTreeItem.name
        self.graph.addNode(currTreeItem.name)



    




