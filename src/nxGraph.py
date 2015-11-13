from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx
import dialogs

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

    def clearAll(self):
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        self.axes.axis('off')
        self.axes.hold(False)
        self.draw()
        self.graph = nx.Graph()
        self.pos = self.setLayout(self.graph)
        self.labels = {}
        self.edgeLabels = {}


    #redraw the graph and update the figure
    def redrawGraph(self):
        self.pos = self.setLayout(self.graph)
        nx.draw(self.graph, self.pos, ax = self.axes, labels = self.labels)
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels = self.edgeLabels, ax = self.axes, label_pos = 0.5)
        self.draw()

    #add a node to the graph
    def addNode(self, node, storage):
        self.graph.add_node(node, storage = storage)
        self.labels[node] = node
        self.redrawGraph()

    def removeNode(self, node):
        self.checkAndRemoveLinks(node)
        self.graph.remove_node(node)
        del self.labels[node]
        self.redrawGraph()

    #add an edge to the graph
    def addEdge(self, name, protocol ,node1, node2, risk):
        self.graph.add_edge(node1, node2, key = name, name = name, protocol = protocol, risk = risk)
        self.edgeLabels[(node1, node2)] = name
        self.redrawGraph()

    def removeEdge(self, node1, node2):
        self.graph.remove_edge(node1, node2)
        try:
            del self.edgeLabels[(node1, node2)]
        except KeyError:
            del self.edgeLabels[(node2, node1)]
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
        if ok:
            self.addEdge(nodes[0], nodes[1], nodes[2], nodes[3], nodes[4])

    #dialog to remove an edge from the graph
    def getRemoveEdge(self):
        currNodes = self.graph.nodes()
        nodes, ok = dialogs.RemoveEdge.getDataDialog(currNodes)
        if ok:
            self.removeEdge(nodes[0], nodes[1])

    def checkAndRemoveLinks(self, node):
        links = self.graph.edges()

        for link in links:
            if node in link:
                self.removeEdge(link[0], link[1])

    def displayEdge(self):
        currNodes = self.graph.nodes()
        edge, ok = dialogs.DisplayEdge.getDataDialog(currNodes)
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


