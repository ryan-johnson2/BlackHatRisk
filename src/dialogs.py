from PyQt4.QtGui import *
from PyQt4.QtCore import *
import resources

class Dialog(QDialog):

    def __init__(self, nodes = [], parent = None):
        super(Dialog, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.nodes = nodes

    def setTitle(self, name):
        self.setWindowTitle(name)

    def addWidgets(self):
        pass

    def addButtons(self):
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout.addWidget(buttons)

    def getData(self):
        pass

    @staticmethod
    def getDataDialog(self, nodes = []):
        pass

class AddNode(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(AddNode, self).__init__(nodes, parent)
        self.setTitle("Add Node")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.nodeNamelbl = QLabel(self)
        self.nodeNamelbl.setText("Node Name:")
        self.nodeName = QLineEdit(self)
        self.nodeName.setObjectName("Node Name")

        self.storagelbl = QLabel(self)
        self.storagelbl.setText("Storage:")
        self.storage = QComboBox(self)
        
        for storeDev in resources.storage:
            self.storage.addItem(storeDev)

        self.layout.addWidget(self.nodeNamelbl)
        self.layout.addWidget(self.nodeName)
        self.layout.addWidget(self.storagelbl)
        self.layout.addWidget(self.storage)

    def getData(self):
        name = str(self.nodeName.text())
        storage = str(self.storage.currentText())
        return (name, storage)

    @staticmethod
    def getDataDialog(nodes = [], parent = None):
        dialog = AddNode(parent)
        result = dialog.exec_()
        nodeData = dialog.getData()
        return (nodeData, result == QDialog.Accepted)

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
            self.nodeName.addItem(node)

        self.layout.addWidget(self.nodeNamelbl)
        self.layout.addWidget(self.nodeName)

    def getData(self):
        return str(self.nodeName.currentText())

    @staticmethod
    def getDataDialog(nodes = [], parent = None):
        dialog = RemoveNode(nodes, parent)
        result = dialog.exec_()
        nodeData = dialog.getData()
        return (nodeData, result == QDialog.Accepted)

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
        nodeData = dialog.getData()
        return (nodeData, result == QDialog.Accepted)

class AddEdge(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(AddEdge, self).__init__(nodes, parent)
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
            self.node1.addItem(node)

        #node 2 of the edge
        self.node2lbl = QLabel(self)
        self.node2lbl.setText("Node 2 Name:")
        self.node2 = QComboBox(self)
        
        for node in self.nodes:
            self.node2.addItem(node)

        #risk of the edge
        self.risklbl = QLabel(self)
        self.risklbl.setText("Risk:")
        self.risk = QLabel(self)
        self.risk.setText("5")

        #self.risk = QComboBox(self)
        
        #for value in ['low', 'medium', 'high']:
        #    self.risk.addItem(str(value))



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
        node1 = str(self.node1.currentText())
        node2 = str(self.node2.currentText())
        risk = str(5)
        return (name, protocol, node1, node2, risk)

    @staticmethod
    def getDataDialog(nodes, parent = None):
        dialog = AddEdge(nodes, parent)
        result = dialog.exec_()
        nodes = dialog.getData()
        return (nodes, result == QDialog.Accepted)

class RemoveEdge(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(RemoveEdge, self).__init__(nodes, parent)
        self.setTitle("Remove Edge")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.edgelbl = QLabel(self)
        self.edgelbl.setText("Edge Name:")
        self.edge = QComboBox(self)
        
        for edge in self.nodes:
            self.edge.addItem(edge[2]["name"])

        self.layout.addWidget(self.edgelbl)
        self.layout.addWidget(self.edge)

    def getData(self):
        name = str(self.edge.currentText())
        
        for edge in self.nodes:
            if edge[2]['name'] == name:
                node1 = edge[0]
                node2 = edge[1]
                break

        return (node1, node2)

    @staticmethod
    def getDataDialog(nodes, parent = None):
        dialog = RemoveEdge(nodes, parent)
        result = dialog.exec_()
        nodes = dialog.getData()
        return (nodes, result == QDialog.Accepted)

class DisplayEdge(Dialog):

    def __init__(self, nodes = [], parent = None):
        super(DisplayEdge, self).__init__(nodes, parent)
        self.setTitle("Display Edge")
        self.addWidgets()
        self.addButtons()

    def addWidgets(self):
        self.edgelbl = QLabel(self)
        self.edgelbl.setText("Edge Name:")
        self.edge = QComboBox(self)
        
        for edge in self.nodes:
            self.edge.addItem(edge[2]["name"])

        self.layout.addWidget(self.edgelbl)
        self.layout.addWidget(self.edge)

    def getData(self):
        name = str(self.edge.currentText())
        
        for edge in self.nodes:
            if edge[2]['name'] == name:
                node1 = edge[0]
                node2 = edge[1]
                break

        return (node1, node2)

    @staticmethod
    def getDataDialog(nodes, parent = None):
        dialog = DisplayEdge(nodes, parent)
        result = dialog.exec_()
        nodes = dialog.getData()
        return (nodes, result == QDialog.Accepted)

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


