import hashlib
import base64
class hasher(object):
	
	"""
	Method md5Encr(hash)
		return md5 string of the passed argument 
	"""
	@staticmethod
	def md5Encr(hash):
		return hashlib.md5(hash.encode("utf-8")).hexdigest()
	
	"""
	Method base46Encr(text)
		return base64 string of string passed
	"""
	@staticmethod
	def base64Encr(text):
		return base64.encodebytes(text.encode('ascii')).decode("utf-8")
	"""
	Method base64Decr(text)
		return string decrypted base64
	"""
	@staticmethod
	def base64Decr(text):
		return base64.decodebytes(text.encode('ascii')).decode("utf-8")