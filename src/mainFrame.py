from PyQt4 import QtGui, QtCore
import networkItemsTree
import nxGraph
import XMLfunctions as xml
import resources

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
        self.setGeometry(50, 50, 900, 900)
        self.setWindowIcon(QtGui.QIcon('../img/blackhat.png'))

        #create layout and add widgets
        #create widgets
        self.networkBuild = nxGraph.GraphCanvas()
        self.netTree = networkItemsTree.NetworkItemsTree(self.networkBuild)
        

        #create splitter which allows resizing
        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

        #add widgets to splitter
        splitter.addWidget(self.netTree)
        splitter.addWidget(self.networkBuild)

        splitter.setSizes([50,300])
        
        #set splitter as the cental application widget
        self.setCentralWidget(splitter) 

        #create the drop down menus
        self.createMenu()
     
        #show the UI
        self.show()

    def createMenu(self):
        #create menu bar
        menu = self.menuBar()

        #add menus to menu bar
        fileMenu = menu.addMenu('&File')
        analyzeMenu = menu.addMenu('&Analyze')
        modifyMenu = menu.addMenu('&Modify')
        viewMenu = menu.addMenu('&View')
        editMenu = menu.addMenu('&Edit')
        optionsMenu = menu.addMenu('&Options')

        #set save actions and add to file menu
        saveAction = QtGui.QAction('&Save', self)        
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save file')
        saveAction.triggered.connect(lambda: self.saveFile())
        fileMenu.addAction(saveAction)

        #set open actions and add to file menu
        openAction = QtGui.QAction('&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file')
        openAction.triggered.connect(lambda: self.openFile())
        fileMenu.addAction(openAction)

        #set new actions and add to file menu
        newAction = QtGui.QAction('&New', self)        
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New file')
        newAction.triggered.connect(lambda: self.makeNew())
        fileMenu.addAction(newAction)

        #set exit actions and add to file menu
        exitAction = QtGui.QAction('&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        fileMenu.addAction(exitAction)

        #set the evaluate network action and add to analyze menu
        evalNetAction = QtGui.QAction('&Evaluate Network', self)        
        evalNetAction.setStatusTip('Evaluate Network')
        analyzeMenu.addAction(evalNetAction)

        #set the evaluate link and add to analyze
        evalLinkAction = QtGui.QAction('&Evaluate Link', self)        
        evalLinkAction.setStatusTip('Evaluate Link')
        analyzeMenu.addAction(evalLinkAction)

        #set the simulate least risk route action and add to analyze menu
        simulateLRRAction = QtGui.QAction('&Simulate Least Risk Route', self)        
        simulateLRRAction.setStatusTip('Simulate Least Risk Route')
        analyzeMenu.addAction(simulateLRRAction)

        #set the simulate random route action and add to analyze menu
        simulateRandAction = QtGui.QAction('&Simulate Random Route', self)        
        simulateRandAction.setStatusTip('Simulate Random Route')
        analyzeMenu.addAction(simulateRandAction)

        #set the settings action and add to options
        settingsAction = QtGui.QAction('&Settings', self)        
        settingsAction.setStatusTip('Settings')
        settingsAction.triggered.connect(lambda: self.showSettings())
        optionsMenu.addAction(settingsAction)
        #need to add a setting for max allowed filesize

        #set the help action and add to options
        helpAction = QtGui.QAction('&Help', self)        
        helpAction.setStatusTip('Help')
        helpAction.setShortcut("Ctrl+h")
        helpAction.triggered.connect(lambda: self.showHelp())
        optionsMenu.addAction(helpAction)

        addNodeAction = QtGui.QAction('&Add Node', self)        
        addNodeAction.setStatusTip('Add Node')
        addNodeAction.setShortcut('Ctrl+a')
        addNodeAction.triggered.connect(lambda: self.networkBuild.getNewNode())
        modifyMenu.addAction(addNodeAction)

        addEdgeAction = QtGui.QAction('&Add Edge', self)        
        addEdgeAction.setStatusTip('Add Edge')
        addEdgeAction.setShortcut('Ctrl+e')
        addEdgeAction.triggered.connect(lambda: self.networkBuild.getNewEdge())
        modifyMenu.addAction(addEdgeAction)

        removeNodeAction = QtGui.QAction('&Remove Node', self)        
        removeNodeAction.setStatusTip('Remove Node')
        removeNodeAction.setShortcut('Ctrl+i')
        removeNodeAction.triggered.connect(lambda: self.networkBuild.getRemoveNode())
        modifyMenu.addAction(removeNodeAction)

        removeEdgeAction = QtGui.QAction('&Remove Edge', self)        
        removeEdgeAction.setStatusTip('Remove Edge')
        removeEdgeAction.setShortcut('Ctrl+d')
        removeEdgeAction.triggered.connect(lambda: self.networkBuild.getRemoveEdge())
        modifyMenu.addAction(removeEdgeAction)

        removeProtoAction = QtGui.QAction('&Remove Protocol', self)        
        removeProtoAction.setStatusTip('Remove Protocol')
        removeProtoAction.triggered.connect(lambda: self.removeProtocol())
        modifyMenu.addAction(removeProtoAction)

        addProtoAction = QtGui.QAction('&Add Protocol', self)        
        addProtoAction.setStatusTip('Add Protocol')
        addProtoAction.triggered.connect(lambda: self.addProtocol())
        modifyMenu.addAction(addProtoAction)

        removeStoreAction = QtGui.QAction('&Remove Storage', self)        
        removeStoreAction.setStatusTip('Remove Storeage')
        removeStoreAction.triggered.connect(lambda: self.removeStorage())
        modifyMenu.addAction(removeStoreAction)

        addStoreAction = QtGui.QAction('&Add Storage', self)        
        addStoreAction.setStatusTip('Add Storage')
        addStoreAction.triggered.connect(lambda: self.addStorage())
        modifyMenu.addAction(addStoreAction)

        viewNodeAction = QtGui.QAction('&View Node', self)        
        viewNodeAction.setStatusTip('View Node')
        viewNodeAction.setShortcut('Ctrl+w')
        viewNodeAction.triggered.connect(lambda: self.networkBuild.displayNode())
        viewMenu.addAction(viewNodeAction)

        viewEdgeAction = QtGui.QAction('&View Edge', self)        
        viewEdgeAction.setStatusTip('View Edge')
        viewEdgeAction.setShortcut('Ctrl+r')
        viewEdgeAction.triggered.connect(lambda: self.networkBuild.displayEdge())
        viewMenu.addAction(viewEdgeAction)

        undoAction = QtGui.QAction('&Undo', self)        
        undoAction.setStatusTip('Undo')
        undoAction.setShortcut('Ctrl+z')
        undoAction.triggered.connect(lambda: self.networkBuild.undo())
        editMenu.addAction(undoAction)

        redoAction = QtGui.QAction('&Redo', self)        
        redoAction.setStatusTip('Redo')
        redoAction.setShortcut('Ctrl+y')
        redoAction.triggered.connect(lambda: self.networkBuild.redo())
        editMenu.addAction(redoAction)

    def saveFile(self):
        saveF = QtGui.QFileDialog.getSaveFileName(self, "Save File", "untitled.xml", "XML (*.xml)")
        
        nodes = self.networkBuild.graph.nodes(data = True)
        links = self.networkBuild.graph.edges(data = True)

        try:

            xml.create(saveF)

            for node in nodes:
                name = node[0]
                storage = node[1]['storage']
                xml.addNode(saveF, name, storage)

            for link in links:
                data = link[2]
                name = data['name']
                protocol = data['protocol']
                node1 = link[0]
                node2 = link[1]
                risk = data['risk']
                xml.addLink(saveF, name, protocol, node1, node2, risk)

        except IOError:
            dialog = QtGui.QMessageBox.warning(self, "Incorrect File Selection", "You selected no file or an incorrect file type!")

    def openFile(self):
        openF = QtGui.QFileDialog.getOpenFileName(self, "Open File", "", "XML (*.xml)")
        try:

            links = xml.returnLinks(openF)
            nodes = xml.returnNodes(openF)

            #clear the current graph
            self.makeNew()

            for node in nodes:
                if node != None:
                    name = node[0]
                    storage = node[1]
                    self.networkBuild.addNode(name, storage)

            for link in links:
                if link != None:
                    name = link[0]
                    risk = link[1]
                    protocol = link[2]
                    node1 = link[3]
                    node2 = link[4]
                    self.networkBuild.addEdge(name, protocol, node1, node2, risk)

        except IOError:
            dialog = QtGui.QMessageBox.warning(self, "Incorrect File Selection", "You selected no file or an incorrect file type!")

    def makeNew(self):
        self.networkBuild.clearAll()

    def showHelp(self):
        message = QtGui.QMessageBox.about(self, "Black Hat Risk", "Black Hat Risk Help")

    def showSettings(self):
        message = QtGui.QMessageBox.about(self, "Black Hat Risk", "Black Hat Risk Settings")

    def removeProtocol(self):
        resources.getRemoveProtocol()
        self.netTree.updateUI()

    def addProtocol(self):
        resources.getAddProtocol()
        self.netTree.updateUI()

    def removeStorage(self):
        resources.getRemoveStorage()
        self.netTree.updateUI()

    def addStorage(self):
        resources.getAddStorage()
        self.netTree.updateUI()






        

