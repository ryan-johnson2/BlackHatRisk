import networkx as nx
import node, link

class Graph(nx.MultiGraph):
    """This multi graph will provide the underlying graph datastructure
    to maintain all nodes and links. This will act as the model of our
    MVC framework"""

    def __init__(self):
        """initialize the networkx multigraph as well as our label dictionaries"""
        super(Graph, self).__init__() # initialize the super class, nx.MultiGraph
        self._labels = {} # initialize the dictionary for labels of nodes
        self._linkLabels = {} # initialze the dictionary for the labels of links

    ### Node Methods ###

    def addNode(self, node):
        """add a node to the graph. The input must be a Node"""
        nodeName = node.getName()
        self.add_node(nodeName, obj = node) # add the node to the graph by name storing the Node in obj
        self._labels[nodeName] = nodeName # add the name to the labels dictionary

    def removeNode(self, nodeName):
        """remove the node from the graph as long as it is
        not part of a link"""
        if not self.isLinked(nodeName): # check to see if a node is part of a link
            self.remove_node(nodeName) # remove a the node from the graph
            del self._labels[nodeName] # remove the nodes label

    def getNode(self, nodeName):
        """get the Node give a nodeName"""
        for node in self.nodes(data = True): # iterate through all nodes
            if node[0] == nodeName: # check if the node's name is equal to the input node
                return node[1]['obj'] # return the correct node's Node object

    def isLinked(self, nodeName):
        """determines whether a node is attached to any links"""
        for linkData in self.edges(data = True):
            if nodeName in linkData[:2]: # check to see if the node is in a link
                return True
        return False

    ### Link Methods ###

    def addLink(self, link):
        """adds a link to the graph"""
        (node1, node2) = link.getNodes() 
        linkName = link.getName()
        # adds the link into the graph
        self.add_edge(node1.getName(), node2.getName(), key = linkName, obj = link)
        self.createLinkLabels() # creates new labels for links

    def removeLink(self, linkName):
        """removes a link from the graph"""
        for linkData in self.edges(data = True):
            link = linkData[2]['obj']
            if link.getName() == linkName: # finds the correct link
                (node1, node2) = link.getNodes()
                # removes the link from the graph
                self.remove_edge(node1.getName(), node2.getName())
                self.createLinkLabels() # creates the new link labels
                return

    def getLink(self, linkName):
        """gets a link from the graph"""
        for linkData in self.edges(data = True):
            link = linkData[2]['obj']
            if link.getName() == linkName:
                return link

    def createLinkLabels(self):
        """creates the labels for all links in the graph"""
        links = self.edges(data = True) # get all links
        self._linkLabels =  {} # clear the link lables
        for linkData in links:
            # get all data for the link
            link = linkData[2]['obj']
            linkName = link.getName()
            (node1, node2) = link.getNodes()
            node1Name = node1.getName()
            node2Name = node2.getName()
            # creates the link labels ensuring that multiple can be listed
            # to account for multiple links between a single node
            if (node1Name, node2Name) in self._linkLabels.keys():
                self._linkLabels[(node1Name, node2Name)] += ",\n" + linkName
            elif (node2Name, node1Name) in self._linkLabels.keys():
                self._linkLabels[(node2Name, node1Name)] += ",\n" + linkName
            else:
                self._linkLabels[(node1Name, node2Name)] = linkName

    def getLabels(self):
        """returns the labels and link labels for the graph"""
        return (self._labels, self._linkLabels)

    #TODO: getNodes that will return all node objects
    #TODO: getLinks that will return all link objects