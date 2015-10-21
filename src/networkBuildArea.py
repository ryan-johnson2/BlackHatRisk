from PyQt4 import QtGui

class NetworkBuildArea(QtGui.QGraphicsView):

    def __init__(self):
        #calls the init function of the QWidget class
        super(NetworkBuildArea, self).__init__()

        #initializes the UI and creates all objects
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)
        self.initScene()
        self.setScene(self.scene)

    def initScene(self):
         self.scene = NetworkScene()


class NetworkScene(QtGui.QGraphicsScene):

    def __init__(self):
        super(NetworkScene, self).__init__()

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        self.addItem(event)