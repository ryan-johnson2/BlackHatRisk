#http://docs.python-guide.org/en/latest/scenarios/xml/
"""
import untangle
obj = untangle.parse('test1.xml')

print obj.link["name"]
print obj.link.protocol
print obj.link.node1
print obj.link.node2
print obj.link.risk
attempt one, could not get untangle to operate correctly
"""

import xml.etree.ElementTree as ET
tree = ET.parse('test1.xml')
root = tree.getroot()
#print root
#print root.tag
"""
for child in root:
	print child.tag, child.attrib, child.text"""
#print root[0].text

""" NOTES
.tag gets the tag
.attrib gets associated attribute ie name
.text gets text inside of the tags like risk (returns 15)
 
 root[0][0][0].text would result in GSM Data
 this is the first child, first link, first namespace
</notes>
"""
""" do not use
intent was to try to edit a single part of the xml file
result, deletes everything
def change():
	import xml.etree.ElementTree as ET
	tree = ET.parse('test1.xml')
	root = tree.getroot()
  	f = open('test1.xml', 'w')
	root[0][0][0] = "text message"
  	f.close()
if __name__=="__main__":
  change()

"""

"""
copied from http://stackoverflow.com/questions/1591579/how-to-update-modify-a-xml-file-in-python
import xml.etree.ElementTree

# Open original file
et = xml.etree.ElementTree.parse('file.xml')

# Append new tag: <a x='1' y='abc'>body text</a>
new_tag = xml.etree.ElementTree.SubElement(et.getroot(), 'a')
new_tag.text = 'body text'
new_tag.attrib['x'] = '1' # must be str; cannot be an int
new_tag.attrib['y'] = 'abc'

# Write back to file
#et.write('file.xml')
et.write('file_new.xml')
"""
root[0][0][0].text = "text message" #changes the value of GSM to text message
#attempt to create new node
newTag = ET.SubElement(root[1], 'node3')
#newTag = ET.SubElement(new1, 'Node3')
newTag.attrib["name"] = "Bud"
newTag1 = ET.SubElement(newTag, 'storage')
newTag1.text = "Harddrive"

#newTag.extend(newTag1)
#https://pymotw.com/2/xml/etree/ElementTree/create.html

ET.dump(tree) # this writes the XML to the screen
tree.write("testWrite.xml")