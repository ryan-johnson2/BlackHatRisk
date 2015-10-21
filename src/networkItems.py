from PyQt4 import QtGui, QtCore

class NetworkItem(QtGui.QTreeWidgetItem):

    def __init__(self, name):
        super(NetworkItem, self).__init__([name])
