import xml.etree.ElementTree as ET

"""Creates a new, blank XML file with a given name."""
def create(fname):
	if (fname[-1:-5:-1] != "lmx."): fName = fname + ".xml"  #checks for .xml at end, and adds if needed
	else: fName = fname
	f = open(fname, 'w')
	f.write('<?xml version="1.0"?>\n<network><links></links><nodes></nodes></network>') #empty network
  	f.close()
	#stackoverflow.com/questions/13299427/python-functions-call-by-reference

"""Adds a new link to the network"""
def addLink(fname, name, protocol, node1, node2, riskm sizeOfData, maxFileSize, linkSecurity, peakHours):
	#add risk subelement with default value
	tree = ET.parse(fname)
	root = tree.getroot() #finds proper link to create
	newTag = ET.SubElement(root[0], "Name")
	newTag.attrib["name"] = name #adds name value
	riskTag = ET.SubElement(newTag, "risk")
	riskTag.text = str(risk)#adds risk value
	protocolTag = ET.SubElement(newTag, 'protocol')
	protocolTag.text = protocol #adds protocol
	node1Tag = ET.SubElement(newTag, 'node1')
	node1Tag.text = node1 #adds parent node 1
	node2Tag = ET.SubElement(newTag, 'node2')
	node2Tag.text = node2 #adds parent node 2
	sizeTag = ET.SubElement(newTag, 'sizeOfData')
	sizeTag.text = sizeOfData
	maxTag = ET.SubElement(newTag, 'maxFileSize')
	maxTag.text = maxFileSize
	secTag = ET.SubElement(newTag, 'LinkSecurity')
	secTag.text = linkSecurity
	peakTag = ET.SubElement(newTag, 'PeakHours?')
	peakTag.text = peakHours
	tree.write(fname) #writes to the xml file
"""Adds a node to the network"""
def addNode(fname, name, storage):
	tree = ET.parse(fname)
	root = tree.getroot() #finds proper node to create
	newTag = ET.SubElement(root[1], "Name")
	newTag.attrib["name"] = name #adds name value
	storageTag = ET.SubElement(newTag, 'storage')
	storageTag.text = storage #adds storage value
	tree.write(fname)#writes to the XML file
"""Removes a link from the XML file"""
def removeLink(fname, name):
	tree = ET.parse(fname)
	root = tree.getroot()
	for links in root.findall("links"):
		for link in links.findall("Name"): #finds proper link
			if (link.attrib == {'name': name}):
				links.remove(link) #removes proper link
	tree.write(fname) #write the XML file without the link
"""Removes a node from the tree"""
def removeNode(fname, name):
	tree = ET.parse(fname)
	root = tree.getroot()
	for nodes in root.findall("nodes"):
		for node in nodes.findall("Name"): #finds proper node
			if (node.attrib == {'name': name}):
				nodes.remove(node) #removes proper node
	tree.write(fname) #writes the XML file without the link

#http://stackoverflow.com/questions/15585885/how-to-delete-a-node-from-an-xml-document-in-python-using-elementtree
"""Pulls all the information on a link out of the XML files into a readable format"""
def returnLinks(fname):
	tree = ET.parse(fname) #creates XML tree
	root = tree.getroot() #gets root of tree
	returnList = list()
	for links in root.findall("links"): #parses though links
		for link in links.findall("Name"): #finds the proper link
			returnList.append(tuple([link.attrib["name"], link[0].text, link[1].text, link[2].text, link[3].text], link[4].text, link[5].text, link[6].text, link[7].text)) #adds the link name, risk value, protocol, and parent nodes to a list
	#print returnList
	return returnList #returns list of information for interpretation
"""Pulls all the information on a node out of the XML files into a readable format"""
def returnNodes(fname):
	tree = ET.parse(fname) #creates XML tree
	root = tree.getroot() #gets root of tree
	returnList = list()
	for nodes in root.findall("nodes"): #parses though nodes
		for node in nodes.findall("Name"):#finds the proper node
			returnList.append(tuple([node.attrib["name"], node[0].text])) #adds the node name and storage method to the list
	#print returnList
	return returnList #returns list of information for interpretation



