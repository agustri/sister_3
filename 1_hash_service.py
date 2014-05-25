from ladon.ladonizer import ladonize
import hashlib

class Calculator(object):
	@ladonize(int,int,rtype=int)
	def add(self,a,b):
		return a+b

class Hash(object):
	@ladonize(str,rtype=str)
	def hash_md5(self, text):
		return hashlib.md5(text).hexdigest()
	@ladonize(str,rtype=str)
	def hash_sha1(self, text):
		return hashlib.sha1(text).hexdigest()
	@ladonize(str,rtype=str)
	def hash_sha224(self, text):
		return hashlib.sha224(text).hexdigest()