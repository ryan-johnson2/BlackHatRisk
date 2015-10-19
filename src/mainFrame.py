#library dependencies
from PyQt4 import QtGui
import networkBuildArea

class MainFrame(QtGui.QMainWindow):
    """Creates the main frame of the GUI  which will contain
    all other GUI items to be displayed
    """

    def __init__(self):
        #calls the init function of the QWidget class
        super(MainFrame, self).__init__()

        #initializes the UI and creates all objects
        self.initUI()

    def initUI(self):

        #set the status
        self.statusBar().showMessage("Ready")

        #set the window options
        self.setWindowTitle("Black Hat Risk")
        self.setGeometry(200, 50, 650, 650)
        self.setWindowIcon(QtGui.QIcon('../img/blackhat.png'))

        #create the drop down menus
        self.createMenu()

        #create layout and add widgets
        self.createLayout()      

        #show the UI
        self.show()

    def createMenu(self):
        #create menu bar
        menu = self.menuBar()

        #add menus to menu bar
        fileMenu = menu.addMenu('&File')
        analyzeMenu = menu.addMenu('&Analyze')

        #set exit actions and add to file menu
        exitAction = QtGui.QAction('&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        fileMenu.addAction(exitAction) 

        #set save actions and add to file menu
        saveAction = QtGui.QAction('&Save', self)        
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save file')
        fileMenu.addAction(saveAction)

        #set open actions and add to file menu
        openAction = QtGui.QAction('&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file')
        fileMenu.addAction(openAction)

        #set the test action and add to analyze menu
        testAction = QtGui.QAction('&Test Network', self)        
        testAction.setStatusTip('Test Network')
        analyzeMenu.addAction(testAction)

        #set the simulate action and add to analyze menu
        simulateAction = QtGui.QAction('&Simulate Network', self)        
        simulateAction.setStatusTip('Simulate Network')
        analyzeMenu.addAction(simulateAction)


    def createLayout(self):
        #create the main widget with a grid layout
        mainWidget = QtGui.QWidget()
        gridLayout = QtGui.QGridLayout()
        mainWidget.setLayout(gridLayout)

        #create widgets and add them to the layout
        networkBuild = networkBuildArea.NetworkBuildArea()
        gridLayout.addWidget(networkBuild, 0, 1)
        
        #set the main widget as the cental application widget
        self.setCentralWidget(mainWidget)

