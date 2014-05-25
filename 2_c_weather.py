import xml.etree.ElementTree as ET
from suds.client import Client

# konversi node dari xml menjadi 'node.tag<spasi>: node.text'
def addnode(node):
	return "{0:23}: {1}\n".format(str(node.tag), str(node.text))

url = 'http://www.webservicex.net/globalweather.asmx?WSDL'
client = Client(url)

xml = client.service.GetWeather('jakarta', 'indonesia').encode('utf-16')
root = ET.fromstring(xml)

#tree = ET.parse('data/c_weather.xml')
#root = tree.getroot()

output = "== Informasi Cuaca ==\n"
for i in root:
	output += addnode(i)
print output