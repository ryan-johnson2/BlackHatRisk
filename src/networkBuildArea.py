from PyQt4 import QtGui, QtCore
from PIL import Image, ImageQt

class NetworkBuildArea(QtGui.QGraphicsView):

    def __init__(self):
        #calls the init function of the QWidget class
        super(NetworkBuildArea, self).__init__()

        #initializes the UI and creates all objects
        self.initUI()

    def initUI(self):
        #self.setAcceptDrops(True)
        self.setInteractive(True)
        self.initScene()
        self.setScene(self.scene)
        self.hardCodeNet()

    def initScene(self):
        self.scene = NetworkScene()

    def hardCodeNet(self):
        imgSrc = "../img/router.png"
        #imgs = [Image.open(imgSrc) for i in range(3)]
        #imgQs = [ImageQt.ImageQt(img) for img in imgs]
        #pixmaps = [QtGui.QPixmap.fromImage(img) for img in imgQs]

        img = Image.open(imgSrc)
        img.thumbnail((128,128))
        self.imgq = ImageQt.ImageQt(img)

        pixmap = QtGui.QPixmap.fromImage(self.imgq)
        pixmapItem = QtGui.QGraphicsPixmapItem(pixmap)
        pixmapItem2 = QtGui.QGraphicsPixmapItem(pixmap)
        pixmapItem3 = QtGui.QGraphicsPixmapItem(pixmap)

        pixmapItem.setPos(200,200)
        pixmapItem2.setPos(400,0)
        pixmapItem3.setPos(0,0)

        self.scene.addLine(64,64,264,264)
        self.scene.addLine(264,264,464,64)
        self.scene.addLine(464,64,64,64)

        self.scene.addItem(pixmapItem)
        self.scene.addItem(pixmapItem2)
        self.scene.addItem(pixmapItem3)
        
        self.scene.update()



class NetworkScene(QtGui.QGraphicsScene):

    def __init__(self):
        super(NetworkScene, self).__init__()
