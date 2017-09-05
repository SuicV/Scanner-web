import re
class regex(object):
	Ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
	Url = r"^http[s]?://[A-z0-9.]+.[A-z]{1,4}"
	File = r"([A-z0-9]+\.[A-z]+)"
	List = r'^([A-z]://)+?([A-z0-9\-_/\s]+)([A-z0-9\s\-_]+\.txt)$|/?([A-z0-9\-_/\s]+)([A-z0-9\s\-_]+\.txt)$'
	
	"""
	Method isIpV4(String)
		check if there an ipV4 in String
	"""
	def isIpV4(self,String):
		if re.match(self.Ip,String) is None :
			return False
		return True

	"""
	Method getIpsV4(self,String)
		return Ipsv4 if it's exist in the passed String  
	"""
	def getIpsV4(self,String):
		if isIpV4(String) : 
			return re.findall(self.Ip,String)
	
	"""
	Method isPath(self,String):
		return True if String passed is a path and False if is not a path
	"""
	def isPath(self,String):
		if re.match(self.List,String) is None :
			return False
		return True
	
	"""
	Method isPath(self,String):
		return True if String passed is a url and False if is not a url
	"""
	def isUrl(self,String):
		if re.match(self.Url,String) is None :
			return False
		return True
	"""
	Method findRegex(slef,pattern,string)
		return list of matched regex
	"""
	def findRegex(self,pattern,string):
		return re.findall(pattern,string)

	def findMatch(self,pattern,string):
		if re.match(pattern,string) is None :
			return False
		return True