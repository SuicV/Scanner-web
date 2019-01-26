from socket import gethostbyname
from socket import getservbyport
from Connection import connector
from ScannerWebCore import Scanner_Web_Core
from regex import regex
from vulnerability import vuln
from collections import Counter
from math import floor
from os import system

pp = ["Status","Server","HTTP Version","Ip","Cms","Time Out","Validation","X-Powered-By","Regex","Tcp Ports","Udp Ports","Sql Injection","External Command"]
core = Scanner_Web_Core()
Regex = regex()
connection = connector()
vulna = vuln(connection)

def getHttp(code):
	if code == 10 :
		return "HTTP/1.0"
	return "HTTP/1.1"

"""
@func to form a string of opened ports to print on screen
@return string
"""
def openedPortsString(opendports):
	string =""
	for port in opendports :
		try :
			string += str(port) + " [ "+getservbyport(port)+" ] "
		except OSError :
			string += str(port) +" [ Service Not Found ] " 
	return string
"""
@func to get dorks or urls from the passed file in arguments -u or -d 
@return {List} of urls or dorks
"""
def getLists(file):
	List = []
	for line in open(file,"r").readlines():
		List.append(line[:-1])
	return List 

def dorkSearch(dork, core, sc, pages):

	for page in range(10,pages*10+10,10):
		print(" "*sc.termenalSize().columns,end="\r")
		sc.prInfo(sc.getColor("cyan")+"Scanning page :",
				  sc.getColor("bold_yellow")+str(floor(page/10)),rtn=True)	
		enginUrl = core.prepareEngin(dork,page)
		results = core.searchDork(enginUrl)
	return results
	
def startScannig(sc,options,urls,proxy=None):

	scannResults = {}
	serverScannedTcp = []
	serverScannedUdp = []

	for urlNu , url in enumerate(urls) :
		
		print("-"*20)
		sc.prDanger("Url Num",str(urlNu+1)+"/"+str(len(urls)))
		print("-"*20)
		sc.prInfo("Url",sc.getColor("blue")+url)
		
		timeout=options.get("timeout")

		print(sc.getColor("bold_green")+" Connecting ..."+sc.restarColor, end="\r")

		# SET PROXY 
		if proxy:
			resp = connection.connection(url, proxy,timeout=timeout)
			scannResults["Proxy"] = proxy
		else :
			resp = connection.connection(url,timeout=timeout)
		
		# IF AN ERROR 
		if resp.response is  None: 
			scannResults["Error"]              = str(resp.error)+str(resp.status)
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
				print(sc.getColor("bold_green")+" Geting information ..."+sc.restarColor, end="\r")
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
				openedports = connection.tcpScan(sc,url,serverScannedTcp)
				if openedports != False :
					result = openedPortsString(openedports)
					scannResults["Tcp Ports"]      = sc.getColor("green")+result
					serverScannedTcp.append(connector.parser(url).netloc)

				else : 
					scannResults["Tcp Ports"]      = sc.getColor("red")+"this server already scanned"
				
			# SCANNIG UDP PORTS
			if options.get("udp-ports") :
				openedports = connection.udpScan(sc,url,serverScannedUdp)
				if openedports != False :
					result = openedPortsString(openedports)
					scannResults["Udp Ports"]      = sc.getColor("green")+result
					serverScannedUdp.append(connector.parser(url).netloc)

				else :
					scannResults["Udp Ports"]      = sc.getColor("red")+"this server already scanned"
			
			# LOOK FOR SQL INJECTION ERROR
			if options.get("sql"):
				sc.prInfo("Scanning","Sql-Injection",rtn=True)
				scanSqlResponse = vulna.sqlInjection(url)
				if scanSqlResponse is True :
					scannResults["Sql Injection"] = sc.getColor("green")+"Error Found"
				else :
					scannResults["Sql Injection"] = sc.getColor("red")+vulna.sqlInjection(url)
			
			# PRINT RESULTS
			printScaningResult(sc , scannResults)

			# SAVE RESULSTS
			if options.get("save") :
				saveResults(scannResults, options.get("save"),url)
			
			# EXTERNAL COMMAND 
			if options.get("external-command"):
				command = externalCommand( options.get("external-command"), url, scannResults["Ip"])
				sc.prSubInfo("External-command",sc.getColor("green")+command)
				system(command)

"""
@func to print results passed in scannResults parameter
"""
def printScaningResult(sc, scannResults):
	# REMOVE LAST LINE FROM TERMENAL
	print(" "*sc.termenalSize().columns,end="\r")
	if scannResults["Error"] is not None :
		sc.prSubInfo("Error",scannResults["Error"])
	else : 
		for info in pp :
			if info in scannResults and scannResults[info] is not None :
				sc.prSubInfo(info , scannResults[info])

"""
@func to check if a string start with a color and remove it 
@return string without color
"""
def hasColor(value):

	if Regex.findMatch(r'^\x1b[^m]*m',value):
		return value[7:]
	return value
"""
@func to save results 
"""
def saveResults(scannResults,file,url):
	file = open(file,'a')
	file.writelines("::[{}]::\n".format(url))
	for value in scannResults.keys():
		if value != "htmlResponse" and scannResults[value] is not None:
			file.writelines("\t{} : {}\n".format(value,hasColor(scannResults[value])))
	file.close()
"""
@func to prepare the externale command by replacing flags with there values
@return command to run 
"""
def externalCommand(command,url,ip):
	if "--HOST" in command:
		command = command.replace("--HOST",connection.parser(url).netloc)
	if "--IP" in command : 
		if  ip :
			command = command.replace("--IP",ip)
		else :
			command = command.replace("--IP",connection.getIp(url))
	return command