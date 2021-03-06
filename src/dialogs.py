from PyQt4.QtGui import *
from PyQt4.QtCore import *
import resources
from node import Node
from link import Link

class Dialog(QDialog):
    """Provides the base for each graphical dialog
    """

    def __init__(self, nodes = [], parent = None):
        super(Dialog, self).__init__(parent)
        self.layout = QVBoxLayout(self) # set the layout of the dialog to VBox
        self.nodes = nodes 

    def setTitle(self, name):
        """Set the window title"""
        self.setWindowTitle(name)

    def addWidgets(self):
        """Add widgets to the VBox"""
        pass

    def addButtons(self):
        """add the ok and cancel buttons to the VBox"""
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self) # create buttons
        buttons.accepted.connect(self.accept) # set the action of the buttons
        buttons.rejected.connect(self.reject)
        self.layout.addWidget(buttons) # add the buttons to the 

    def findNode(self, name):
        """find a node and its data by name"""
        for node in self.nodes: # check thorugh all nodes and their data
            if node[0] == name:
                return node # return the node with the correct name

    def getData(self):
        """get the data returned from the Dialog"""
        pass

    @staticmethod
    def getDataDialog(self, nodes = []):
        """build the dialog and get the data from it"""
        pass

class AddNode(Dialog):
    """Create a dialog to add a node"""

    def __init__(self, nodes = [], parent = None):
        super(AddNode, self).__init__(nodes, parent)
        self.setTitle("Add Node")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        """add widgets to the window"""
        self.nodeNamelbl = QLabel(self)
        self.nodeNamelbl.setText("Node Name:") # ass a label that shows Node Name:
        self.nodeName = QLineEdit(self) # create a text entry box
        self.nodeName.setObjectName("Node Name")

        self.storagelbl = QLabel(self)
        self.storagelbl.setText("Storage:")
        self.storage = QComboBox(self) # create a dropdown selection
        
        for storeDev in resources.storage:
            self.storage.addItem(storeDev) # get all possible storage devices and add them to the dropdown

        # add all widgets to the main VBox
        self.layout.addWidget(self.nodeNamelbl)
        self.layout.addWidget(self.nodeName)
        self.layout.addWidget(self.storagelbl)
        self.layout.addWidget(self.storage)

    def getData(self):
        """get the data input in the window"""
        name = str(self.nodeName.text()) # get the name in the text box
        storage = str(self.storage.currentText()) # get teh selected storage device
        node = Node(name, storage)
        return node

    @staticmethod
    def getDataDialog(nodes = [], parent = None):
        """creates a dialog and returns the data"""
        dialog = AddNode(parent) # create instance of add node
        result = dialog.exec_() # run the class
        node = dialog.getData() # get the data selected
        return (node, result == QDialog.Accepted) # will return a node object

class RemoveNode(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(RemoveNode, self).__init__(nodes, parent)
        self.setTitle("Remove Node")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.nodeNamelbl = QLabel(self)
        self.nodeNamelbl.setText("Node Name:")
        self.nodeName = QComboBox(self)
        
        for node in self.nodes:
            self.nodeName.addItem(node) # create a dropdown selection of nodes

        self.layout.addWidget(self.nodeNamelbl)
        self.layout.addWidget(self.nodeName)

    def getData(self):
        return str(self.nodeName.currentText())

    @staticmethod
    def getDataDialog(nodes = [], parent = None):
        dialog = RemoveNode(nodes, parent)
        result = dialog.exec_()
        nodeName = dialog.getData()
        return (nodeName, result == QDialog.Accepted) # returns the name of a node

class DisplayNode(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(DisplayNode, self).__init__(nodes, parent)
        self.setTitle("Display Node")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.nodeNamelbl = QLabel(self)
        self.nodeNamelbl.setText("Node Name:")
        self.nodeName = QComboBox(self)
        
        for node in self.nodes:
            self.nodeName.addItem(node)

        self.layout.addWidget(self.nodeNamelbl)
        self.layout.addWidget(self.nodeName)

    def getData(self):
        return str(self.nodeName.currentText())

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getDataDialog(nodes = [], parent = None):
        dialog = DisplayNode(nodes, parent)
        result = dialog.exec_()
        nodeName = dialog.getData()
        return (nodeName, result == QDialog.Accepted) # returns a node name

class AddLink(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(AddLink, self).__init__(nodes, parent)
        self.setTitle("Add Edge")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.linkNamelbl = QLabel(self)
        self.linkNamelbl.setText("Link Name:")
        self.linkName = QLineEdit(self)
        self.linkName.setObjectName("Link Name")

        #protocol of the edge
        self.protocollbl = QLabel(self)
        self.protocollbl.setText("Protocol:")
        self.protocol = QComboBox(self)
        
        for proto in resources.protocols:
            self.protocol.addItem(proto)


        #node 1 of the edge
        self.node1lbl = QLabel(self)
        self.node1lbl.setText("Node 1 Name:")
        self.node1 = QComboBox(self)

        for node in self.nodes:
            self.node1.addItem(node[0]) # refers to nodename in
                                        # list of nodes from nx

        #node 2 of the edge
        self.node2lbl = QLabel(self)
        self.node2lbl.setText("Node 2 Name:")
        self.node2 = QComboBox(self)
        
        for node in self.nodes:
            self.node2.addItem(node[0])

        #risk of the edge
        self.risklbl = QLabel(self)
        self.risklbl.setText("Risk:")
        self.risk = QLabel(self)
        self.risk.setText("5")

        self.layout.addWidget(self.linkNamelbl)
        self.layout.addWidget(self.linkName)
        self.layout.addWidget(self.protocollbl)
        self.layout.addWidget(self.protocol)
        self.layout.addWidget(self.node1lbl)
        self.layout.addWidget(self.node1)
        self.layout.addWidget(self.node2lbl)
        self.layout.addWidget(self.node2)
        self.layout.addWidget(self.risklbl)
        self.layout.addWidget(self.risk)

    def getData(self):
        name = str(self.linkName.text())
        protocol = str(self.protocol.currentText())
        nodeName1 = str(self.node1.currentText())
        nodeName2 = str(self.node2.currentText())
        risk = str(5)
        node1 = self.findNode(nodeName1)[1]['obj']
        node2 = self.findNode(nodeName2)[1]['obj']
        link = Link(node1, node2, name, protocol, risk)
        return link

    @staticmethod
    def getDataDialog(nodes, parent = None):
        dialog = AddLink(nodes, parent)
        result = dialog.exec_()
        link = dialog.getData()
        return (link, result == QDialog.Accepted)

class RemoveLink(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(RemoveLink, self).__init__(nodes, parent)
        self.setTitle("Remove Edge")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.edgelbl = QLabel(self)
        self.edgelbl.setText("Edge Name:")
        self.edge = QComboBox(self)
        
        for edge in self.nodes:
            link = edge[2]['obj']
            self.edge.addItem(link.getName())

        self.layout.addWidget(self.edgelbl)
        self.layout.addWidget(self.edge)

    def getData(self):
        name = str(self.edge.currentText())
        
        for edge in self.nodes:
            link = edge[2]['obj']
            if  link.getName() == name:
                return link.getName()

    @staticmethod
    def getDataDialog(nodes, parent = None):
        dialog = RemoveLink(nodes, parent)
        result = dialog.exec_()
        linkName = dialog.getData()
        return (linkName, result == QDialog.Accepted)

class DisplayLink(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(DisplayLink, self).__init__(nodes, parent)
        self.setTitle("Display Edge")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.edgelbl = QLabel(self)
        self.edgelbl.setText("Edge Name:")
        self.edge = QComboBox(self)
        
        for edge in self.nodes:
            link = edge[2]['obj']
            self.edge.addItem(link.getName())

        self.layout.addWidget(self.edgelbl)
        self.layout.addWidget(self.edge)

    def getData(self):
        name = str(self.edge.currentText())
        
        for edge in self.nodes:
            link = edge[2]['obj']
            if link.getName() == name:
                return link

    @staticmethod
    def getDataDialog(nodes, parent = None):
        dialog = DisplayLink(nodes, parent)
        result = dialog.exec_()
        linkName = dialog.getData()
        return (linkName, result == QDialog.Accepted)

class RemoveProtocol(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(RemoveProtocol, self).__init__(nodes, parent)
        self.setTitle("Remove Protocol")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.protoNamelbl = QLabel(self)
        self.protoNamelbl.setText("Protocol Name:")
        self.protoName = QComboBox(self)
        
        for proto in resources.protocols:
            self.protoName.addItem(proto)

        self.layout.addWidget(self.protoNamelbl)
        self.layout.addWidget(self.protoName)

    def getData(self):
        return str(self.protoName.currentText())

    @staticmethod
    def getDataDialog(nodes = [], parent = None):
        dialog = RemoveProtocol(nodes, parent)
        result = dialog.exec_()
        nodeData = dialog.getData()
        return (nodeData, result == QDialog.Accepted)

class AddProtocol(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(AddProtocol, self).__init__(nodes, parent)
        self.setTitle("Add Protocol")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.protoNamelbl = QLabel(self)
        self.protoNamelbl.setText("Protocol Name:")
        self.protoName = QLineEdit(self)
        self.protoName.setObjectName("Link Name")

        self.layout.addWidget(self.protoNamelbl)
        self.layout.addWidget(self.protoName)

    def getData(self):
        return str(self.protoName.text())

    @staticmethod
    def getDataDialog(nodes = [], parent = None):
        dialog = AddProtocol(nodes, parent)
        result = dialog.exec_()
        nodeData = dialog.getData()
        return (nodeData, result == QDialog.Accepted)

class RemoveStorage(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(RemoveStorage, self).__init__(nodes, parent)
        self.setTitle("Remove Storage")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.storageNamelbl = QLabel(self)
        self.storageNamelbl.setText("Storage Name:")
        self.storageName = QComboBox(self)
        
        for store in resources.storage:
            self.storageName.addItem(store)

        self.layout.addWidget(self.storageNamelbl)
        self.layout.addWidget(self.storageName)

    def getData(self):
        return str(self.storageName.currentText())

    @staticmethod
    def getDataDialog(nodes = [], parent = None):
        dialog = RemoveStorage(nodes, parent)
        result = dialog.exec_()
        nodeData = dialog.getData()
        return (nodeData, result == QDialog.Accepted)

class AddStorage(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(AddStorage, self).__init__(nodes, parent)
        self.setTitle("Add Storage")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.storageNamelbl = QLabel(self)
        self.storageNamelbl.setText("Storage Name:")
        self.storageName = QLineEdit(self)
        self.storageName.setObjectName("Storage Name")

        self.layout.addWidget(self.storageNamelbl)
        self.layout.addWidget(self.storageName)

    def getData(self):
        return str(self.storageName.text())

    @staticmethod
    def getDataDialog(nodes = [], parent = None):
        dialog = AddStorage(nodes, parent)
        result = dialog.exec_()
        nodeData = dialog.getData()
        return (nodeData, result == QDialog.Accepted)

class SaveOnNew(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(SaveOnNew, self).__init__(nodes, parent)
        self.setTitle("Save")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.savelbl = QLabel(self)
        self.savelbl.setText("Would you like to save") # ass a label that shows Node Name:

        self.save = QComboBox(self) # create a dropdown selection
        self.save.addItem("Yes") # get all possible storage devices and add them to the dropdown
        self.save.addItem("No")
        self.save.addItem("Cancel")

        # add all widgets to the main VBox
        self.layout.addWidget(self.savelbl)
        self.layout.addWidget(self.save)

    def getData(self):
        ans = str(self.save.currentText()) # get teh selected storage device
        return ans

    @staticmethod
    def getDataDialog(nodes = [], parent = None):
        dialog = SaveOnNew(parent) # create instance of add node
        result = dialog.exec_() # run the class
        ans = dialog.getData() # get the data selected
        return (ans, result == QDialog.Accepted) # will return a node object


