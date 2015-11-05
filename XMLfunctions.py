import xml.etree.ElementTree as ET


def create(fname):
	global fName
	if (fname[-1:-5:-1] != "lmx."): fName = fname + ".xml"
	else: fName = fname
	f = open(fName, 'w')
	f.write('<?xml version="1.0"?>\n<network><links></links><nodes></nodes></network>')
  	f.close()
  	global tree 
	tree = ET.parse(fName)
	global root 
	root = tree.getroot()
	#stackoverflow.com/questions/13299427/python-functions-call-by-reference


def addLink(name, protocol, node1, node2, risk):
	#add risk subelement with default value
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
	tree.write(fName)

def addNode(name, storage):
	newTag = ET.SubElement(root[1], "Name")
	newTag.attrib["name"] = name
	storageTag = ET.SubElement(newTag, 'storage')
	storageTag.text = storage
	tree.write(fName)

def removeLink(name):
	for links in root.findall("links"):
		for link in links.findall("Name"):
			if (link.attrib == {'name': name}):
				links.remove(link)
	tree.write(fName)

def removeNode(name):
	for nodes in root.findall("nodes"):
		for node in nodes.findall("Name"):
			if (node.attrib == {'name': name}):
				nodes.remove(node)
	tree.write(fName)

#http://stackoverflow.com/questions/15585885/how-to-delete-a-node-from-an-xml-document-in-python-using-elementtree

def returnLinks():
	returnList = list()
	for links in root.findall("links"):
		for link in links.findall("Name"):
			returnList += tuple([link.attrib["name"], link[0].text, link[1].text, link[2].text, link[3].text])
	print returnList
	#return returnList

def returnNodes():
	returnList = list()
	for nodes in root.findall("links"):
		for node in nodes.findall("Name"):
			returnList += tuple([node.attrib["name"], node[0].text])
	print returnList
	#return returnList

if __name__ == '__main__':
	create("test16")
	addLink("bud", "GSM", "Node1", "Node2", 5)
	addLink("Joe", "GSM", "Node1", "Node2", 5)
	addNode("bud", "GSM")
	addNode("Joe", "Phone")
	#removeLink("bud")
	#removeNode("Joe")
	returnNodes()
	returnLinks()
	print "End"