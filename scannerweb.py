from screen import screen
from hasher import hasher
from ScannerWebCore import Scanner_Web_Core
from os import getcwd
from platform import platform
from functions import startScannig, getLists, dorkSearch
from Connection import connector
from cmdparser import buildArgvSys

if __name__ == "__main__":

	# SETUP
	try :
		options = buildArgvSys()
		con = connector()
		core = Scanner_Web_Core(con)
		core.options = options
		sc = screen(logos = Scanner_Web_Core.logos)
		print(sc.getColor("bold_green"))
		# BANNER
		sc.prLogo()

		print(":"*sc.termenalSize().columns)

		sc.prInfo("Developper",sc.getColor("bold_red")+"SuicV")
		sc.prInfo("Directory",getcwd())
		sc.prInfo("System",sc.getColor("green")+platform())
		sc.prInfo("Version",sc.getColor("yellow")+str(core.version))
		print("-"*sc.termenalSize().columns)

		# CHECK CONNECTION TO THE PROXY
		if options.get("proxy") :
			sc.prInfo("Checking Porxy",options.get("proxy"))

			if con.checkProxy(options.get("proxy")) == False :
				sc.prDanger("Error",sc.getColor("red")+"Connection To Proxy Is Faild")
				exit()
			else : 
				sc.prInfo("Success",sc.getColor("green")+"Connection To Proxy Is Succeed")

		#  CHECK FOR UPDATES
		if options.get("update"):
			
			sc.prInfo("PROCCESS","Look for updates")
			if core.updateChecker():
				sc.prDanger("Resulte",sc.getColor("red")+"There are a new version available, download it and enjoy !",4)
			else :
				sc.prSubInfo("Resulte",sc.getColor("green")+"No new version available",4)
			exit()

		# BASE 64 ENCRYPTATION
		if options.get("base64Encr"):

			sc.prInfo("PROCESS","Encrypt base64")
			sc.prSubInfo("STRING",options.get("base64Encr"))
			sc.prSubInfo("Base64 encypted",hasher.base64Encr(options.get("base64Encr")))

		# BASE 64 DECRYPTATION
		if options.get("base64Decr"):

			sc.prInfo("PROCESS","Encrypt base64")
			sc.prSubInfo("BASE64",options.get("base64Decr"))
			sc.prSubInfo("Base64 Decrypted",hasher.base64Decr(options.get("base64Decr")))

		# MD5 ENCRYPTATION
		if options.get("md5Enc"):
			sc.prInfo("PROCESS","Decrypt md5")
			sc.prSubInfo("STRING",options.get("md5Enc"))
			sc.prSubInfo("Hash encypted",hasher.md5Encr(options.get("md5Enc")))

		# SCAN URL
		if options.get("url"):
			urls = []
			sc.prInfo("SCAN TYPE",core.scanTitles.get("u"))
			if type(options.get("url")) is dict :
				for url in getLists(options.get("url").get("List")) :
					if core.isForbiden(url) != True:
						urls.append(url)
			else : 
				urls.append(options.get("url"))
			if len(urls) == 0 :
				sc.prDanger("Error",sc.getColor("red")+"Urls not found or is forbiden")
				exit()
			startScannig(core,options,urls,options.get("proxy"))
			print("-"*sc.termenalSize().columns)

		# SEARCH DORK AND SCANN RESULTS 
		if options.get("dork"):
			
			sc.prInfo("SCAN TYPE", core.scanTitles.get("d"))
			engins = options.get("engin").split("|")
			for engin in engins :
				core.urlFound = []
				engin = engin.lower().strip()
				sc.prDanger("Engin", engin.title())

				# WHEN USER SET A FILE
				if type(options.get("dork")) is dict :
					dorks = getLists(options.get("dork").get("List"))
					sc.prInfo("Number of Dork found",len(dorks))
					for dork in dorks :
						core.urlFound = []
						# PRINTING CURRENT DORK SCANING 
						print(sc.getColor("bold_yellow"),"-"*(sc.termenalSize().columns-2),sc.restarColor)
						sc.prInfo("DORK",dork)
						print(sc.getColor("bold_yellow"),"-"*(sc.termenalSize().columns-2),sc.restarColor)
						
						# GETTING URLS TO SCAN
						urlsFound = dorkSearch(dork,core,options.get("pages"), engin)
						print(" "*sc.termenalSize().columns,end="\r")
						
						startScannig(core, options, urlsFound, options.get("proxy"))

				else : 
					print(sc.getColor("bold_yellow"),"-"*(sc.termenalSize().columns-2),sc.restarColor)
					sc.prInfo("DORK",options.get("dork"))
					print(sc.getColor("bold_yellow"),"-"*(sc.termenalSize().columns-2),sc.restarColor)

					urlsFound = dorkSearch(options.get("dork"),core,options.get("pages"), engin)
					print(" "*sc.termenalSize().columns,end="\r")

					startScannig(core, options, urlsFound, options.get("proxy"))			

		# END OF SCRIPT
		sc.clearLine()
		print(sc.getColor("red"),"-"*(sc.termenalSize().columns-1))
	except KeyboardInterrupt :
		print(sc.getColor("red"),"-"*15," SCAN STOPED ","-"*15,sc.restarColor)

	print(sc.getColor("bold_green")+"[ENJOY!]"+sc.restarColor)