import xml.etree.ElementTree as ET
# import codecs

f = open("drink.xml", encoding = "UTF - 8")
data = f.read()
tree = ET.ElementTree(ET.fromstring(data))
root = tree.getroot()
# print(root.tag)

for child in root:
    print("tag : " + child.tag , child.text)
f.close()