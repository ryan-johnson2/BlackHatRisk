from PyQt4 import QtGui, QtCore
import networkItemsTree
import nxGraph
import XMLfunctions as xml
import resources
from node import Node
from link import Link
import dialogs


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
        """initialize the UI by creating the main frame and adding in all
        the other modules for the application"""

        #set the status bar message
        self.statusBar().showMessage("Ready")

        #set the window options
        self.setWindowTitle("Black Hat Risk")
        self.setGeometry(50, 50, 900, 900)
        self.setWindowIcon(QtGui.QIcon('../img/blackhat.png'))

        #create layout and add widgets
        #create widgets
        self.networkBuild = nxGraph.GraphCanvas()  # The area the network is displayed
        self.netTree = networkItemsTree.NetworkItemsTree(self.networkBuild) # The network tree with the network objects
        

        #create splitter which allows multiple widgets with the ability to resize
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
        """create the menus displayed in the GUI"""

        #create menu bar
        menu = self.menuBar()

        # add menus to menu bar
        fileMenu = menu.addMenu('&File')
        analyzeMenu = menu.addMenu('&Analyze')
        modifyMenu = menu.addMenu('&Modify')
        viewMenu = menu.addMenu('&View')
        editMenu = menu.addMenu('&Edit')
        optionsMenu = menu.addMenu('&Options')

        # set save actions and add to file menu
        saveAction = QtGui.QAction('&Save', self)  # set the name of the action      
        saveAction.setShortcut('Ctrl+S') # set the action keyboard shortcut
        saveAction.setStatusTip('Save file') # set the status bar message
        saveAction.triggered.connect(lambda: self.saveFile()) # actual action for saving a file
        fileMenu.addAction(saveAction) # add the action to the menu

        # set open actions and add to file menu
        openAction = QtGui.QAction('&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file')
        openAction.triggered.connect(lambda: self.openFile())
        fileMenu.addAction(openAction)

        # set new actions and add to file menu
        newAction = QtGui.QAction('&New', self)        
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New file')
        newAction.triggered.connect(lambda: self.makeNew())
        fileMenu.addAction(newAction)

        # set exit actions and add to file menu
        exitAction = QtGui.QAction('&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        fileMenu.addAction(exitAction)

        # set the evaluate network action and add to analyze menu
        evalNetAction = QtGui.QAction('&Evaluate Network', self)        
        evalNetAction.setStatusTip('Evaluate Network')
        analyzeMenu.addAction(evalNetAction)

        # set the evaluate link and add to analyze
        evalLinkAction = QtGui.QAction('&Evaluate Link', self)        
        evalLinkAction.setStatusTip('Evaluate Link')
        analyzeMenu.addAction(evalLinkAction)

        # set the simulate least risk route action and add to analyze menu
        simulateLRRAction = QtGui.QAction('&Simulate Least Risk Route', self)        
        simulateLRRAction.setStatusTip('Simulate Least Risk Route')
        analyzeMenu.addAction(simulateLRRAction)

        # set the simulate random route action and add to analyze menu
        simulateRandAction = QtGui.QAction('&Simulate Random Route', self)        
        simulateRandAction.setStatusTip('Simulate Random Route')
        analyzeMenu.addAction(simulateRandAction)

        # set the settings action and add to options
        settingsAction = QtGui.QAction('&Settings', self)        
        settingsAction.setStatusTip('Settings')
        settingsAction.triggered.connect(lambda: self.showSettings())
        optionsMenu.addAction(settingsAction)
        # need to add a setting for max allowed filesize

        # set the help action and add to options
        helpAction = QtGui.QAction('&Help', self)        
        helpAction.setStatusTip('Help')
        helpAction.setShortcut("Ctrl+h")
        helpAction.triggered.connect(lambda: self.showHelp())
        optionsMenu.addAction(helpAction)

        # set the add node action and add to the modify menu
        addNodeAction = QtGui.QAction('&Add Node', self)        
        addNodeAction.setStatusTip('Add Node')
        addNodeAction.setShortcut('Ctrl+a')
        addNodeAction.triggered.connect(lambda: self.networkBuild.getNewNode()) # call on network build for modify actions
        modifyMenu.addAction(addNodeAction)

        # set the add edge action and add to the modify menu
        addEdgeAction = QtGui.QAction('&Add Edge', self)        
        addEdgeAction.setStatusTip('Add Edge')
        addEdgeAction.setShortcut('Ctrl+e')
        addEdgeAction.triggered.connect(lambda: self.networkBuild.getNewLink())
        modifyMenu.addAction(addEdgeAction)

        # set the remove node action and add to the modify menu
        removeNodeAction = QtGui.QAction('&Remove Node', self)        
        removeNodeAction.setStatusTip('Remove Node')
        removeNodeAction.setShortcut('Ctrl+i')
        removeNodeAction.triggered.connect(lambda: self.networkBuild.getRemoveNode())
        modifyMenu.addAction(removeNodeAction)

        # set the remove edge action and add to the modify menu
        removeEdgeAction = QtGui.QAction('&Remove Edge', self)        
        removeEdgeAction.setStatusTip('Remove Edge')
        removeEdgeAction.setShortcut('Ctrl+d')
        removeEdgeAction.triggered.connect(lambda: self.networkBuild.getRemoveLink())
        modifyMenu.addAction(removeEdgeAction)

        # set the remove protocol action and add to the modify menu
        removeProtoAction = QtGui.QAction('&Remove Protocol', self)        
        removeProtoAction.setStatusTip('Remove Protocol')
        removeProtoAction.triggered.connect(lambda: self.removeProtocol())
        modifyMenu.addAction(removeProtoAction)

        # set the add protocol action and add to the modify menu
        addProtoAction = QtGui.QAction('&Add Protocol', self)        
        addProtoAction.setStatusTip('Add Protocol')
        addProtoAction.triggered.connect(lambda: self.addProtocol())
        modifyMenu.addAction(addProtoAction)

        # set the remove storage action and add to the modify menu
        removeStoreAction = QtGui.QAction('&Remove Storage', self)        
        removeStoreAction.setStatusTip('Remove Storeage')
        removeStoreAction.triggered.connect(lambda: self.removeStorage())
        modifyMenu.addAction(removeStoreAction)

        # set the add storage action and add to the modify menu
        addStoreAction = QtGui.QAction('&Add Storage', self)        
        addStoreAction.setStatusTip('Add Storage')
        addStoreAction.triggered.connect(lambda: self.addStorage())
        modifyMenu.addAction(addStoreAction)

        # set the view node action and add to the view menu
        viewNodeAction = QtGui.QAction('&View Node', self)        
        viewNodeAction.setStatusTip('View Node')
        viewNodeAction.setShortcut('Ctrl+w')
        viewNodeAction.triggered.connect(lambda: self.networkBuild.displayNode())
        viewMenu.addAction(viewNodeAction)

        # set the view edge action and add to the view menu
        viewEdgeAction = QtGui.QAction('&View Edge', self)        
        viewEdgeAction.setStatusTip('View Edge')
        viewEdgeAction.setShortcut('Ctrl+r')
        viewEdgeAction.triggered.connect(lambda: self.networkBuild.displayLink())
        viewMenu.addAction(viewEdgeAction)

        # set the undo action and add to the edit menu
        undoAction = QtGui.QAction('&Undo', self)        
        undoAction.setStatusTip('Undo')
        undoAction.setShortcut('Ctrl+z')
        undoAction.triggered.connect(lambda: self.networkBuild.undo())
        editMenu.addAction(undoAction)

        # set the redo action and add to the edit menu
        redoAction = QtGui.QAction('&Redo', self)        
        redoAction.setStatusTip('Redo')
        redoAction.setShortcut('Ctrl+y')
        redoAction.triggered.connect(lambda: self.networkBuild.redo())
        editMenu.addAction(redoAction)

    def saveFile(self):
        """save the current file that is being worked on to XML format"""
        # creates a graphical dialog that returns a path to where the user wants to save
        saveF = QtGui.QFileDialog.getSaveFileName(self, "Save File", "untitled.xml", "XML (*.xml)")
        
        #get the data for the links and nodes
        nodes = self.networkBuild.graph.nodes(data = True)
        links = self.networkBuild.graph.edges(data = True)

        try:
            # calls the XMLFunctions to create an xml file at the given path
            xml.create(saveF)

            for item in nodes: # add each node to the xml file
                node = item[1]['obj']
                name = node.getName()
                storage = node.getStorage()
                xml.addNode(saveF, name, storage)

            for item in links: # add each link to the xml file
                link = item[2]['obj']
                name = link.getName()
                protocol = link.getProtocol()
                (n1, n2) = link.getNodes()
                node1 = n1.getName()
                node2 = n2.getName()
                risk = link.getRisk()
                xml.addLink(saveF, name, protocol, node1, node2, risk)

        except IOError: # displays a warning if an incorrect file is chosen
            dialog = QtGui.QMessageBox.warning(self, "Incorrect File Selection", "You selected no file or an incorrect file type!")

    def openFile(self):
        """opens an xml file into a network"""
        # creates a graphical dialog allowing the user to choose a file
        openF = QtGui.QFileDialog.getOpenFileName(self, "Open File", "", "XML (*.xml)")
        try:

            links = xml.returnLinks(openF) # get all the links from xml
            nodes = xml.returnNodes(openF) # get all the nodes from xml

            #clear the current graph
            self.makeNew() # create a blank graph

            for item in nodes: # add each node to the graph
                if item != None:
                    name = item[0]
                    storage = item[1]
                    node = Node(name, storage)
                    self.networkBuild.addNode(node)

            nodes = self.networkBuild.graph.nodes(data = True)

            for item in links: # add each link to the graph
                if item != None:
                    name = item[0]
                    risk = item[1]
                    protocol = item[2]
                    nodeName1 = item[3]
                    nodeName2 = item[4]
                    node1 = self.networkBuild.findNode(nodeName1)[1]['info']
                    node2 = self.networkBuild.findNode(nodeName2)[1]['info']
                    link = Link(node1, node2, name, protocol, risk)
                    self.networkBuild.addEdge(link)

        except IOError: # show an error dialog when a wrong file is selected
            dialog = QtGui.QMessageBox.warning(self, "Incorrect File Selection", "You selected no file or an incorrect file type!")

    def makeNew(self):
        """clears the network building area of all information"""
        # ask if the user wants to save their work
        saveAns, ok = dialogs.SaveOnNew.getDataDialog()
        if ok:
            if saveAns == "Yes" :
                self.saveFile()
            elif saveAns == "Cancel":
                return
            self.networkBuild.clearAll()

    def showHelp(self):
        """shows a help dialog"""
        message = QtGui.QMessageBox.about(self, "Black Hat Risk", "Black Hat Risk Help")

    def showSettings(self):
        """shows a settings dialog"""
        message = QtGui.QMessageBox.about(self, "Black Hat Risk", "Black Hat Risk Settings")

    def removeProtocol(self):
        """removes a protocol"""
        resources.getRemoveProtocol() # creates dialog to remove a protocol
        self.netTree.updateUI() # updates the UI to show the protocol

    def addProtocol(self):
        """adds a protocol"""
        resources.getAddProtocol() # creates dialog to add a protocol
        self.netTree.updateUI()

    def removeStorage(self):
        """removes a storage device"""
        resources.getRemoveStorage() # creates a dialog to remove a storage device
        self.netTree.updateUI()

    def addStorage(self):
        """adds a storage device"""
        resources.getAddStorage() # creates a dialog to add a storage device
        self.netTree.updateUI()






        

