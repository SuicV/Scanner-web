from Connection import connector
from screen import screen
from optparse import OptionParser
from optparse import OptionGroup
from optparse import OptionValueError
from random import choice
from regex import regex

class Scanner_Web_Core (object):
	logos = [(" ___                             __      __   _    \n"
              "/ __| __ __ _ _ _  _ _  ___ _ _  \ \    / /__| |__ \n"
              "\__ \/ _/ _` | ' \| ' \/ -_) '_|  \ \/\/ / -_) '_ \ \n"
              "|___/\__\__,_|_||_|_||_\___|_|     \_/\_/\___|_.__/\n"
              ),
			  ("   ____                             _      __    __ \n"
			   "  / __/______ ____  ___  ___ ____  | | /| / /__ / / \n"
			   " _\ \/ __/ _ `/ _ \/ _ \/ -_) __/  | |/ |/ / -_) _ \ \n"
			   "/___/\__/\_,_/_//_/_//_/\__/_/     |__/|__/\__/_.__/\n"),
			  (
			   "  ()                                        (_|   |   |_/ | |  \n"
			   "  /\  __   __,   _  _    _  _    _   ,_       |   |   | _ | |  \n"
			   " /  \/    /  |  / |/ |  / |/ |  |/  /  |      |   |   ||/ |/ \_\n"
			   "/(__/\___/\_/|_/  |  |_/  |  |_/|__/   |_/     \_/ \_/ |__/\_/ \n")]

	googleDot = ["com", "ac", "com.om", "ad", "ae", "com.af", "com.ag", "com.ai", "am", "it.ao", "com.ar", "cat", "as", "at", "com.au", "az", "ba",
                "com.bd", "be", "bf", "bg", "com.bh", "bi", "bj", "com.bn", "com.bo", "com.br", "bs", "co.bw", "com.by", "com.bz", "ca", "com.kh",
    	        "cc", "cd", "cf", "cn", "com.co", "co.nz", "cg", "ch", "co.ck", "cl", "cm", "cz", "de", "nu", "dj",
                "dk", "dm", "com.do", "dz", "no", "com.ec", "ee", "com.eg", "es", "com.np", "fi", "com.fj", "fm", "fr", "ga", "nl", "ge",
                "gf", "gg", "com.gh", "com.gi", "nr", "gl", "gp", "gr", "com.gt", "com.ni", "gy", "com.hk", "hn", "com.ng",
                "co.id", "iq", "ie", "co.il", "com.nf", "im", "co.in", "is", "it", "ne", "je", "com.jm", "jo", "co.jp", "co.ke", "com.na",
                "kg", "co.kr", "la", "com.lb", "li", "com.my", "co.ls", "lt", "lu", "lv", "com.ly", "com.mx",
                "co.ma", "md", "mg", "mk", "ml", "mn", "ms", "com.mt", "mu", "mv", "com.pa", "com.pe", "com.ph", "com.pk", "pn", "com.pr",
                "ps", "pt", "com.py", "com.qa", "ro", "rs", "ru", "rw", "com.sa", "com.sb", "sc", "se", "com.sg", "sh", "si", "com.sl", "sn", "sm",
                "so", "st", "com.sv", "td", "tg", "co.th", "tk", "tl", "tm", "to", "com.tn", "com.tr", "tt", "com.tw", "co.tz", "com.ua", "co.ug", "co.uk",
                "us", "com.uy", "co.uz", "co.ve", "vg", "co.vi", "vu", "co.za", "co.zm", "co.zw"]

	Forbiden = ['facebook.com', 'twitter.', '.google.','github.', 'linkedin.', 'microsoft.', 'youtube.', 'bing.',"stackoverflow.","teamfortress",
                'yahoo.', 'sogou.', 'ask.', 'yandex.', 'msn.', 'w3school.', 'windows.', 'adobe.com', 'outlook.',"laravel.","wordpress.","w3schools"
                 'window.', 'JQuery.min', 'hotmail.', 'yandex.','sogou.', 'bing','php.net', 'mysql.', 'microsofttranslator.','amazon.', 'www.asp.net',
                 "devdocs.","steampowered.","origin.","adsense.google.","linuxmint.","ubuntu.","debian.","arch-linux.","w3schools.com"]
	pageAdmins = ["/admin/", "/admin/login.php", "/myadmin/", "/acceso/", "/administrator/", "/admin1/", "/admin2/", "/wp-admin/login.php",
                 "/administrator/index.php", "/admin3/", "/admin4/", "/admin5/", "/usuarios/", "/usuario/", "/administrador/", "/administrateur/",
                 "/moderator/", "/webadmin/", "/adminarea/", "/bb-admin/", "/adminLogin/", "/admin_area/", "/panel-administracion/",
                 "/instadmin/", "/memberadmin/", "/administratorlogin/", "/adm/", "/wp-login.php", "/admin/account.php", "/admin/index.php",
                 "/admin/admin.php", "/admin/account.php", "/admin_area/admin.php", "/admin_area/login.php", "/siteadmin/login.php", "/siteadmin/index.php",
                 "/siteadmin/login.html", "/admin/account.html", "/admin/index.html", "/admin/login.html", "/admin/admin.html", "/admin_area/index.php",
                 "/bb-admin/index.php", "/bb-admin/login.php", "/bb-admin/admin.php", "/admin/home.php", "/admin_area/login.html", "/admin_area/index.html",
                 "/admin/controlpanel.php", "/admin.php", "/admincp/index.asp", "/admincp/login.asp", "/admincp/index.html", "/admin/account.html", "/administracion",
                 "/adminpanel.html", "/webadmin.html", "/webadmin/index.html", "/webadmin/admin.html", "/webadmin/login.html", "/admin/admin_login.html",
                 "/admin_login.html", "/panel-administracion/login.html", "/admin/cp.php", "/cp.php", "/administrator/index.php", "/administrator/login.php",
                 "/nsw/admin/login.php", "/webadmin/login.php", "/admin/admin_login.php", "/admin_login.php", "/administrator/account.php", "/administrator.php",
                 "/admin_area/admin.html", "/pages/admin/admin-login.php", "/admin/admin-login.php", "/admin-login.php", "/bb-admin/index.html", "/bb-admin/login.html",
                 "/acceso.php", "/bb-admin/admin.html", "/admin/home.html", "/login.php", "/modelsearch/login.php", "/moderator.php", "/moderator/login.php",
                 "/moderator/admin.php", "/account.php", "/pages/admin/admin-login.html", "/admin/admin-login.html", "/admin-login.html", "/controlpanel.php",
                 "/admincontrol.php", "/admin/adminLogin.html", "/adminLogin.html", "/admin/adminLogin.html", "/home.html", "/rcjakar/admin/login.php",
                 "/adminarea/index.html", "/adminarea/admin.html", "/webadmin.php", "/webadmin/index.php", "/webadmin/admin.php", "/admin/controlpanel.html",
                 "/admin.html", "/admin/cp.html", "/cp.html", "/adminpanel.php", "/moderator.html", "/administrator/index.html", "/administrator/login.html",
                 "/user.html", "/administrator/account.html", "/administrator.html", "/login.html", "/modelsearch/login.html", "/moderator/login.html",
                 "/adminarea/login.html", "/panel-administracion/index.html", "/panel-administracion/admin.html", "/modelsearch/index.html", "/modelsearch/admin.html",
                 "/admincontrol/login.html", "/adm/index.html", "/adm.html", "/moderator/admin.html", "/user.php", "/account.html", "/controlpanel.html",
                 "/admincontrol.html", "/panel-administracion/login.php", "/wp-login.php", "/adminLogin.php", "/admin/adminLogin.php", "/home.php",
                 "/admin.php", "/adminarea/index.php", "/adminarea/admin.php", "/adminarea/login.php", "/panel-administracion/index.php",
                 "/panel-administracion/admin.php", "/modelsearch/index.php", "/modelsearch/admin.php", "/admincontrol/login.php", "/adm/admloginuser.php",
                 "/admloginuser.php", "/admin2.php", "/admin2/login.php", "/admin2/index.php", "/adm/index.php", "/adm.php",
				 "/affiliate.php", "/adm_auth.php", "/memberadmin.php", "/administratorlogin.php"]

	cmsTags = {"wordpress":["<a href=\"https:\/\/wordpress.org\/\">Proudly powered by WordPress", "<meta name=\"generator\" content=\"WordPress", "\/wp-content\/(.*).js","wordpress/plugins"],
    		"joomla" : ["<meta name=\"generator\" content=\"Joomla"]}

	def __init__(self) :
		self.version = 1.4
		self.scanTitles = {"u":"URL SCAN","d":"DORK SEARCH","md5":"MD5 ENCRYPTATION"}
		self.sc = screen()
		self.connector = connector()
		self.engins = {"google":"http://www.google.{}/search?q={}&start={}",
					   "bing":"http://www.bing.com/search?q={}&first={}",
					   }
		self.url =""
		self.urlFound = []
		self.regex = regex()

	"""
	Method prepareEngin (self, dork)
		return  String ==> url of engin for Dork search
	"""
	def prepareEngin(self, dork,page):
		"""
		param dork string dork to add it to url engin 
		"""
		engin = self.options.get("engin").lower()
		if engin in ["bing"] :
			return self.engins.get(engin).format(dork,page)
		else :
			domain = choice(self.googleDot)
			return self.engins.get(engin).format(domain,self.connector.queryEncode(dork),page)
	
	"""
	Method searchDork (self, enginUrl)
		return search dork result after passing self.connecto.connection(urlEngin) to getDorkResutls method 
	"""
	def searchDork(self,enginUrl):
		"""
		param enginUrl string 
		"""
		enginResponse = self.connector.connection(enginUrl)
		try :
			return self.getDorkResults(   enginResponse.response.read().decode("utf-8","ignore")   )
		except Exception :
			pass
	"""
	Method getDorkResults(self, html)
		return self.urlFound after filtring html code passed by searchDork and engin used
	"""
	def getDorkResults (self,html):
		"""
		param html string html code  
		"""
		engin = self.options.get("engin").lower()
		if engin == "bing":
			result = self.regex.findRegex(r'<h2><a href="(.*?)" h="',html)
		elif engin == "google":
			result = self.regex.findRegex(r'<h3 class="r"><a href="(.*?)"', html)
			
		for url in result :
			if self.isForbiden(url) is False and url not in self.urlFound :
				self.urlFound.append(url) 
		return self.urlFound
	
	"""
	Method isForbiden(self, url)
		check if the domain is forbiden 
		return False if url is not Forbiden True else
	"""
	def isForbiden(self,url):
		"""
		param url String 
		"""
		for forbiden in self.Forbiden :
			if forbiden in connector.parser(url).netloc :
				return True
		return False
	
	"""
	Method cmsDetector(self, hmtl)
		look for self.cmsTags in the html code
		return detected cms if true or not detected if is not detected
	"""
	def cmsDetector(self, html):
		"""
		param html string html code after connecting to target
		"""
		for cms in self.cmsTags.keys():
			for cmsTag in self.cmsTags.get(cms):
				if cmsTag in html:
					return cms
		return "not detected"
	
	"""
	Method pageSearcher(self, url)
		check if url is exist using method connetion.isExist in class connector after parse it 
		retur url if is found and False if is not found 
	"""
	def pageSearcher(self,url, urls):
		"""
		param urls string
		"""
		parsedUrl = self.connector.parser(url)
		for path in urls:
			fullUrl = parsedUrl.scheme +"://"+ parsedUrl.netloc + path
			self.sc.prInfo("Looking for",fullUrl,rtn=True)

			if self.connector.isExist(self.connector.connection(fullUrl).status):
					return fullUrl
		return False

	"""
	Method validation (self,validation,html)
		return true if validation param found in the html code and False else
	"""
	def validation (self,validation,html):
		"""
		param validation, html String
		"""
		if validation in html :
			return True
		return False
	"""
	Method updtaeCecker(self)
		return True if a new version is available or False if not 
	"""
	def updateChecker(self):
		getVersion = self.regex.findRegex(r"<!-- Version (\d+\.\d+) -->",str(self.connector.connection("https://raw.githubusercontent.com/SuicV/Scanner-web/master/README.md").response.read()))[0]
		if float(getVersion) > self.version :
			return True
		return False
