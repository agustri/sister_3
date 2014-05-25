from suds.client import Client

url = 'http://www.webservicex.net/CurrencyConvertor.asmx?WSDL'
client = Client(url)
# lihat method dan type yg dipakai pada web service
#print client
# melihat struktur type Currency
#currency = client.factory.create('Currency')
#print currency


print "Kurs Dollar ke Rupiah saat ini : Rp. {0}".format(
	client.service.ConversionRate('USD','IDR'))