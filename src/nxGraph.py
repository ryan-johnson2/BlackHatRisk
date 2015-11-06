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

    def redrawGraph(self):
        nx.draw(self.graph, self.pos, ax = self.axes)
        self.draw()

    def addNode(self, node):
        self.graph.add_node(node)
        self.pos = nx.spring_layout(self.graph)
        self.redrawGraph()

    def addNodes(self, nodes):
        self.graph.add_nodes_from(nodes)
        self.pos = nx.spring_layout(self.graph)
        self.redrawGraph()

    def addEdge(self, node1, node2):
        self.graph.add_edge((node1, node2))
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
        nx.draw(G,pos,ax=self.axes)

