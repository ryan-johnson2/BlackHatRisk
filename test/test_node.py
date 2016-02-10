import unittest
import src
from src import node

class TestNodeMethods(unittest.TestCase):
    """Test all node methods"""

    def setUp(self):
        """fixture containing a node"""
        self.node = node.Node("Test Node", "HDD")

    def test_getName(self):
        """tests the get name method"""
        self.assertEqual(self.node.getName(), "Test Node", "Incorrect Name")

    def test_setName(self):
        """tests the set name method"""
        self.node.setName("Node 1")
        self.assertEqual(self.node.getName(), "Node 1", "Incorrect Name")

    def test_getStorage(self):
        """tests the get storage method"""
        self.assertEqual(self.node.getStorage(), "HDD", "Incorrect Storage")

    def test_setStorage(self):
        """tests the set storage method"""
        self.node.setStorage("Paper")
        self.assertEqual(self.node.getStorage(), "Paper", "Incorrect Storage")

    def test_addAndGetAdditional(self):
        """tests the ability to add and get info from additional"""
        self.node.addAdditional("Sec", 4)
        self.assertEqual(self.node.getAdditional("Sec"), 4, "Incorrect Value")

    def test_removeAndGetAdditional(self):
        """tests the ability to remove and get info from additional"""
        self.node.addAdditional("Sec", 4)
        self.node.addAdditional("Test", 8)
        self.assertEqual(self.node.getAdditional("Sec"), 4, "Incorrect Value")
        self.assertEqual(self.node.getAdditional("Test"), 8, "Incorrect Value")
        self.node.removeAdditional("Sec")
        with self.assertRaises(KeyError):
            self.node.getAdditional("Sec")

    def suite():
        """builds a test suite"""
        suite = unittest.TestSuite()
        suite.addTest(TestNodeMethods('test_getName'))
        suite.addTest(TestNodeMethods('test_setName'))
        suite.addTest(TestNodeMethods('test_getStorage'))
        suite.addTest(TestNodeMethods('test_setStorage'))
        suite.addTest(TestNodeMethods('test_addAndGetAdditional'))
        suite.addTest(TestNodeMethods('test_removeAndGetAdditional'))
        return suite
