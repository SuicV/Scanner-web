import urllib.request as request
from urllib.parse import urlparse , quote
import urllib.error
from random import choice
import socket
class connector (object):

	USER_AGENT = ["Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
	]

	ports = [20,21,22,23,24,25,35,37,53,80,88,130,135,161,162,443,445,530,546,547,561,
			 1433,1434,1701,1723,2082,2087,2121,2222,3306,3389,8080]
	
	"""
	Method connection(self,url,proxy,timeout)
		this method make a connection to url with proxy if is found 
		return self if connection is succeed and False if is not 
	"""
	def connection(self,url, proxy = None, timeout=30) :
		"""
		params url , proxy String 
		param timeout intiger
		"""
		self.status   = None
		self.error    = None
		self.response = None
		self.url      = None
		self.proxy    = None
		try :
			Request = request.Request(url,headers = {"User-Agent":choice(self.USER_AGENT)})
			if proxy is not None:
				parser = self.parser(proxy)
				Request.set_proxy(parser.netloc,parser.scheme) 
			self.proxy = proxy
			self.url = url
			self.error = None
			self.response = request.urlopen(Request,timeout=int(timeout))
			self.status  = self.response.getcode()
		except urllib.error.HTTPError as error:
			self.status = error.code
			self.error = error.reason
		except urllib.error.URLError as error :
			self.error = error.reason
			self.status = ""
		except socket.timeout :
			self.error = "Time out Error"
		except ValueError :
			self.error = "Unkown url type "
		return self
	
	"""
	Method checkProxy(self,proxy)
	"""
	def checkProxy(self,proxy):
		try :
			Request = request.Request("http://www.github.com",headers={"User-Agent":self.USER_AGENT[0]})
			parser = self.parser(proxy)
			Request.set_proxy(parser.netloc,parser.scheme)
			request.urlopen(Request, timeout = 30)
		except Exception :
			return False 
	"""
	Method isExist(self,status)
		check if a page is exist by passing status code 
	"""
	def isExist(self,status):
		"""
		param status intiger status code 
		"""
		if status in [200,401,403]:
			return True
		elif status == 404 :
			return False
	
	"""
	Method parser(url) 
		return urllib.parse.urlparse parsed url
	"""
	@staticmethod
	def parser(url):
		"""
		param url string url to parse
		"""
		return urlparse(url)

	"""
	Method queryEncode(query)
		encode url query 
		return String urllib.parse.quote 
	"""
	@staticmethod
	def queryEncode(query):
		return quote(query)
	"""
	Method getIp(self,url):
		return String IpV4 of the target
	"""
	def getIp(self,url):
		return socket.gethostbyname(  self.parser(url).netloc  )

	"""
	Method tcpScan(self,sc,target)
		method scan tcp ports
		return list of opened ports or false if no port opened
	"""
	def tcpScan (self, sc, target, serverScanned):

		target = self.parser(target).netloc
		if target not in serverScanned : 
			openedTcp = []
			for port in self.ports :
				socketTcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socketTcp.settimeout(10)
				sc.prInfo("Scann TCP port ",str(port),rtn=True)
				if socketTcp.connect_ex((target, port)) == 0 :
					openedTcp.append(port)
			return openedTcp

		return False
	"""
	Method udpScan(self,sc,target)
		method scan udp ports
		return list of opened ports return false if no port opened
	"""
	def udpScan (self, sc, target, serverScanned):
		target = self.parser(target).netloc
		if target not in serverScanned :
			openedTcp = []
			for port in self.ports :
				socketUdp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				socketUdp.settimeout(10)
				sc.prInfo("Scann UDP port ",str(port),rtn=True)
				if socketUdp.connect_ex((target, port)) == 0 :
					openedTcp.append(port)

			return openedTcp

		return False