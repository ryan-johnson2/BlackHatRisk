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


def addLink(name, protocol, node1, node2, linkCounter):
	newTag = ET.SubElement(root[0], "link"+str(linkCounter))
	newTag.attrib["name"] = name
	protocolTag = ET.SubElement(newTag, 'protocol')
	protocolTag.text = protocol
	node1Tag = ET.SubElement(newTag, 'node1')
	node1Tag.text = node1
	node2Tag = ET.SubElement(newTag, 'node2')
	node2Tag.text = node2
	tree.write(fName)

def addNode(name, storage, nodeCounter):
	newTag = ET.SubElement(root[1], "node"+str(nodeCounter))
	newTag.attrib["name"] = name
	storageTag = ET.SubElement(newTag, 'storage')
	storageTag.text = storage
	tree.write(fName)

def remove(name):
	#elem = tree.find(name)
	tree.remove(elem)