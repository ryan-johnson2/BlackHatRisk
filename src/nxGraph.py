from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx
import edgeDialog as ed
import nodeDialog as nd

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
        self.graph = nx.Graph()
        self.pos = nx.spring_layout(self.graph)
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
        self.pos = nx.spring_layout(self.graph)
        self.labels = {}
        self.edgeLabels = {}


    #redraw the graph and update the figure
    def redrawGraph(self):
        nx.draw(self.graph, self.pos, ax = self.axes, labels = self.labels)
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels = self.edgeLabels, ax = self.axes, label_pos = 0.5)
        self.draw()

    #add a node to the graph
    def addNode(self, node, storage):
        self.graph.add_node(node, storage = storage)
        self.pos = nx.spring_layout(self.graph)
        self.labels[node] = node
        self.redrawGraph()

    def removeNode(self, node):
        self.graph.remove_node(node)
        del self.labels[node]
        self.pos = nx.spring_layout(self.graph)
        self.redrawGraph()

    #add an edge to the graph
    def addEdge(self, name, protocol ,node1, node2, risk):
        self.graph.add_edge(node1, node2, name = name, protocol = protocol, risk = risk)
        self.pos = nx.spring_layout(self.graph)
        self.edgeLabels[(node1, node2)] = name
        self.redrawGraph()

    def removeEdge(self, node1, node2):
        self.graph.remove_edge(node1, node2)
        self.pos = nx.spring_layout(self.graph)
        try:
            del self.edgeLabels[(node1, node2)]
        except KeyError:
            del self.edgeLabels[(node2, node1)]
        self.redrawGraph()

    #dialog to add a node to the graph
    def getNewNode(self):
        node, ok = nd.AddNodeDialog.getNode()
        if ok:
            self.addNode(node[0], node[1])

    #dialog to remove a node from the graph
    def getRemoveNode(self):
        currNodes = self.graph.nodes()
        node, ok = nd.RemoveNodeDialog.getNode(currNodes)
        if ok:
            self.removeNode(node)

    #dailog to add an edge to the graph
    def getNewEdge(self):
        currNodes = self.graph.nodes()
        nodes, ok = ed.AddEdgeDialog.retNodes(currNodes)
        if ok:
            self.addEdge(nodes[0], nodes[1], nodes[2], nodes[3], nodes[4])

    #dialog to remove an edge from the graph
    def getRemoveEdge(self):
        currNodes = self.graph.nodes()
        nodes, ok = ed.RemoveEdgeDialog.retNodes(currNodes)
        if ok:
            self.removeEdge(nodes[0], nodes[1])

