from optparse import OptionParser
from optparse import OptionGroup
from optparse import OptionValueError
from regex import regex
from os.path import exists

def buildArgvSys():
	Regex = regex()
	parser = OptionParser()
	# GROUPS
	Proxy = OptionGroup(parser,
						"Proxy Options")
	Encryptation = OptionGroup(parser,
							   "Hash's Encrypt And Decrypt")
	External_command = OptionGroup(parser,
									"External Command",
									"Use an external tool with the scan")
	# SET OPTIONS TO GROUPS 
	Proxy.add_option("-p","--proxy",
					 dest="proxy",
					 help="Use proxy with scan",
					 metavar="PROXY")
	External_command.add_option("--command",
								dest="external-command",
								help="call command at evrey host scan",
								metavar="COMMAND",
								type="str")
	External_command.add_option("--HOST",
								help="Constant in command option for replace it with url",
								metavar=None)
	External_command.add_option("--IP",
								help="Constant in command option for replace it with the ip of host ",
								metavar=None)
	Encryptation.add_option("--md5Encr",
							dest="md5Enc",
							help="Encrypte a string to md5 hash",
							metavar="STRING")
	Encryptation.add_option("--base64Encr",
							dest="base64Encr",
							help="Encrypte a string to base64",
							metavar="STRING")
	Encryptation.add_option("--base64Decr",
							dest="base64Decr",
							help="Decrypte a base64 to string",
							metavar="STRING")
	# ADD GROUPS
	parser.add_option_group(Proxy)
	parser.add_option_group(Encryptation)
	parser.add_option_group(External_command)
	
	# GENERAL OPTIONS
	parser.add_option("-u","--url",
					  dest="url",
					  help="Scan a particular URL",
					  type="str",
					  metavar="URL|LIST",
					  callback=listExist,
					  callback_args=tuple([Regex]),
					  action="callback")

	parser.add_option("-d","--dork",
					  dest="dork",
					  help="Look for dork", 
					  metavar="DORK|LIST",
					  type="str",
					  callback=listExist,
					  callback_args=tuple([Regex]),
					  action="callback")

	parser.add_option("--pages",
					  help="Set number of pages to get from the engine",
					  dest="pages",
					  type="int",
					  default=1)

	parser.add_option("-e","--engine",
					  dest="engin",
					  help="Set engine to search for dork",
					  metavar="ENGINE",
					  default="google")

	parser.add_option("--time-out",
					  dest="timeout",
					  help="Set time out of the connecton default time out = 30s",
					  metavar="SECONDS",
					  default=30,
					  type="int",
					  callback=timeout,
					  action="callback")

	parser.add_option("--tcp-ports",
					  dest="tcp-ports",
					  help="Scan tcp ports in the server",
					  default=False,
					  action="store_true")

	parser.add_option("--udp-ports",
					  dest="udp-ports",
					  help="Scan udp ports in the server",
					  default=False,
					  action="store_true")

	parser.add_option("--ports",
					  dest="ports",
					  help="set your ports to scan you can set set a single port or multiple ports separated by ','\
					        or an intervale of ports with using range(min,max) function ",
					  callback=portsChecker,
					  action="callback",
					  type="string",
					  callback_args=tuple([Regex])
					)
	parser.add_option("--portsTCP",
					  dest="portsTCP",
					  help="Scan tcp ports in the server",
					  default=False,
					  action="store_true")

	parser.add_option("--portsUDP",
					dest="portsUDP",
					help="Scan udp ports in the server",
					default=False,
					action="store_true")				  
	parser.add_option("--validation",
					  dest="validation",
					  help="Look for a string in response of site's",
					  metavar="STRING",
					  default=False)

	parser.add_option("--regex",
					  dest="regex",
					  help="Look for a regex in response",
					  metavar="REGEX")

	parser.add_option("--sql-injection",
					  dest="sql",
					  help="scan for sql injection error",
					  default=False,
					  action="store_true")

	parser.add_option("--noInfo",
					  dest="info",
					  help="Disable displaying informations about target" ,
					  action="store_true",
					  default=False)

	parser.add_option("--update",
					  dest="update",
					  help="Check if a new update available",
					  action="store_true",
					  default=False)
	parser.add_option("-s","--save",
					  dest="save",
					  help="save scan results in file",
					  metavar="FILE")

	(options, args) = parser.parse_args()
	return vars(options)

# CALLBACKS FOR HANDLING OPTIONS 
def timeout(option,opt_str,value,parser):
	"""
	param option optparse.Option
	param opt_str str passed option
	param value str the value of option
	param parser OptionParser object
	"""
	if value >= 5 :
		parser.values.timeout = value
	else :
		raise OptionValueError("{} value must be more than 10 seconds".format(opt_str))	
	pass
"""
@func to check if a passed file exist or not and raise an error if doesn't exist
"""
def listExist(option,opt_str,value,parser,Regex):

	if Regex.isPath(value):
		if exists(value):
			if option.dest == "dork" :
				parser.values.dork = {"List":value}
			elif option.dest == "url" :
				parser.values.url = {"List":value}
		else :
			raise OptionValueError("file passed in {} doesn't exist".format(opt_str))
	else :
		if option.dest == "dork":
			parser.values.dork = value
		if option.dest == "url":
			parser.values.url = value
	pass

def portsChecker(option,opt_str,value,parser,Regex):
	result = Regex.getfullMatch(Regex.PortsChecker,value)
	if result.match() != None:
		if "range" not in result.match() :
			result = result.match().split(",")
		else :
			fromPort = result.groups[0][1]
			toPort = result.groups[0][2]
			if fromPort < toPort :
				result = range(fromPort,toPort)
			else :
				result = range(toPort,fromPort)
	else :
		raise OptionValueError("no ports match set a single port or port1,port2,... or range(fromPort,toPort)")
	pass