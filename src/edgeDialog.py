from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EdgeDialog(QDialog):
    def __init__(self, parent = None):
        super(EdgeDialog, self).__init__(parent)

        layout = QVBoxLayout(self)

        # nice widget for editing the date
        self.node1 = QTextEdit(self)
        self.node2 = QTextEdit(self)
        layout.addWidget(self.node1)
        layout.addWidget(self.node2)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # get current date and time from the dialog
    def getNodes(self):
        return (str(self.node1.toPlainText()), str(self.node2.toPlainText()))

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def retNodes(parent = None):
        dialog = EdgeDialog(parent)
        result = dialog.exec_()
        nodes = dialog.getNodes()
        print nodes
        return (nodes, result == QDialog.Accepted)