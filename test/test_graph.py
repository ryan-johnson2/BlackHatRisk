import unittest
import src
from src import node, link, graph

class TestGraphMethods(unittest.TestCase):

    def setUp(self):
        """builds a basic graph for testing"""
        self.node1 = node.Node("N1", "HDD")
        self.node2 = node.Node("N2", "Paper")
        self.node3 = node.Node("N3", "Disk")
        self.link1 = link.Link(self.node1, self.node2, "L1", "IO", 5)
        self.link2 = link.Link(self.node2, self.node1, "L2", "WIFI", 9)
        self.graph = graph.Graph()

    def test_addNode(self):
        """tests the add node method"""
        self.graph.addNode(self.node1)
        self.assertEqual(self.graph.nodes()[0], "N1")
        self.assertEqual(self.graph.nodes(data = True)[0][1]['obj'], self.node1)

    def test_removeNode(self):
        """tests the remove node method"""
        self.graph.addNode(self.node1)
        self.assertEqual(self.graph.nodes()[0], "N1")
        self.graph.removeNode("N1")
        self.assertEqual(self.graph.nodes(), [])

    def test_getNode(self):
        """tests the get node method"""
        self.graph.addNode(self.node1)
        self.assertEqual(self.graph.nodes()[0], "N1")
        self.assertEqual(self.graph.getNode("N1"), self.node1)

    def test_isLinked(self):
        """tests the is linked method"""
        self.graph.addNode(self.node1)
        self.graph.addNode(self.node2)
        self.graph.addNode(self.node3)
        self.graph.addLink(self.link1)
        self.assertTrue(self.graph.isLinked("N1"))
        self.assertTrue(self.graph.isLinked("N2"))
        self.assertFalse(self.graph.isLinked("N3"))

    def test_addLink(self):
        """tests the add link method"""
        self.graph.addNode(self.node1)
        self.graph.addNode(self.node2)
        self.graph.addLink(self.link1)
        link = self.graph.edges(data = True)[0]
        self.assertEqual(link[2]['obj'], self.link1)

    def test_removeLink(self):
        """tests the remove link method"""
        self.graph.addNode(self.node1)
        self.graph.addNode(self.node2)
        self.graph.addLink(self.link1)
        link = self.graph.edges(data = True)[0]
        self.assertEqual(link[2]['obj'], self.link1)
        self.graph.removeLink("L1")
        self.assertTrue(self.graph.edges() == [])

    def test_getLink(self):
        """tests the get link method"""
        self.graph.addNode(self.node1)
        self.graph.addNode(self.node2)
        self.graph.addLink(self.link1)
        self.assertEqual(self.graph.getLink("L1"), self.link1)

    def test_createLinkLabels(self):
        """tests the create links and labels method"""
        self.graph.addNode(self.node1)
        self.graph.addNode(self.node2)
        self.graph.addLink(self.link1)
        self.assertEqual(self.graph._linkLabels, {("N1", "N2"): "L1"})
        self.graph.addLink(self.link2)
        self.assertEqual(self.graph._linkLabels, {("N2", "N1"): "L2,\nL1"})

    def test_getLabels(self):
        """tests the get labels method"""
        self.graph.addNode(self.node1)
        self.graph.addNode(self.node2)
        self.graph.addLink(self.link1)
        (labels, linkLabels) = self.graph.getLabels()
        self.assertEqual(self.graph._labels, {"N1":"N1", "N2":"N2"})
        self.assertEqual(self.graph._linkLabels, {("N1", "N2"): "L1"})