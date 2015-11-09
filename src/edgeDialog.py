from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AddEdgeDialog(QDialog):

    def __init__(self, nodes = [], parent = None):
        super(AddEdgeDialog, self).__init__(parent)
        self.nodes = nodes

        layout = QVBoxLayout(self)

        #name of the edge
        self.linkNamelbl = QLabel(self)
        self.linkNamelbl.setText("Link Name:")
        self.linkName = QLineEdit(self)
        self.linkName.setObjectName("Link Name")

        #protocol of the edge
        self.protocollbl = QLabel(self)
        self.protocollbl.setText("Protocol:")
        self.protocol = QLineEdit(self)
        self.protocol.setObjectName("Protocol")

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
        self.risk = QLineEdit(self)
        self.risk.setObjectName("Risk")



        layout.addWidget(self.linkNamelbl)
        layout.addWidget(self.linkName)
        layout.addWidget(self.protocollbl)
        layout.addWidget(self.protocol)
        layout.addWidget(self.node1lbl)
        layout.addWidget(self.node1)
        layout.addWidget(self.node2lbl)
        layout.addWidget(self.node2)
        layout.addWidget(self.risklbl)
        layout.addWidget(self.risk)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # get current date and time from the dialog
    def getNodes(self):
        name = str(self.linkName.text())
        protocol = str(self.protocol.text())
        node1 = str(self.node1.currentText())
        node2 = str(self.node2.currentText())
        risk = str(self.risk.text())
        return (name, protocol, node1, node2, risk)

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def retNodes(nodes, parent = None):
        dialog = AddEdgeDialog(nodes, parent)
        result = dialog.exec_()
        nodes = dialog.getNodes()
        return (nodes, result == QDialog.Accepted)

class RemoveEdgeDialog(QDialog):

    def __init__(self, nodes = [], parent = None):
        super(RemoveEdgeDialog, self).__init__(parent)
        self.nodes = nodes

        layout = QVBoxLayout(self)

        self.node1lbl = QLabel(self)
        self.node1lbl.setText("Node 1 Name:")
        self.node1 = QComboBox(self)

        for node in self.nodes:
            self.node1.addItem(node)


        self.node2lbl = QLabel(self)
        self.node2lbl.setText("Node 2 Name:")
        self.node2 = QComboBox(self)
        
        for node in self.nodes:
            self.node2.addItem(node)

        layout.addWidget(self.node1lbl)
        layout.addWidget(self.node1)
        layout.addWidget(self.node2lbl)
        layout.addWidget(self.node2)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # get current date and time from the dialog
    def getNodes(self):
        return (str(self.node1.currentText()), str(self.node2.currentText()))

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def retNodes(nodes, parent = None):
        dialog = RemoveEdgeDialog(nodes, parent)
        result = dialog.exec_()
        nodes = dialog.getNodes()
        return (nodes, result == QDialog.Accepted)