import xml.etree.ElementTree as ET


def create(fname):
	if (fname[-1:-5:-1] != "lmx."): fName = fname + ".xml"
	else: fName = fname
	f = open(fname, 'w')
	f.write('<?xml version="1.0"?>\n<network><links></links><nodes></nodes></network>')
  	f.close()
	#stackoverflow.com/questions/13299427/python-functions-call-by-reference


def addLink(fname, name, protocol, node1, node2, risk):
	#add risk subelement with default value
	tree = ET.parse(fname)
	root = tree.getroot()
	newTag = ET.SubElement(root[0], "Name")
	newTag.attrib["name"] = name
	riskTag = ET.SubElement(newTag, "risk")
	riskTag.text = str(risk)
	protocolTag = ET.SubElement(newTag, 'protocol')
	protocolTag.text = protocol
	node1Tag = ET.SubElement(newTag, 'node1')
	node1Tag.text = node1
	node2Tag = ET.SubElement(newTag, 'node2')
	node2Tag.text = node2
	tree.write(fname)

def addNode(fname, name, storage):
	tree = ET.parse(fname)
	root = tree.getroot()
	newTag = ET.SubElement(root[1], "Name")
	newTag.attrib["name"] = name
	storageTag = ET.SubElement(newTag, 'storage')
	storageTag.text = storage
	tree.write(fname)

def removeLink(fname, name):
	tree = ET.parse(fname)
	root = tree.getroot()
	for links in root.findall("links"):
		for link in links.findall("Name"):
			if (link.attrib == {'name': name}):
				links.remove(link)
	tree.write(fname)

def removeNode(fname, name):
	tree = ET.parse(fname)
	root = tree.getroot()
	for nodes in root.findall("nodes"):
		for node in nodes.findall("Name"):
			if (node.attrib == {'name': name}):
				nodes.remove(node)
	tree.write(fname)

#http://stackoverflow.com/questions/15585885/how-to-delete-a-node-from-an-xml-document-in-python-using-elementtree

def returnLinks(fname):
	tree = ET.parse(fname)
	root = tree.getroot()
	returnList = list()
	for links in root.findall("links"):
		for link in links.findall("Name"):
			returnList.append(tuple([link.attrib["name"], link[0].text, link[1].text, link[2].text, link[3].text]))
	#print returnList
	return returnList

def returnNodes(fname):
	tree = ET.parse(fname)
	root = tree.getroot()
	returnList = list()
	for nodes in root.findall("nodes"):
		for node in nodes.findall("Name"):
			returnList.append(tuple([node.attrib["name"], node[0].text]))
	#print returnList
	return returnList



