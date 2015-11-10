from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AddNodeDialog(QDialog):
    def __init__(self, parent = None):
        super(AddNodeDialog, self).__init__(parent)
        self.setWindowTitle("Add Node")
        layout = QVBoxLayout(self)

        self.nodeNamelbl = QLabel(self)
        self.nodeNamelbl.setText("Node Name:")
        self.nodeName = QLineEdit(self)
        self.nodeName.setObjectName("Node Name")

        self.storagelbl = QLabel(self)
        self.storagelbl.setText("Storage:")
        self.storage = QLineEdit(self)
        self.storage.setObjectName("storage")

        layout.addWidget(self.nodeNamelbl)
        layout.addWidget(self.nodeName)
        layout.addWidget(self.storagelbl)
        layout.addWidget(self.storage)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # get current date and time from the dialog
    def getNodeData(self):
        name = str(self.nodeName.text())
        storage = str(self.storage.text())
        return (name, storage)

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getNode(parent = None):
        dialog = AddNodeDialog(parent)
        result = dialog.exec_()
        nodeData = dialog.getNodeData()
        return (nodeData, result == QDialog.Accepted)

class RemoveNodeDialog(QDialog):
    def __init__(self, nodes = [], parent = None):
        super(RemoveNodeDialog, self).__init__(parent)
        self.setWindowTitle("Remove Node")
        self.nodes = nodes

        layout = QVBoxLayout(self)

        self.nodeNamelbl = QLabel(self)
        self.nodeNamelbl.setText("Node Name:")
        self.nodeName = QComboBox(self)
        
        for node in self.nodes:
            self.nodeName.addItem(node)

        layout.addWidget(self.nodeNamelbl)
        layout.addWidget(self.nodeName)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # get current date and time from the dialog
    def getNodeData(self):
        return str(self.nodeName.currentText())

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getNode(nodes = [], parent = None):
        dialog = RemoveNodeDialog(nodes, parent)
        result = dialog.exec_()
        nodeData = dialog.getNodeData()
        return (nodeData, result == QDialog.Accepted)

class DisplayNodeDialog(QDialog):
    def __init__(self, nodes = [], parent = None):
        super(DisplayNodeDialog, self).__init__(parent)
        self.setWindowTitle("Display Node")
        self.nodes = nodes

        layout = QVBoxLayout(self)

        self.nodeNamelbl = QLabel(self)
        self.nodeNamelbl.setText("Node Name:")
        self.nodeName = QComboBox(self)
        
        for node in self.nodes:
            self.nodeName.addItem(node)

        layout.addWidget(self.nodeNamelbl)
        layout.addWidget(self.nodeName)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # get current date and time from the dialog
    def getNodeData(self):
        return str(self.nodeName.currentText())

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getNode(nodes = [], parent = None):
        dialog = DisplayNodeDialog(nodes, parent)
        result = dialog.exec_()
        nodeData = dialog.getNodeData()
        return (nodeData, result == QDialog.Accepted)