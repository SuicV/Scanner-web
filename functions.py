from socket import gethostbyname
from Connection import connector
from ScannerWebCore import Scanner_Web_Core
from regex import regex
from vulnerability import vuln
from collections import Counter
from socket import getservbyport
from math import floor

pp = ["Status","Server","HTTP Version","Ip","Cms","Time Out","Validation","X-Powered-By","Regex","Tcp Ports","Udp Ports","Sql Injection","Page Admin","External Command"]

def getHttp(code):
	if code == 10 :
		return "HTTP/1.0"
	return "HTTP/1.1"

def openedPortsString(opendports):
	string =""
	for port in opendports :
		try :
			string += str(port) + " [ "+getservbyport(port)+" ] "
		except OSError :
			pass
	return string
def getLists(file):
	List = []
	for line in open(file,"r").readlines():
		List.append(line[:-1])
	return List 
def dorkSearch(dork, core,sc):

	for page in range(10,core.options.get("pages")*10+10,10):
		print(" "*sc.termenalSize().columns,end="\r")
		sc.prInfo(sc.getColor("cyan")+"Scanning page ==>",sc.getColor("bold_yellow")+str(floor(page/10)),rtn=True)	
		enginUrl = core.prepareEngin(dork,page)
		results = core.searchDork(enginUrl)
	return results
def startScannig(connection,sc,options,urls,proxy=None):
	
	core = Scanner_Web_Core()
	Regex = regex()
	vulna = vuln(connection)
	scannResults = {}
	
	for urlNu , url in enumerate(urls) :
		
		print("-"*20)
		sc.prDanger("Url Num",str(urlNu+1)+"/"+str(len(urls)))
		print("-"*20)
		sc.prInfo("Url",sc.getColor("blue")+url)

		#CHECK TIME OUT 
		timeout=options.get("timeout")

		# SET PROXY 
		if proxy:
			resp = connection.connection(url, proxy,timeout=timeout)
			scannResults["Proxy"] = proxy
		else :
			resp = connection.connection(url,timeout=timeout)
		
		# IF AN ERROR 
		if resp.response is  None: 
			scannResults["Error"]              = str(resp.error)
			printScaningResult(sc,scannResults)
		# IF NOT 
		else :

			scannResults["Error"]              = None
			scannResults["htmlResponse"]       = resp.response.read().decode("utf-8", "ignore")
			scannResults["HTTP Version"]       = getHttp(resp.response.version)
			scannResults["Status"]             = str(resp.response.status) + " " +resp.response.reason 
			scannResults["X-Powered-By"]	   = resp.response.getheader("X-Powered-By")
			
			# GET INFO ABOUT SERVER IF --noInfo not used
			if options.get("info") is False :
				scannResults["Server"]         = resp.response.getheader("Server")
				if regex().isIpV4(connector.parser(url).netloc) is False :
					scannResults["Ip"]         = gethostbyname( connector.parser(url).netloc )
				else :
					scannResults["Ip"]         = connector.parser(url).netloc
				scannResults["Cms"]            = core.cmsDetector( scannResults["htmlResponse"] ).upper()
			
			# VALIDATION --validation 
			if options.get("validation"):
				if core.validation(options.get("validation"),scannResults["htmlResponse"]):
					scannResults["Validation"] = sc.getColor("green")+"Found"
				else :
					scannResults["Validation"] = sc.getColor("red")+"Not Found"
			
			# TIME OUT
			if options.get("timeout") is not 30:
				scannResults["Time Out"]       = options.get("timeout")
			
			# REGEX 
			if options.get("regex") :
				results = Regex.findRegex(options.get("regex"),scannResults["htmlResponse"])
				flilResults = ""
				if results != [] :
					counter = Counter(results)
					for key in counter.keys() :
						flilResults += str(key) + " |["+str(counter.get(key))+"]| "
					scannResults["Regex"]      = sc.getColor("green")+flilResults
				else :
					scannResults["Regex"]      = sc.getColor("red")+"Matched Regex Not Found"
			# SCANNING TCP PORTS 
			if options.get("tcp-ports") :
				openedports = connection.tcpScan(sc,url)
				result = openedPortsString(openedports)
				
				scannResults["Tcp Ports"]      = sc.getColor("green")+result
			
			# SCANNIG UDP PORTS
			if options.get("udp-ports") :
				openedports = connection.udpScan(sc,url)
				result = openedPortsString(openedports)
				scannResults["Udp Ports"]      = sc.getColor("green")+result
			
			# LOOK FOR SQL INJECTION ERROR
			if options.get("sql"):
				sc.prInfo("Scanning","Sql-Injection",rtn=True)
				scanSqlResponse = vulna.sqlInjection(url)
				if scanSqlResponse is True :
					scannResults["Sql Injection"] = sc.getColor("green")+"Error Found"
				else :
					scannResults["Sql Injection"] = sc.getColor("red")+vulna.sqlInjection(url)
			
			# FIND PAGE ADMIN
			if options.get("adminPage") :
				adminpage = core.pageSearcher(url, core.pageAdmins)
				if adminpage :
					scannResults["Page Admin"] = sc.getColor("green")+adminpage
				else : 
					scannResults["Page Admin"] = sc.getColor("red")+"Not found"		
			
			# PRINT RESULTS
			printScaningResult(sc , scannResults)
def printScaningResult(sc, scannResults):
	# REMOVE LAST LINE FROM TERMENAL
	print(" "*sc.termenalSize().columns,end="\r")
	global pp

	if scannResults["Error"] is not None :
		sc.prSubInfo("Error",scannResults["Error"])
	else : 
		for info in pp :
			if info in scannResults and scannResults[info] is not None :
				sc.prSubInfo(info , scannResults[info])	
