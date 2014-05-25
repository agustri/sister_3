from suds.client import Client

url = 'http://localhost:8080/Hash/soap/description'
client = Client(url)

text = raw_input("Masukkan text yg akan di-hash :")

print "\n"
print "Text  :{0}".format(text)
print "md5   :{0}".format(client.service.hash_md5(text))
print "sha1  :{0}".format(client.service.hash_sha1(text))
print "sha224:{0}".format(client.service.hash_sha224(text))
