from PyQt4 import QtGui, QtCore

class NetworkItem(QtGui.QTreeWidgetItem):

    def __init__(self, name, graph):
        super(NetworkItem, self).__init__([name])
        self.name = name
        self.graph = graph


