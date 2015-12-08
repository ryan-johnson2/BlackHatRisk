from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx
import dialogs
from copy import deepcopy

class GraphCanvas(FigureCanvas):
    
    def __init__(self, parent=None, width=5, height=4, dpi=100):

        #The figure and axes that will be shown in the GUI
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.axis('off')
        self.axes.hold(False)

        #initialize teh figure and set the parent
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        #allow for changing sizes
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        #create a network graph and labels
        self.graph = nx.MultiGraph()
        self.setLayout = lambda g: nx.spring_layout(g)
        self.pos = self.setLayout(self.graph)
        self.labels = {}
        self.edgeLabels = {}

        #images for nodes
        self.routerImg = '../img/router.png'

        #create a stack of old graphs for undo redo max size of 10
        self.undoStack = []
        self.redoStack = []


    def clearScreen(self):
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        self.axes.axis('off')
        self.axes.hold(False)
        self.draw()
        self.graph = nx.MultiGraph()
        self.pos = self.setLayout(self.graph)
        self.labels = {}
        self.edgeLabels = {}

    def clearAll(self):
        self.clearScreen()
        self.clearStacks()


    #redraw the graph and update the figure
    def redrawGraph(self):
        self.pos = self.setLayout(self.graph)
        nx.draw(self.graph, self.pos, ax = self.axes, labels = self.labels)
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels = self.edgeLabels, ax = self.axes, label_pos = 0.5)
        self.draw()

    #add a node to the graph
    def addNode(self, node, storage):
        self.clearRedo()
        self.pushToUndo()
        self.graph.add_node(node, storage = storage)
        self.labels[node] = node
        self.redrawGraph()

    def removeNode(self, node):
        self.clearRedo()
        self.pushToUndo()
        self.checkAndRemoveLinks(node)
        self.graph.remove_node(node)
        del self.labels[node]
        self.redrawGraph()

    #add an edge to the graph
    def addEdge(self, name, protocol ,node1, node2, risk):
        self.clearRedo()
        self.pushToUndo()
        self.graph.add_edge(node1, node2, key = name, name = name, protocol = protocol, risk = risk)
        self.createEdgeLabels()
        self.redrawGraph()

    def createEdgeLabels(self):
        edges = self.graph.edges(data = True)
        self.edgeLabels = {}
        for edge in edges:
            if (edge[0], edge[1]) in self.edgeLabels.keys():
                self.edgeLabels[(edge[0], edge[1])] += ",\n" + edge[2]['name']
            elif (edge[1], edge[0]) in self.edgeLabels.keys():
                self.edgeLabels[(edge[1], edge[0])] += ",\n" + edge[2]['name']
            else:
                self.edgeLabels[(edge[0], edge[1])] = edge[2]['name']

    def removeEdge(self, node1, node2):
        self.clearRedo()
        self.pushToUndo()
        self.graph.remove_edge(node1, node2)
        self.createEdgeLabels()
        self.redrawGraph()

    #dialog to add a node to the graph
    def getNewNode(self):
        node, ok = dialogs.AddNode.getDataDialog()
        if ok:
            self.addNode(node[0], node[1])

    #dialog to remove a node from the graph
    def getRemoveNode(self):
        currNodes = self.graph.nodes()
        node, ok = dialogs.RemoveNode.getDataDialog(currNodes)
        if ok:
            self.removeNode(node)

    def displayNode(self):
        currNodes = self.graph.nodes()
        node, ok = dialogs.DisplayNode.getDataDialog(currNodes)
        if ok:
            name = node
            storage = "Unknown"

            for item in self.graph.nodes(data = True):
                if item[0] == node:
                    storage = item[1]['storage']


            message = QtGui.QMessageBox.information(self, "View Node", "Name: {0}\nStorage: {1}".format(name, storage))

    #dailog to add an edge to the graph
    def getNewEdge(self):
        currNodes = self.graph.nodes()
        nodes, ok = dialogs.AddEdge.getDataDialog(currNodes)

        n1 = self.findNode(nodes[2])
        n2 = self.findNode(nodes[3])
        proto = nodes[1]

        if ok and self.checkLinkCompat(n1, n2, proto):
            self.addEdge(nodes[0], nodes[1], nodes[2], nodes[3], nodes[4])
        else:
            message = QtGui.QMessageBox.warning(self, "Black Hat Risk", "Incompatible Link between storage devices!")

    #dialog to remove an edge from the graph
    def getRemoveEdge(self):
        currEdges = self.graph.edges(data = True)
        nodes, ok = dialogs.RemoveEdge.getDataDialog(currEdges)
        if ok:
            self.removeEdge(nodes[0], nodes[1])

    def checkAndRemoveLinks(self, node):
        links = self.graph.edges()

        for link in links:
            if node in link:
                self.removeEdge(link[0], link[1])

    def displayEdge(self):
        currEdges = self.graph.edges(data = True)
        edge, ok = dialogs.DisplayEdge.getDataDialog(currEdges)
        if ok:
            node1 = edge[0]
            node2 = edge[1]
            name = "Unknown"
            protocol = "Unknown"
            risk = "Unknown"

            for item in self.graph.edges(data = True):
                if (item[0] == node1 and item[1] == node2) or (item[1] == node1 and item[0] == node2):
                    name = item[2]['name']
                    protocol = item[2]['protocol']
                    risk = item[2]['risk']

            message = QtGui.QMessageBox.information(self, "View Edge", "Name: {0}\nNode 1: {1}\nNode 2: {2}\nProtocol: {3}\nRisk: {4}".format(name, node1, node2, protocol, risk))

    def pushToUndo(self):
        data = (deepcopy(self.graph), deepcopy(self.labels), deepcopy(self.edgeLabels))
        if len(self.undoStack) == 10:
            self.undoStack = self.undoStack[1:].append(data)
        else:
            self.undoStack.append(data)

    def pushToRedo(self):
        data = (deepcopy(self.graph), deepcopy(self.labels), deepcopy(self.edgeLabels))
        if len(self.redoStack) == 10:
            self.redoStack = self.redoStack[1:].append(data)
        else:
            self.redoStack.append(data)

    def clearRedo(self):
        for item in self.redoStack:
            self.undoStack.append(item)
        self.redoStack = []

    def clearStacks(self):
        self.undoStack = []
        self.redoStack = []

    def undo(self):
        if not (self.undoStack == []):
            self.pushToRedo()
            self.graph, self.labels, self.edgeLabels = self.undoStack.pop()
            self.redrawGraph()
        else:
            self.clearScreen()

    def redo(self):
        if not (self.redoStack == []):
            self.pushToUndo()
            self.graph, self.labels, self.edgeLabels = self.redoStack.pop()
            self.redrawGraph()
        else:
            self.clearScreen()

    def checkLinkCompat(self, node1, node2, proto):
        stores = [node1[1]["storage"], node2[1]["storage"]]

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
        for node in self.graph.nodes(data = True):
            if node[0] == name:
                return node





        





            