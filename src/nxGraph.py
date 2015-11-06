from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx

class GraphCanvas(FigureCanvas):
    
    def __init__(self, parent=None, width=5, height=4, dpi=100):\

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.axis('off')
        self.axes.hold(False)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.graph = nx.Graph()
        self.pos = nx.spring_layout(self.graph)
        self.labels = {}

    def redrawGraph(self):
        nx.draw(self.graph, self.pos, ax = self.axes, labels = self.labels)
        self.draw()

    def addNode(self, node):
        self.graph.add_node(node)
        self.pos = nx.spring_layout(self.graph)
        self.labels[node] = node
        self.redrawGraph()

    def addNodes(self, nodes):
        self.graph.add_nodes_from(nodes)
        self.pos = nx.spring_layout(self.graph)
        for node in nodes:
            self.labels[node] = node   
        self.redrawGraph()

    def addEdge(self, nodes):
        self.graph.add_edge(nodes[0], nodes[1])
        self.pos = nx.spring_layout(self.graph)
        self.redrawGraph()

    def addEdges(self, edges):
        self.add_edges_from(edges)
        self.pos = nx.spring_layout(self.graph)
        self.redrawGraph




class StaticCanvas(GraphCanvas):

    def compute_initial_figure(self):
        G = nx.path_graph(10)
        pos = nx.spring_layout(G)
        nx.draw(G,pos, labels = self.labels, ax=self.axes, font_size = 16)

