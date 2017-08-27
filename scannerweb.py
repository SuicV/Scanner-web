from screen import screen
from hasher import hasher
from ScannerWebCore import Scanner_Web_Core
from os import getcwd
from platform import platform
from functions import startScannig, getLists, dorkSearch
from Connection import connector

if __name__ == "__main__":
	
	# SETUP
	try :
		core = Scanner_Web_Core()
		con = connector()
		sc = screen(logos = Scanner_Web_Core.logos)
		core.buildArgvSys()
		print(sc.getColor("bold_green"))

		sc.prLogo()

		print(":"*sc.termenalSize().columns)

		sc.prInfo("Developper",sc.getColor("bold_red")+"SuicV")
		sc.prInfo("Directory",getcwd())
		sc.prInfo("System",sc.getColor("green")+platform())
		sc.prInfo("Version",sc.getColor("yellow")+str(core.version))
		print("-"*sc.termenalSize().columns)

		# CHECK CONNECTION TO THE PROXY
		if core.options.get("proxy") :
			sc.prInfo("Checking Porxy",core.options.get("proxy"))
			
			if con.checkProxy(core.options.get("proxy")) == False :
				sc.prDanger("Error",sc.getColor("red")+"Connection To Proxy Is Faild")
				exit()
			else : 
				sc.prInfo("Success",sc.getColor("green")+"Connection To Proxy Is Succeed")
		
		#  CHECK FOR UPDATES
		if core.options.get("update"):
			
			sc.prInfo("PROCCESS","Look for updates")
			if core.updateChecker():
				sc.prDanger("Resulte",sc.getColor("red")+"There are a new version available, download it and enjoy !",4)
			else :
				sc.prSubInfo("Resulte",sc.getColor("green")+"No new version available",4)
			exit()

		# BASE 64 ENCRYPTATION
		if core.options.get("base64Encr"):
			
			sc.prInfo("PROCCESS","Encrypte base64")
			sc.prSubInfo("BASE64",core.options.get("base64Encr"))
			sc.prSubInfo("Base64 encypted",hasher.base64Encr(core.options.get("base64Encr")))
		
		# BASE 64 DECRYPTATION
		if core.options.get("base64Decr"):

			sc.prInfo("PROCCESS","Encrypte base64")
			sc.prSubInfo("BASE64",core.options.get("base64Decr"))
			sc.prSubInfo("Base64 Decrypted",hasher.base64Decr(core.options.get("base64Decr")))

		# MD5 ENCRYPTATION
		if core.options.get("md5Enc"):
			sc.prInfo("PROCCESS","Decrypte md5")
			sc.prSubInfo("STRIGN",core.options.get("md5Enc"))
			sc.prSubInfo("Hash encypted",hasher.md5Encr(core.options.get("md5Enc")))

		# SCAN URL
		if core.options.get("url"): 
			sc.prInfo("SCAN TYPE",core.scanTitles.get("u"))
			if type(core.options.get("url")) is dict :
				urls = getLists(core.options.get("url").get("List"))
			else : 
				urls = [core.options.get("url")]
			startScannig(connector(),sc,core.options,urls,core.options.get("proxy"))
			print("-"*75)

		# SEARCH DORK AND SCANN RESULTS 
		if core.options.get("dork"):
			
			sc.prInfo("SCAN TYPE",core.scanTitles.get("d"))
			sc.prDanger("Engin",core.options.get("engin").title())
			
			# WHEN USER SET A FILE
			if type(core.options.get("dork")) is dict :
				dorks = getLists(core.options.get("dork").get("List"))
				sc.prInfo("Number of Dork found",len(dorks))
				for dork in dorks :
					print(sc.getColor("bold_yellow"),"-"*(sc.termenalSize().columns-2),sc.restarColor)
					sc.prInfo("DORK",dork)
					print(sc.getColor("bold_yellow"),"-"*(sc.termenalSize().columns-2),sc.restarColor)
					urlsFound = dorkSearch(dork,core,sc)
					print(" "*sc.termenalSize().columns,end="\r")
					startScannig(con,sc, core.options,urlsFound,core.options.get("proxy"))	
			else : 
				print(sc.getColor("bold_yellow"),"-"*(sc.termenalSize().columns-2),sc.restarColor)
				sc.prInfo("DORK",core.options.get("dork"))
				print(sc.getColor("bold_yellow"),"-"*(sc.termenalSize().columns-2),sc.restarColor)
				
				urlsFound = dorkSearch(core.options.get("dork"),core,sc)
				print(" "*sc.termenalSize().columns,end="\r")

				startScannig(con,sc, core.options,urlsFound,core.options.get("proxy"))			
		# END OF SCRIPT
		print(sc.getColor("red"),"-"*(sc.termenalSize().columns-1))
		print(sc.getColor("bold_green"),"[ ENJOY! ]",sc.restarColor)	
	except KeyboardInterrupt :
		print(sc.getColor("red"),"-"*15," SCAN STOPED ","-"*15,sc.restarColor)
		print(sc.getColor("bold_green"),"[ ENJOY! ]",sc.restarColor)