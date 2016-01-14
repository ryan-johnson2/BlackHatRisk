from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx
import dialogs
from copy import deepcopy
import node, link

class GraphCanvas(FigureCanvas):
    """Provides the backend functionality for the graph as well
    as the actually GUI representation of the graph.

    Methods:
        clearScreen
        clearAll
        redrawGraph
        addNode
        removeNode
        addEdge
        createEdgeLabels
        removeEdge
        getNewNode
        getRemoveNode
        displayNode
        getNewEdge
        getRemoveEdge
        checkAndRemoveLinks
        displayEdge
        pushToUndo
        pushToRedo
        clearRedo
        clearStacks
        undo
        redo
        checkLinkCompat
        findNode
    """

    
    def __init__(self, parent=None, width=5, height=4, dpi=100):

        #The figure and axes that will be shown in the GUI
        self.fig = Figure(figsize=(width, height), dpi=dpi) # creates the initial figure needed by matplotlib
        self.axes = self.fig.add_subplot(111) # adds the sub_plot that items will be added to
        self.axes.axis('off') # do not show the axes
        self.axes.hold(False) # allows the graph to be displayed

        #initialize the figure and set the parent
        FigureCanvas.__init__(self, self.fig) # initializes the parent class from matplotlib to work with Qt
        self.setParent(parent) # set as parent

        #allow for changing sizes
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding) # allows the Figure to be resized
        FigureCanvas.updateGeometry(self) # update the gemoetry to reflect the changes above

        #create a network graph and labels
        self.graph = nx.MultiGraph() # creates the graph that all nodes and links will be added to
        self.setLayout = lambda g: nx.spring_layout(g) # anonymous function to set the layout of the graph when it displays
        self.pos = self.setLayout(self.graph) # set the layout of the graph
        self.labels = {} # dictionary that will contain the labels for nodes
        self.edgeLabels = {} # dictionary that will contain the labels for edges

        #images for nodes
        self.routerImg = '../img/router.png' # path to image of a router (unused)

        #create a stack of old graphs for undo redo max size of 10
        self.undoStack = [] # stack that will hold the state for undos
        self.redoStack = [] # stack that will hold the state for redos


    def clearScreen(self):
        """clear the UI screen and all data in the graph"""
        self.fig.clear() # clear the figure
        self.axes = self.fig.add_subplot(111) # readd the subplot
        self.axes.axis('off') # create same settings as __init__
        self.axes.hold(False)
        self.draw() # draw the balnk subplot
        self.graph = nx.MultiGraph() # create a new graph
        self.pos = self.setLayout(self.graph) # set the layout
        self.labels = {} # clear the labels
        self.edgeLabels = {}

    def clearAll(self):
        """clears the screen and stacks for undo and redo"""
        self.clearScreen()
        self.clearStacks()


    #redraw the graph and update the figure
    def redrawGraph(self):
        """redraw the graph to the UI"""
        self.pos = self.setLayout(self.graph) # set the graph layout
        nx.draw(self.graph, self.pos, ax = self.axes, labels = self.labels) # draw the graph to the screen
        # draw the edge labels
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels = self.edgeLabels, ax = self.axes, label_pos = 0.5)
        self.draw() # draw the figure to the screen

    #add a node to the graph
    def addNode(self, node):
        """add a node to the graph and display it on the UI"""
        self.clearRedo() # clear the redo stack
        self.pushToUndo() # push the state to the undo stack
        self.graph.add_node(node.name, info = node) # add the node to the graph
        self.labels[node.name] = node.name # add the label to labels
        self.redrawGraph() # redraw the graph to the screen

    def removeNode(self, nodeName):
        """remove a node from the graph and display on the UI"""
        self.clearRedo()
        self.pushToUndo()
        self.checkAndRemoveLinks(nodeName) # remove any links that were attached to the node
        self.graph.remove_node(nodeName) # remove the node
        del self.labels[nodeName] # delete the label
        self.redrawGraph()

    #add an edge to the graph
    def addEdge(self, link):
        """add an edge to the graph and display on the UI"""
        self.clearRedo()
        self.pushToUndo()
        self.graph.add_edge(link.n1.name, link.n2.name, key = link.name, info = link) # add the edge to the graph
        self.createEdgeLabels() # create the edge labels
        self.redrawGraph()

    def createEdgeLabels(self):
        """creates the dictionary of edge labels"""
        edges = self.graph.edges(data = True) # get all of the edges with their data
        self.edgeLabels = {}
        for edge in edges: # add each edge into the edgeLabels dict
            # the logic will create multiple lables in the case of multiple edges
            # between the same nodes
            link = edge[2]['info']
            if (edge[0], edge[1]) in self.edgeLabels.keys():
                self.edgeLabels[(edge[0], edge[1])] += ",\n" + link.name
            elif (edge[1], edge[0]) in self.edgeLabels.keys():
                self.edgeLabels[(edge[1], edge[0])] += ",\n" + link.name
            else:
                self.edgeLabels[(edge[0], edge[1])] = link.name

    def removeEdge(self, nodeName1, nodeName2):
        """remove an edge from the graph and display on the UI"""
        self.clearRedo()
        self.pushToUndo()
        self.graph.remove_edge(nodeName1, nodeName2) # remove the edge
        self.createEdgeLabels() # recreate the edge labels
        self.redrawGraph()

    #dialog to add a node to the graph
    def getNewNode(self):
        """creates a graphical dialog to add a node to the graph"""
        node, ok = dialogs.AddNode.getDataDialog() # calls the add node dialog from dialogs
        if ok:
            self.addNode(node) # adds the new node if ok is hit on the dialog

    #dialog to remove a node from the graph
    def getRemoveNode(self):
        """creates a graphical dialog to remove a node from the graph"""
        currNodes = self.graph.nodes() # gets the current nodes
        nodeName, ok = dialogs.RemoveNode.getDataDialog(currNodes)
        if ok:
            self.removeNode(nodeName) # removes the selected node

    def displayNode(self):
        """creates a graphical dialog to display a nodes information
        which will be shown in a seperate dialog"""
        currNodes = self.graph.nodes()
        nodeName, ok = dialogs.DisplayNode.getDataDialog(currNodes)
        if ok:
            name = nodeName
            storage = "Unknown"

            for item in self.graph.nodes(data = True): # finds the data of the selected node
                node = item[1]['info']
                if node.name == nodeName:
                    storage = node.storage

            # displays the selected nodes information in a message box
            message = QtGui.QMessageBox.information(self, "View Node", "Name: {0}\nStorage: {1}".format(name, storage))

    #dailog to add an edge to the graph
    def getNewEdge(self):
        """creates a graphical dialog to create a new edge and ensures
        that the edge is between two compatible nodes"""
        currNodes = self.graph.nodes(data = True)
        link, ok = dialogs.AddEdge.getDataDialog(currNodes)

        if ok and self.checkLinkCompat(link.n1, link.n2, link.proto): # checks compatability of the nodes and protocol and adds the edge if possible
            self.addEdge(link)
        else:
            message = QtGui.QMessageBox.warning(self, "Black Hat Risk", "Incompatible Link between storage devices!")

    #dialog to remove an edge from the graph
    def getRemoveEdge(self):
        """creates a graphical dialog to remove an edge from the graph"""
        currEdges = self.graph.edges(data = True) # gets the current edges and their data
        (node1, node2), ok = dialogs.RemoveEdge.getDataDialog(currEdges)
        if ok:
            self.removeEdge(node1, node2) # removes the edge

    def checkAndRemoveLinks(self, node):
        """checks for links attached to a node and removes them"""
        links = self.graph.edges() # gets all edges

        for link in links: # looks for the node in every link and removes all links attached to it
            if node in link:
                self.removeEdge(link[0], link[1])

    def displayEdge(self):
        """creates a graphical dialog to select an edge and display its information"""
        currEdges = self.graph.edges(data = True)
        (nodeName1, nodeName2), ok = dialogs.DisplayEdge.getDataDialog(currEdges)
        if ok: # gets teh user selected edge
            name = "Unknown"
            protocol = "Unknown"
            risk = "Unknown"

            for item in self.graph.edges(data = True): # finds all the data for the edge selected
                link = item[2]['info']
                if (item[0] == nodeName1 and item[1] == nodeName2) or (item[1] == nodeName1 and item[0] == nodeName2):
                    name = link.name
                    protocol = link.proto
                    risk = link.risk

            # display the data for the edge in a message box
            message = QtGui.QMessageBox.information(self, "View Edge", "Name: {0}\nNode 1: {1}\nNode 2: {2}\nProtocol: {3}\nRisk: {4}".format(name, nodeName1, nodeName2, protocol, risk))

    def pushToUndo(self):
        """gets the current state of the graph and pushes it to the undo stack"""
        # gets a deep copy of the state due to object mutability
        data = (deepcopy(self.graph), deepcopy(self.labels), deepcopy(self.edgeLabels))
        if len(self.undoStack) == 10: # only allows stack to grow to 10 states
            self.undoStack = self.undoStack[1:].append(data) # push the state to the stack
        else:
            self.undoStack.append(data)

    def pushToRedo(self):
        """gets teh current state of the graph and push it to the redo stack"""
        data = (deepcopy(self.graph), deepcopy(self.labels), deepcopy(self.edgeLabels))
        if len(self.redoStack) == 10: # redo stack can only grow to 10 states
            self.redoStack = self.redoStack[1:].append(data)
        else:
            self.redoStack.append(data)

    def clearRedo(self):
        """clears the redo stack and pushes the items to the undo stack"""
        for item in self.redoStack:
            self.undoStack.append(item) # push items to undo stack
        self.redoStack = []

    def clearStacks(self):
        """clears teh undo and redo stacks"""
        self.undoStack = []
        self.redoStack = []

    def undo(self):
        """undo to the previous state"""
        if not (self.undoStack == []): # check to ensure undo is not empty
            self.pushToRedo() # push the current state to redo
            self.graph, self.labels, self.edgeLabels = self.undoStack.pop() # get the previous state from undo
            self.redrawGraph() # redraw the graph to the previous state
        else:
            self.clearScreen() # clear the screen if undo stack is empty

    def redo(self):
        """redo to the state before the last undo"""
        if not (self.redoStack == []): # ensure redo is not empty
            self.pushToUndo() # push the current state to undo
            self.graph, self.labels, self.edgeLabels = self.redoStack.pop() # get the previous data from redo
            self.redrawGraph() 
        else:
            self.clearScreen()

    def checkLinkCompat(self, node1, node2, proto):
        """checks to ensure the protocol is compatible for use between the two nodes"""
        stores = [node1.storage, node2.storage] # create a list of the storage devices for the two nodes

        # follow the logic to ensure that the protocol and nodes storage devices are compatibile
        if stores[0] == "Paper" and stores[1] == "Paper":
            if proto == "Sneakernet":
                return True
            return False

        elif "Paper" in stores and "Hard Drive" in stores:
            if proto == "IO":
                return True
            return False

        elif "Paper" in stores and "Phone" in stores:
            if proto == "IO":
                return True
            return False

        elif "Hard Drive" in stores and "Phone" in stores:
            if proto in ["IO", "Bluetooth", "Sharedrive", "Instant Communication", "Nearfield"]:
                return True
            return False

        elif "Hard Drive" in stores and "Removeable Media" in stores:
            if proto in ["IO", "Bluetooth", "Nearfield"]:
                return True
            return False

        elif stores[0] == "Hard Drive" and stores[1] == "Hard Drive":
            if proto in ["IO", "Bluetooth", "Sharedrive", "Instant Communication", "Nearfield", "Email"]:
                return True
            return False

        elif "Phone" in stores and "Removeable Media" in stores:
            if proto in ["IO", "Bluetooth", "Nearfield"]:
                return True
            return False

        elif stores[0] == "Phone" and stores[1] == "Phone":
            if proto in ["IO", "Bluetooth", "Sharedrive", "Instant Communication", "Nearfield", "GSM", "Email" ]:
                return True
            return False

        elif stores[0] == "Removeable Media" and stores[1] == "Removeable Media":
            if proto in ["IO", "Bluetooth", "Sharedrive", "Instant Communication", "Nearfield", "GSM", "Email"]:
                return True
            return False

        else:
            return False

    def findNode(self, name):
        """find a node and its data by name"""
        for node in self.graph.nodes(data = True): # check thorugh all nodes and their data
            if node[0] == name:
                return node # return the node with the correct name





        





            