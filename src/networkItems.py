from PyQt4 import QtGui, QtCore

class NetworkItem(QtGui.QTreeWidgetItem):
    """creates a NetworkItem Object"""

    def __init__(self, name):
        super(NetworkItem, self).__init__([name]) # initialize the parent class
        self.name = name # store the name
        


