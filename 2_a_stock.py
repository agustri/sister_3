import xml.etree.ElementTree as ET
from suds.client import Client

# konversi node dari xml menjadi 'node.tag<spasi>: node.text'
def addnode(node):
	return "{0:23}: {1}\n".format(str(node.tag), str(node.text))

url = 'http://www.webservicex.net/stockquote.asmx?WSDL'
client = Client(url)
#print client

xml = client.service.GetQuote('TLK')
root = ET.fromstring(xml)

# Test xml hasil
#tree = ET.parse('data/a_stock.xml')
#root = tree.getroot()

output = "== Informasi Saham ==\n"
for i in root[0]:
	output += addnode(i)

print output
