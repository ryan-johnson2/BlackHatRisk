#http://docs.python-guide.org/en/latest/scenarios/xml/


import xml.etree.ElementTree as ET
tree = ET.parse('test1.xml')
root = tree.getroot()

root[0][0][0].text = "Email" 
root[0][0][1].text = "5"

newTag = ET.SubElement(root[1], 'node3')
newTag.attrib["name"] = "Smith"
newTag1 = ET.SubElement(newTag, 'storage')
newTag1.text = "Harddrive"

root[0][0][2].text = "Smith"

tree.write("testWrite.xml")