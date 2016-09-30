# calling libs
import urllib.request
import urllib.parse
import urllib.error
import re
import time
import socket
import http.client
import sys
import random
import os
import getopt
import base64
import hashlib

############################################################################################################################################################################################################################################################################################################
##
##                 Created by : Suicedal-Virus .
##                
##                   ALL RIGHTS RESERVED 2016
##                    
##           [::] Author   : Driss Oulhbib
##           [::] Facebook : https://www.facebook.com/BarmajiyatTreeZero
##           [::} Github   : https://github.com/Suicedal-Virus
##           |::] Youtube  : https://www.youtube.com/channel/UCRR-0urV992N8hrBBaPmzVA
##
############################################################################################################################################################################################################################################################################################################
############################################################################################################################################################################################################################################################################################################
##    CLASS SCREEN  ==> LOGO && HELP && CLEAR SCREEN
#############

class screen () :

    def __init__ (self, platformUser, argumentProgram):
        # colors 
        if platformUser == "linux" :
            self.Color = ("\033[0;30m", "\033[1;30m", "\033[1;31m", "\033[0;32m", "\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[0;35m",
                            "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;34m")
        else :
            self.Color = ("","","","","","","","","","","","","")

        self.argumentList = ["Url=", "Dork=", "sqlInjection","saveRs", "tcpPorts","udpPorts", "Dir","pageAdmin","wp", "jom",
         "count=", "Base64Decry=", "Base64Encry=", "md5Encry=", "motor=","noInfo", "help", "update"]

        self.dialogTxt = ["","Url", "Ip", "Query", "Shema", "Version", "Server-status","Server", "Server-Ip", "User Agent", "Vulnerability sqlInjection",
         "Motor", "Method"]
        self.scanTitle = ["SEARCH DORK ", "SCAN URL", "ENCRYPT BASE64", "DECRYPT BASE64", "FIND ADMIN PAGE", "MD5 ENCRYPT","CHECK UPDATE"]
        self.platformUser = platformUser
        self.argumentUser = argumentProgram
        self.version = "1.2"
        self.Dork , self.Url, self.Errors , self.base64Encry, self.base64Decry, self.md5Encrypt, self.motor , self.count= "","","","","","",int(0), int(10)
        self.tcpPorts, self.udpPorts, self.getInfo  , self.findAdmin ,  self.sqlFind,  self.wordPress, self.joomla , self.exSqlMap, self.noInfo, self.saveResult, self.update= False, False, False, False, False, False , False, False, False , False, False
        pass

    def Logo(self) :
        #
        #      Random logo for program
        #
        lRandom = random.randrange(0,4)
        provRandom = random.randrange(0,4)
        logo = [("   __________                     ________                   _________\n"
                "  /          /                    |__    __|                 |__     __|\n"
                " /  ________/                        \   \                     /    /\n"
                "|  |                                   \   \                  /    / \n"
                "|  |   uicedal                         |   |       irus      |    |\n"
                "\   \             --------------       |   |                 |    |\n"
                "  \   \______     |            |       |   |                 |    |\n"
                "   \_______  \    |            |       |   |                 |   |\n"
                "           |  |   --------------       \   \                /   /\n"
                "           |  |                         \   \              /   /\n"
                "          /   /                          \   \            /   /\n"
                "  _______/   /                            |   |          |   |\n"
                " /          /                             \   \_________/   /\n"
                "/__________/                               |_______________|\n"
                ),
                ("\t   __________\n"
                " \t /  0 10 001  \ \n"
                "\t|   110 1 0    |\n"
                "\t| ( 0 )  ( 0 ) |\n"
                "\t|   00 1 1 11  |\n"
                "\t|  R . I . P   |\n"
                "\t| you have been|\n"
                "\t|____hacked____|\n"
                "\t \ a b c d e f \ \n"
                "\t  \ g h i j k l \ \n"
                "\t   \_____________\ \n"
                ),
                ("                                                ___________\n"
                 "\t|\                   |°|           \\    /     ||    \ \n"
                 "\t| -------------------| |------------***/     $$$$    |*\n"
                 "\t| ----------------------------------***\     $$$$    |*\n"
                 "\t\/            ||*    ||            //   \_____||____/\n"
                 "\t              || ** //          \n"
                 "\t               \\__//      RPG-7\n"
                ),
                ("\t   \\\///\n"
                 "\t **--------\n"
                 "\t */       \ \n"
                 "\t |   $$$$  |\n"
                 "\t |         |\n"
                 "\t \________/\n"
                 )
                ]
        prov = ["[::] keep calm and hack any thing", "[::] Keep calm and be Black-Hacker",
        "[::] Web site ==> K.O", "[::] UserName Password Found !!!"]
        print(self.Color[2],"\tNO SYSTEM IS SAFE !!!")
        print(self.Color[1],logo[lRandom],"\n",self.Color[2], prov[provRandom])

        print(self.Color[3],"\n [+] usage : python 'scanner Web.py' [OPTIONS] || ",self.dialogTxt[+5]," : ",self.version,"\n")
        print(" [!} Example : python 'scanner Web.py' --Dork [DORK] --wp --pageAdmin\n")

    def help(self):
        ##
        ##      Help and option can use white programme
        ##
        print(self.Color[4],"     [+] Options : \n")
        print(self.Color[-1],"         --Url            ",self.Color[5],":",self.Color[-2],"  url of web-site")
        print(self.Color[-1],"         --Dork           ",self.Color[5],":",self.Color[-2],"  Use dork ")
        print(self.Color[-1],"         --motor          ",self.Color[5],":",self.Color[-2],"  Set your engine ")
        print(self.Color[-1],"                          ",self.Color[5],":",self.Color[-2],"     1 => Sogou  2=> Yandex ")
        print(self.Color[-1],"                          ",self.Color[5],":",self.Color[-2],"     3 => Google  4=> Bing  5 => Ask")
        print(self.Color[-1],"         --sqlInjection   ",self.Color[5],":",self.Color[-2],"  Scan Sql Injection vulnerability")
        print(self.Color[-1],"         --noInfo         ",self.Color[5],":",self.Color[-2],"  Don't show information web-site")
        print(self.Color[-1],"         --tcpPorts       ",self.Color[5],":",self.Color[-2],"  Scan tcp port of server ")
        print(self.Color[-1],"         --udpPorts       ",self.Color[5],":",self.Color[-2],"  Scan udp port of server ")
        print(self.Color[-1],"         --pageAdmin      ",self.Color[5],":",self.Color[-2],"  Find page admin ")
        print(self.Color[-1],"         --count          ",self.Color[5],":",self.Color[-2],"  Number of search engine results")
        print(self.Color[-1],"         --Base64Decry    ",self.Color[5],":",self.Color[-2],"  Decrypt string to base64")
        print(self.Color[-1],"         --Base64Encry    ",self.Color[5],":",self.Color[-2],"  Encrypt string to base64")
        print(self.Color[-1],"         --md5Encry       ",self.Color[5],":",self.Color[-2],"  Encrypt string to md5")
        print(self.Color[-1],"         --wp             ",self.Color[5],":",self.Color[-2],"  Check if the web-site from Word-Press ")
        print(self.Color[-1],"         --jom            ",self.Color[5],":",self.Color[-2],"  Check if the web-site from Joomla")
        print(self.Color[-1],"         --update         ",self.Color[5],":",self.Color[-2],"  Check for update")
        print(self.Color[-1],"         --saveRs         ",self.Color[5],":",self.Color[-2],"  Save results ")
        print(self.Color[-1],"         --help           ",self.Color[5],":",self.Color[-2],"  Help")
        print(self.Color[4],"\n  [!] Examples : ")
        print(self.Color[-2],"       [+]  python scannerWeb.py --Url [SITE YOU WANT SCANNING] --pageAdmin")
        print(self.Color[-2],"       [+]  python scannerWeb.py --Dork [YOUR DORK] --sqlInjection ")


    def checkArgument(self):
        #
        #  Get argument used by user and if it on the list argument of the programme
        #
        try:
            argv = getopt.getopt(argumentuser, shortopts="", longopts=self.argumentList)
            if argv == ([], []):
                self.Errors ="\n  [!] Error : No argument found ."
        except getopt.GetoptError as err:
            argv = [[]]
            self.Errors ="\n Error : {0}".format(err)


        ########################################################################################################################################
        #   checking argument  #################################################################################################################
        for opt, argum in argv[0] :
            if opt == "--Url":
                if "--" in argum or argum == "":
                    self.Errors = "[!] Error : {0} require argument".format(opt)
                self.Url = argum
            elif opt == "--Dork":
                if "--" in argum or argum == "":
                    self.Errors = "[!] Error : {0} require argument".format(opt)
                self.Dork = argum
            elif opt == "--sqlInjection":
                self.sqlFind = True
            elif opt == "--noInfo":
                self.noInfo = True
            elif opt == "--About":
                self.getInfo = True
            elif opt == "--pageAdmin":
                self.findAdmin = True
            elif opt == "--wp":
                self.wordPress = True
            elif opt == "--jom":
                self.joomla = True
            elif opt == "--count":
                try:
                    argum = int(argum)
                    self.count = argum
                except ValueError:
                    self.Errors = "[!] Pleas use integer in option --count"
            elif opt == "--tcpPorts":
                self.tcpPorts = True
            elif opt == "--udpPorts":
                self.udpPorts = True
            elif opt == "--Base64Decry":
                self.base64Decry = argum
            elif opt == "--Base64Encry":
                self.base64Encry = argum
            elif opt == "--md5Encry":
                self.md5Encrypt = argum
            elif opt == "--saveRs" :
                self.saveResult = True
            elif opt == "--motor":
                if "--" in argum :
                    self.Errors = "[!] Error : {0} require argument".format(opt)
                try:
                    argum = int(argum)
                    self.motor = argum
                except ValueError:
                    self.Errors = "[!] Pleas use integer in option --motor"
            elif opt == "--help":
                screen.help(self)
                sys.exit()
            elif opt == "--update":
                self.update = True
        if self.Url and self.Dork:
            self.Errors = "\n[!] You cant use options --Url and --Dork in the same time"

        pass
    def Show(self):
        if self.Errors :
            screen.help(self)
            print(self.Color[2],self.Errors)
            print("\033[0;0m")
            sys.exit()
        pass
############################################################################################################################################################################################################################################################################################################
####    CLASS CONNECTION AND SEARCH DORK AND MORE FUNCTION #################################################################################################################################################################################################################################################
####

class connection(screen):

    browserLang = ["af", "am", "ar-SA", "as", "az-Latn", "be", "bg", "bn-BD", "bn-IN", "bs", "ca", "ca-ES-valencia",
                   "cs", "da", "de", "de-DE", "el", "en-CA", "en-GB", "en-IN", "en-AU", "en-US", "es", "es-ES", "es-US",
                   "es-MX", "et", "eu", "fa", "fi", "fil-Latn", "fr", "fr-FR", "fr-CA", "ga", "gd-Latn", "gl", "gu",
                   "ha-Latn", "he", "hi", "hr", "hu", "hy", "id", "ig-Latn", "is", "it", "it-IT", "ja", "ka", "kk",
                   "km", "kn", "ko", "kok", "ku-Arab", "ky-Cyrl", "lb", "lt", "lv", "mi-Latn", "mk", "ml", "mn-Cyrl",
                   "mr", "ms", "mt", "nb", "ne", "nl", "nl-BE", "nn", "nso", "or", "pa", "pa-Arab", "pl", "prs-Arab",
                   "pt-BR", "pt-PT", "qut-Latn", "quz", "ro", "ru", "rw", "sd-Arab", "si", "sk", "sl", "sq",
                   "sr-Cyrl-BA", "sr-Cyrl-RS", "sr-Latn-RS", "sv", "sw", "ta", "te", "tg-Cyrl", "th", "ti", "tk-Latn",
                   "tn", "tr", "tt-Cyrl", "ug-Arab", "uk", "ur", "uz-Latn", "vi", "zh-Hans", "zh-Hant", "zu"]
    browserLang = random.choice(browserLang)
    userAgents = ['Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.0.10) Gecko/2009042513 Ubuntu/8.04 (hardy) Firefox/3.0.10',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.0.10) Gecko/2009042523 Ubuntu/8.10 (intrepid) Firefox/3.0.10',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.0.11) Gecko/2009060214 Firefox/3.0.11',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.0.11) Gecko/2009060308 Ubuntu/9.04 (jaunty) Firefox/3.0.11 GTB5',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.0.11) Gecko/2009060309 Firefox/3.0.11',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.0.13) Gecko/2009080316 Ubuntu/8.04 (hardy) Firefox/3.0.13',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.0.18) Gecko/2010021501 Ubuntu/9.04 (jaunty) Firefox/3.0.18',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.0.19) Gecko/2010040118 Ubuntu/8.10 (intrepid) Firefox/3.0.19 GTB7.1',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.0.2', 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.1.15) Gecko/20101027 Fedora/3.5.15-1.fc12 Firefox/3.5.15',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 GTB5', 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.1.6) Gecko/20091215 Ubuntu/9.10 (karmic) Firefox/3.5.6 GTB6',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.2.11) Gecko/20101013 Ubuntu/10.10 (maverick) Firefox/3.6.10',
                 'Mozilla/5.0 (X11; U; Linux i686; {0}; rv:1.9.2.12) Gecko/20101027 Ubuntu/10.10 (maverick) Firefox/3.6.12 GTB7.1']

    ########################################################################################################################################
    ## CREATE USER AGENT#####################################################################################################################
    userAgent = random.choice(userAgents).format(browserLang)

    googleDomainName = ["com", "ac", "com.om", "ad", "ae", "com.af", "com.ag", "com.ai", "am", "it.ao", "com.ar", "cat", "as", "at", "com.au", "az", "ba",
                        "com.bd", "be", "bf", "bg", "com.bh", "bi", "bj", "com.bn", "com.bo", "com.br", "bs", "co.bw", "com.by", "com.bz", "ca", "com.kh",
                        "cc", "cd", "cf", "cn", "com.co", "co.nz", "cg", "ch", "ci", "co.ck", "cl", "cm", "co.cr", "com.cu", "cv", "cz", "de", "nu", "dj",
                        "dk", "dm", "com.do", "dz", "no", "com.ec", "ee", "com.eg", "es", "com.et", "com.np", "fi", "com.fj", "fm", "fr", "ga", "nl", "ge",
                        "gf", "gg", "com.gh", "com.gi", "nr", "gl", "gm", "gp", "gr", "com.gt", "com.ni", "gy", "com.hk", "hn", "hr", "ht", "com.ng", "hu",
                        "co.id", "iq", "ie", "co.il", "com.nf", "im", "co.in", "io", "is", "it", "ne", "je", "com.jm", "jo", "co.jp", "co.ke", "com.na", "ki",
                        "kg", "co.kr", "com.kw", "kz", "co.mz", "la", "com.lb", "com.lc", "li", "lk", "com.my", "co.ls", "lt", "lu", "lv", "com.ly", "com.mx",
                        "co.ma", "md", "me", "mg", "mk", "mw", "ml", "mn", "ms", "com.mt", "mu", "mv", "com.pa", "com.pe", "com.ph", "com.pk", "pn", "com.pr",
                        "ps", "pt", "com.py", "com.qa", "ro", "rs", "ru", "rw", "com.sa", "com.sb", "sc", "se", "com.sg", "sh", "si", "sk", "com.sl", "sn", "sm",
                        "so", "st", "com.sv", "td", "tg", "co.th", "tk", "tl", "tm", "to", "com.tn", "com.tr", "tt", "com.tw", "co.tz", "com.ua", "co.ug", "co.uk",
                        "us", "com.uy", "co.uz", "com.vc", "co.ve", "vg", "co.vi", "com.vn", "vu", "ws", "co.za", "co.zm", "co.zw"]
    ########################################################################################################################################
    ## RAND A GOOGLE DOMAIN ################################################################################################################
    googleDomainName = random.choice(googleDomainName)

    ########################################################################################################################################
    ## IDS USE FOR ENGINE###################################################################################################################
    Ids = (
        "5D4B3C17298B25CC309D9A0951C6BA04", "761446B6C1810068798CA09C88BE0776", "76DE276369845330D17C7CD111A536DD",
        "A0A6BD56DD1A054B1FF32E7FE3A44D27", "F856B0C416AEBE6E6C7610C3B89B5245",
        "88ADADC7E5DB1A344000A6F8C2B0BFA9", "6B815A7FDAF8A283440CD6AEB586CED3", "B6B0770CB0F48619CA0EDE35E451F9E5",
        "D6EA6D2A00270CA431DD36486EE53F35", "7E84432C6967B7DC0AA29A493A1B8FD0"
    )
    Ids = random.choice(Ids)

    ########################################################################################################################################
    ## MSID USE FOR ENGINGE YANDEX##########################################################################################################
    MsIds = (
        "1462902128.39925.22889.22408", "1462902552.15536.22876.27365", "1462902586.95962.22874.20936",
        "1462902627.17116.22876.27348", "1462902668.37045.20953.58001",
        "1462902238.39125.22589.29408", "1462902129.37521.22479.24410", "1462902113.35935.22853.22412",
        "1462902138.59225.22845.22478", "1462902145.39925.22812.22432",
    )
    MsIds = random.choice(MsIds)

    ########################################################################################################################################
    ## FIND WORDPRESS WEB-SITE##############################################################################################################
    wordpressTag = ["<a href=\"https:\/\/wordpress.org\/\">Proudly powered by WordPress", "<meta name=\"generator\" content=\"WordPress", "\/wp-content\/(.*).js"]

    ########################################################################################################################################
    ## FIND JOOMLA WEB-SITE ################################################################################################################
    joomlaTag = ("<meta name=\"generator\" content=\"Joomla")

    ########################################################################################################################################
    ## ENGINE ##############################################################################################################################
    motors = ["http://www.sogou.com/web?query={0}&page={1}&ie=utf8",
              "http://www.yandex.com/search/?msid={0}&text={1}&lr=25402&p={2}",
              "http://www.google.{0}/search?q={1}&start={2}",
              "http://www.bing.com/search?q={0}&first={1}&cc={2}",
              "http://www.ask.com/web?q={0}&page={1}&qid={2}"
              ]

    ########################################################################################################################################
    ## ADMIN PAGE :#########################################################################################################################
    adminPage = ["/admin/", "/admin/login.php", "/myadmin/", "/acceso/", "/administrator/", "/admin1/", "/admin2/", "/wp-admin/login.php",
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
                 "/admin.html", "/admin/cp.html", "cp.html", "/adminpanel.php", "/moderator.html", "/administrator/index.html", "/administrator/login.html",
                 "/user.html", "/administrator/account.html", "/administrator.html", "/login.html", "/modelsearch/login.html", "/moderator/login.html",
                 "/adminarea/login.html", "/panel-administracion/index.html", "/panel-administracion/admin.html", "/modelsearch/index.html", "/modelsearch/admin.html",
                 "/admincontrol/login.html", "/adm/index.html", "adm.html", "/moderator/admin.html", "/user.php", "account.html", "/controlpanel.html",
                 "/admincontrol.html", "/panel-administracion/login.php", "/wp-login.php", "/adminLogin.php", "/admin/adminLogin.php", "/home.php",
                 "/admin.php", "/adminarea/index.php", "/adminarea/admin.php", "/adminarea/login.php", "/panel-administracion/index.php",
                 "/panel-administracion/admin.php", "/modelsearch/index.php", "/modelsearch/admin.php", "/admincontrol/login.php", "/adm/admloginuser.php",
                 "/admloginuser.php", "/admin2.php", "/admin2/login.php", "/admin2/index.php", "/adm/index.php", "/adm.php",
                 "/affiliate.php", "/adm_auth.php", "/memberadmin.php", "/administratorlogin.php"]

    def __init__ (self, userAgent):
        screen.__init__(self, platformUser=sys.platform, argumentProgram=argumentuser)
        screen.checkArgument(self)
        self.Forbieden = ['facebook.', 'twitter.', 'google.', 'github.', 'linkedin.', 'microsoft.', 'youtube.', 'bing.',
                          'yahoo.', 'sogou.', 'ask.', 'yandex.', 'msn.', 'w3school.', 'windows.', 'adobe.com', 'outlook.',
                          'gmail.', 'doc.google.', 'maps.google', 'window.', 'JQuery.min', 'hotmail.', 'yandex.','sogou', 'bing',
                          'php.net', 'mysql.', 'microsofttranslator.','amazon.', 'www.asp.net']

        self.userAgent = userAgent
        self.motorPrepared, self.findAdminFound , self.wp , self.jm= "", "", 1, 1
        self.urlGetedByEngin = []
        self.getResultAll= []
        self.npage = 0
        pass

    ########################################################################################################################################
    ## PREPARE ENGINE +++++> SELF.DORK######################################################################################################
    def setEngine(self):

    	# encrypt dork 
        queryEncode = urllib.parse.quote(self.Dork)
        
        # set motor if type scan "search whit dork"
        if self.motor == 1:
        	## sougo
            self.engin = connection.motors[0]
            self.engin = self.engin.format(queryEncode, "{0}")
            print(self.Color[5], "[+] Engine :", self.Color[-2], " Sogou")

        elif self.motor == 2:
        	## Yandex
            self.engin = connection.motors[1]
            self.engin = self.engin.format(connection.MsIds, queryEncode, "{0}")
            print(self.Color[5], "[+] Engine :", self.Color[-2], " Yandex")
        
        elif self.motor == 3:
        	## google
            self.engin = connection.motors[2]
            self.engin = self.engin.format(connection.googleDomainName, queryEncode, "{0}")
            print(self.Color[5], "[+] Engine :", self.Color[-2], " Google")
        
        elif self.motor == 4:
        	## Bing 
            self.engin = connection.motors[3]
            self.engin = self.engin.format(queryEncode, "{0}", connection.browserLang)
            print(self.Color[5], "[+] Engine :", self.Color[-2], " Bing")
        
        elif self.motor == 5:
        	## Ask
            self.engin = connection.motors[4]
            self.engin = self.engin.format(queryEncode, "{0}", connection.Ids)
            print(self.Color[5], "[+] Engine :", self.Color[-2], " Ask")
        
        else:
        	## Default google 
            self.engin = connection.motors[2]
            self.engin = self.engin.format(connection.googleDomainName, queryEncode, "{0}")
            print(self.Color[5], "[+] Engine :", self.Color[-2], " Google")
    pass
    def searchDork(self, engine):
        try : 

            urlToChange = engine
                
            ## PREPAIR ENGINE
            engine = engine.format(self.npage)
            request = urllib.request.Request(engine)
                        
            ## SET URSER-AGENT 
            request.add_header("User-Agent", connection.userAgent)
                    
            ## GET COGE HTML OF PAGE 
            response = urllib.request.urlopen(request).read()
            connection.getResult(self,response, engine)
        except Exception : 
            print("[+] Error in connection to the engine")
            print("\033[0;0m")
            sys.exit()
			
    ########################################################################################################################################
    ## SEARCH DORK +++> SELF.DORK###########################################################################################################
    def getResult(self, response, engine):
        ## IF USER CHOICE BING OR GOOGLE ENGINES
        if "www.googel." or "www.bing" in engine :
            self.npage = self.npage +10
            ## USE REGEX TO GET RESULT URL
            if "www.bing"in engine :
                ## REGEX FOR GET RESULT FROM BING ENGINE
                self.getResult = re.findall(r'<h2><a href="(.*?)" h="',str(response))
            if "www.google."in engine:
                ## REGEX FOR GET RESULT FROM GOOGLE ENGINE
                self.getResult = re.findall(r'<h3 class="r"><a href="/url.q=(.*?)&', str(response))
                
                ## IF USER CHOICE AN AUTER ENGINE
        if "www.yandex." or  "www.ask." or "www.sogou.com" in engine :
            self.npage = self.npage + 1
            if "www.yandex." in engine :
                ## REGEX FOR GET RESULT FROM YANDEX ENGINE
                self.getResult = re.findall(r'target="_blank" href="(.*?)"', str(response))
                        
            if "www.ask." in engine :
                ## REGEX FOR GET RESULT FROM ASK ENGINE
                self.getResult = re.findall(r'class="web-result-title-link" href="(.*?)"',str(response))
                        
            if "www.sogou.com" in engine :
                ## REGEX FOR GET RESULT FROM SOGOU ENGINE
                self.getResult = re.findall(r'<a name="dttl" target="_blank" href="(.*?)"',str(response))

            ## CHECK IF URL IN LIST OF FORBIDEN SITE
            for url in self.getResult :
                self.getResultAll.append(url)
                for Forbiden in self.Forbieden :
                    if Forbiden in url :
                        check= 0
                        break
                    else :
                        check= 1
                if check == 1 :
                    if url not in self.urlGetedByEngin :
                        decodUrl = urllib.parse.unquote(url)
                        self.urlGetedByEngin.append(decodUrl)
        pass

    ########################################################################################################################################
    ## CONNETION TO THE TARGET ++++> SELF.URL ##############################################################################################
    def connectionTarget(self, Url):

        self.Urlparse = urllib.parse.urlparse(Url)
        print(self.Color[12], ":" * 75)        
        print(self.Color[5], "[+] ", self.dialogTxt[1], " : ", self.Color[-2], Url)
        try:
            
            self.opener = urllib.request.Request(Url)
            ## SET USER AGENT
            
            self.opener.add_header("User-Agent", self.userAgent)
            
            getResult = urllib.request.urlopen(self.opener)
            
            html = getResult.read()
            
            if self.noInfo == False :
                ## GET TYPE OF SERVER
                self.header = getResult.getheader("Server")
            
                self.ipServer = socket.gethostbyname(self.Urlparse[1])
            
                print(self.Color[5], "[+] ", self.dialogTxt[7], " : ", self.Color[-2], self.header)
                print(self.Color[5], "[+] ", self.dialogTxt[6], " : ", self.Color[-2], getResult.status)
                print(self.Color[5], "[+] ", self.dialogTxt[8], ": ", self.Color[-2], self.ipServer)

            if self.wordPress :
                if Url :
                    for tag in connection.wordpressTag :
                        if tag in str(html):
                            print(self.Color[5], "[+]  WordPress :",self.Color[3]," Yes")
                            self.wp  = 0
                            break
                    if self.wp != 0 :
                        print(self.Color[5],"[+]  WordPress : ",self.Color[-2]," No")

            if self.joomla :
                if Url :
                    if connect.joomlaTag in str(html) :
                        print(self.Color[5], "[+]  Joomla :",self.Color[3]," Yes")
                        self.jm = 0

                    if self.jm != 0 :
                        print(self.Color[5], "[+]  Joomla : ", self.Color[-2], " No")
        except ValueError:
            print("\n",self.Color[2],"[!] Error : check  your url")
            print("\n\t", self.Color[5],
                  "[+]  Some advices :",self.Color[-2]," \n\t\t- Add http or https to your url\n\t\t- Set your url into double cama \n\t\t- Don't set an Ip")
            print("\033[0;0m")
            sys.exit()
        except urllib.error.URLError as e :
            print(self.Color[5],"[+] Url : ",self.Color[-2],Url)
            print("\n", self.Color[2]," [!] Error : ",e)
        pass

    ########################################################################################################################################################
    ##   SCAN PORTS ########################################################################################################################################
    def portsScan(self, url):
        
        print("-"*70)
        urlParse = urllib.parse.urlparse(url)
        ports = [20,21,22,23,24,25,35,37,53,80,88,130,135,161,162,443,445,530,546,547,561,1433,1434,1701,1723,2082,2087,2121,2222,3306,3389,8080]
        
        SocketTcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCKET TCP
        SocketUdp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCKET UDP

        if self.tcpPorts :
            print(self.Color[5],"\n====> Scan port tcp (open) :", end=" ")
            self.tcpport = []
            for port in range(len(ports)):
                resPort = SocketTcp.connect_ex((urlParse[1], ports[port]))
                if resPort == 0 :
                    print(self.Color[-2],ports[port], end=" || ")
                    self.tcpport.append(ports[port])

            SocketTcp.close()
        if self.udpPorts :

            print(self.Color[5],"\n====> Scan port udp (open) :", end=" ")
            self.udpport = []
            for port in range(len(ports)):
                resPort = SocketUdp.connect_ex((urlParse[1], ports[port]))
                if resPort == 0 :
                    print(self.Color[-2],ports[port], end=" || ")
                    self.udpport.append(ports[port])
        pass
    ########################################################################################################################################################
    ## FIND ADMIN PAGE +++++> SELF.DORK AND SELF.URL #######################################################################################################
    def pageAdmin(self, Url):
        Lurl = self.Urlparse
        urllocal = Lurl.netloc
        for paths in connection.adminPage:
            fullUrl = urllocal + paths
            connectionPage = http.client.HTTPConnection(urllocal)
            connectionPage.request("GET",paths)
            response = connectionPage.getresponse().status
            connectionPage.close()
            if response == 200 :
                print(self.Color[5],"[+] Page Admin Found ==> ",self.Color[4],fullUrl)
                self.findAdminFound = fullUrl
                break
            else:
                print(self.Color[5],"[+] Page Admin Not Found For ==>",self.Color[4],fullUrl)
                self.findAdminFound = "Admin page not found ."
        pass

    def saveResults (self, scanType, Url, urlNumb) :
        fileSave = open("save result.txt", "a")
            
        if urlNumb == 1 :
            textToSave = "\n\n:::::::::::::::::::::::::: SCAN BY ==> {0} - {1} ::::::::::::::::::::::::::::::".format(os.getlogin(),Time())
            textToSave += "\n  [::] Type Scan : {0}".format(scanType)
        else :
            textToSave = "\n"
        textToSave += "\n  [::] Url : {0}".format(Url)
            
        if connect.noInfo == False :

            textToSave += "\n  [::] Server : {0}".format(connect.header)
            textToSave += "\n  [::] Server-Ip : {0}".format(connect.ipServer)

        if connect.tcpPorts :
            textToSave += "\n  [::] Port Tcp opened : {0}".format(connect.tcpport)

        if connect.udpPorts :
            textToSave += "\n  [::] Port Udp opened : {0}".format(connect.udpport)

        if connect.findAdminFound :
                textToSave += "\n  [::] page Admin : {0}".format(connect.findAdminFound)
        if connect.wordPress :
            if connect.wp == 0 :
                textToSave += "\n  [::] WordPress : Yes"
            else:
                textToSave += "\n  [::] WordPress : No"
        if connect.joomla :
            if connect.jm == 0:
                textToSave += "\n  [::] Joomla : Yes"
            else:
                textToSave += "\n  [::] Joomla : No"

        if connect.sqlFind :
            if vulnerabil.sqlErrrorFound == 0 :
                textToSave += "\n  [::] Sql Injection : Error Found In This Url"
            else :
                textToSave += "\n  [::] Sql Injection : Error Not Found In This Url"
        fileSave.writelines(textToSave)
        fileSave.close()
        pass

###########################################################################################################################################################
####     VULNERABILITY  ###################################################################################################################################
class vulnerability(connection) :

    sqlErrors = ["You have an error in your", "MySQL server", "MySql Error", "syntax error", "syntax error,", "mysql error", "MySQL result ", "MySQL Error"]

    def __init__(self, url):
        connection.__init__(self, connection.userAgent)
        self.urlTscan = url
        self.parsUrlTScan = urllib.parse.urlparse(url)
        self.sqlErrrorFound = 1
    pass

    ##########################################################################################################################################
    ## METHOD FIND SQL ERRORS ################################################################################################################
    def sqlInjiction (self):
        try :
            if self.parsUrlTScan[4] :
                self.makeUrlSql = self.urlTscan+"%27"
                openUrl = urllib.request.urlopen(self.makeUrlSql).read()
                for msgError in vulnerability.sqlErrors :
                    if msgError in str(openUrl):
                        print(self.Color[5],"[+]  Sql Errors :",self.Color[3]," Error Found :)")
                        self.sqlErrrorFound = 0
                        break
                if self.sqlErrrorFound != 0 :
                    print(self.Color[5],"[!]  Sql Errors :",self.Color[2]," Error Not Found !")
                pass
            else :
                print(self.Color[5],"[!]  Sql Ijection :",self.Color[2]," Noo ! --no query found in the url-- ")
        except Exception as e :
            print(self.Color[2],"[+] Error : ",e)
            pass
        pass

## ENCRYPT BASE64
def base64Encrypt(textEncrypt):
    strEncrypted = base64.encodebytes(textEncrypt.encode('ascii'))
    time.sleep(3)
    print(Screen.Color[5],"\t\t=====>",Screen.Color[-2],strEncrypted)
    pass

## DECRYPT BASE64
def base64Decrypt(textDecrypt):
    try:
        strEncrypted = base64.decodebytes(textDecrypt.encode('ascii'))
        time.sleep(3)
        print(Screen.Color[5],"\t\t=====>",Screen.Color[-2],strEncrypted)
    except  :
        time.sleep(3)
        print(Screen.Color[2],"[!] Error in decrypt your string")
    pass

## ENCRYPT MD5
def md5Encrypt(textEncrypt):
    encryptedString = hashlib.md5(textEncrypt.encode("utf")).hexdigest()
    time.sleep(3)
    print(Screen.Color[5],"\t\t=====>",Screen.Color[-2], encryptedString)
    pass

## GET TIME
def Time():
    localTime = "{0}-{1}-{2} {3}:{4}:{5}".format(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4],time.localtime()[5])
    return localTime

## CHECK PYTHON VERSION
def checkVersion():
    getVersion = re.findall(r"<!-- Version (.*?) -->",str(urllib.request.urlopen("https://raw.githubusercontent.com/Suicedal-Virus/Scanner-web/master/README.md").read()))[0]
    if float(getVersion) > 1.2 :
    	print(Screen.Color[2],"[!] New version available Download it .")
		
    else :
    	print(Screen.Color[3],"[+] Aucun new version available .")
		
    

if __name__ == "__main__" :

    try :
        # get argument in the path .
        argumentuser = sys.argv[1:]
        # call class screen
        Screen = screen(sys.platform, argumentuser)
        # show logo
        Screen.Logo()
        # checking argument
        Screen.checkArgument()
        # call method show
        Screen.Show()
        # call class connection and add user agent 
        connect = connection(connection.userAgent)

        ## CHECK UPDATE 
        if Screen.update :
            print(Screen.Color[12],"::::::::::::::::::::::::::::::: ",Screen.scanTitle[-1]," ::::::::::::::::::::::::::::::: ") 
            checkVersion()
            sys.exit()
        ## IF USER WANT DECRYPT BASE64 TO STRING
        if Screen.base64Decry :
            print("\t\t", Screen.Color[12]," "*10,Time())
            print(Screen.Color[12],":::::::::::::::::::::::::::::::  ", Screen.scanTitle[3], " ::::::::::::::::::::::::::::::: ")
            print(Screen.Color[5],"[+] String Decrypted : ",Screen.Color[-2],Screen.base64Decry)
            base64Decrypt(Screen.base64Decry)

        ## IF USER WANT ENCRYPT STRING TO BASE64
        if Screen.base64Encry :
            print("\t\t", Screen.Color[12]," "*10,Time())
            print(Screen.Color[12],":::::::::::::::::::::::::::::::  ", Screen.scanTitle[2], " ::::::::::::::::::::::::::::::: ")
            print(Screen.Color[5],"[+] String Encrypted : ",Screen.Color[-2],Screen.base64Encry)
            base64Encrypt(Screen.base64Encry)

        ## IF USER WANT ENCRYPT STRING TO MD5
        if Screen.md5Encrypt :
            print("\t\t", Screen.Color[12], " " * 10, Time())
            print(Screen.Color[12], ":::::::::::::::::::::::::::::::  ", Screen.scanTitle[-2]," ::::::::::::::::::::::::::::::: ")
            print(Screen.Color[5],"[+] String Encrypted : ", Screen.Color[-2],Screen.md5Encrypt)
            md5Encrypt(Screen.md5Encrypt)

        ## IF USER USE DORK PARAMETER
        if connect.Dork:
            print("\t\t", Screen.Color[12], " " * 10, Time())
            print(Screen.Color[12], "::::::::::::::::::::::::::::::: ", Screen.scanTitle[0]," ::::::::::::::::::::::::::::::")
            
            ## PREPARE ENTGINE FOR SEARCHING
            connect.setEngine()
            
            ## SEARCH DORK AND ADD IT TO A LIST
            while connect.count > len(connect.getResultAll):
                connect.searchDork(connect.engin)

            print(Screen.Color[5],"[+]",Screen.Color[-2],int(len(connect.urlGetedByEngin)),"result found !")
            
            ## GET URL FROM THE LIST AND CONNECTING TO THIS URL 
            numb = 0
            for urlFromDork in connect.urlGetedByEngin :
                numb +=1
                print("\n",Screen.Color[5],"[+]",Screen.Color[-2],"Result N : ",numb,"/",len(connect.urlGetedByEngin))
                connect.connectionTarget(urlFromDork)
                
                if connect.sqlFind :
                    vulnerabil = vulnerability(urlFromDork)
                    vulnerabil.sqlInjiction()
                
                if connect.tcpPorts or connect.udpPorts :
                    connect.portsScan(urlFromDork)
                
                if connect.findAdmin :
                    print("\n", Screen.Color[12], "::::::::::::::::::::::::::: ", connect.scanTitle[4]," :::::::::::::::::::::::::::::::::")
                    connect.pageAdmin(connect.Url)
                
                if connect.saveResult :
                    connect.saveResults(Screen.scanTitle[0], urlFromDork, numb)
            
            if connect.saveResult : 
                print("\n",Screen.Color[4],"[::] Good Bye ! !--Hacker--! || your result is saved on save result.txt")
        
        ## IF USER USE URL PARAMETER
        elif connect.Url:
            print("\t\t", Screen.Color[12], " " * 10, Time())
            print(Screen.Color[12], ":::::::::::::::::::::::::::::: ",Screen.scanTitle[1] ," :::::::::::::::::::::::::::::::")
            connect.connectionTarget(connect.Url)

            if connect.sqlFind:
                vulnerabil = vulnerability(connect.Url)
                vulnerabil.sqlInjiction()

            if connect.tcpPorts or connect.udpPorts:
                connect.portsScan(connect.Url)

            if connect.findAdmin:
                print("\n", Screen.Color[12], "::::::::::::::::::::::::::: ", connect.scanTitle[4]," :::::::::::::::::::::::::::::::::")
                connect.pageAdmin(connect.Url)
            if connect.saveResult :
                    connect.saveResults(Screen.scanTitle[1], connect.Url , 1)
                    print("\n",Screen.Color[4],"[::] Good Bye ! !--Hacker--! || your result is saved on save result.txt")
    	
    	
    except KeyboardInterrupt :
        print(Screen.Color[2],"\n\t[!] Good bye bro process stopped by user.")

	print("\033[0;0m")
