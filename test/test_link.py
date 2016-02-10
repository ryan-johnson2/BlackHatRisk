import unittest
import src
from src import node, link

class TestLinkMethods(unittest.TestCase):

    def setUp(self):
        """creates two nodes and a link for testing"""
        self.node1 = node.Node("N1", "HDD")
        self.node2 = node.Node("N2", "Paper")
        self.link = link.Link(self.node1, self.node2, "L1", "IO", 5)

    def test_getNodes(self):
        """tests the get nodes method"""
        self.assertEqual(self.link.getNodes(), (self.node1, self.node2))

    def test_getName(self):
        """tests the get name method"""
        self.assertEqual(self.link.getName(), "L1")

    def test_setName(self):
        """tests the set name method"""
        self.link.setName("TL1")
        self.assertEqual(self.link.getName(), "TL1")

    def test_getProtocol(self):
        """tests the get protocol method"""
        self.assertEqual(self.link.getProtocol(), "IO")

    def test_setProtocol(self):
        """tests the set protocol method"""
        self.link.setProtocol("WIFI")
        self.assertEqual(self.link.getProtocol(), "WIFI")

    def test_getRisk(self):
        """tests the get risk method"""
        self.assertEqual(self.link.getRisk(), 5)

    def test_addAndGetAdditional(self):
        """tests the ability to add and get data from additional"""
        self.link.addAdditional("Sec", 4)
        self.assertEqual(self.link.getAdditional("Sec"), 4, "Incorrect Value")

    def test_removeAndGetAdditional(self):
        """tests the ability to remove and get data from additional"""
        self.link.addAdditional("Sec", 4)
        self.link.addAdditional("Test", 8)
        self.assertEqual(self.link.getAdditional("Sec"), 4, "Incorrect Value")
        self.assertEqual(self.link.getAdditional("Test"), 8, "Incorrect Value")
        self.link.removeAdditional("Sec")
        with self.assertRaises(KeyError):
            self.link.getAdditional("Sec")