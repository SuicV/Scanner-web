from random import choice
from platform import system
from os import get_terminal_size
class screen () :
	def __init__ (self, logos= ""):
		# COLORS 
		if system() == "Linux" :
			self.colors = {"black":"\033[0;30m",
						"green":"\033[0;32m",
                        "yellow":"\033[0;33m",
                        "blue":"\033[0;34m",
                        "purple":"\033[0;35m",
                        "cyan":"\033[0;36m",
                        "white":"\033[0;37m",
                        "red":"\033[0;31m",
                        "bold_black":"\033[1;30m",
                        "bold_red":"\033[1;31m",
                        "bold_green":"\033[1;32m",
                        "bold_cyan": "\033[1;36m",
                        "bold_white":"\033[1;37m",
                        "bold_blue":"\033[1;34m",
                        "bold_yellow":"\033[1;33m",
                        "restart":"\033[0m"}
			
			self.restarColor = "\033[0m"
		else :
			self.colors = {}
		# LOGO
		self.logos = logos
	"""
	Method getColor(self, Color)
		return stirng color
	"""
	def getColor (self , Color):
		return self.colors.get(Color)
	"""
	Method prLogo
		method to print the logo 
		print self.logo if is passed
	"""
	def prLogo(self):
		if type(self.logos) is list :
			logo = choice(self.logos)
			print(logo,self.restarColor)
		else :
			print(self.logos,self.restarColor)
	"""
	@mehtod to print an information
	"""
	def prInfo(self, title,value,tab= 0, rtn = None):
		if rtn is not None :
			print(" "*self.termenalSize().columns,end="\r")
			print(" "*tab,"[+]",title,"",value,self.restarColor,end="\r")
		else : 
			print(" "*tab,"[+]",title,":",value,self.restarColor)

	"""
	@method print a subinformation
	"""
	def prSubInfo(self, title, value,tab= 4):
		print(" "*tab,"==>",title,":",value,self.restarColor)
	
	"""
	@method print a danger
	"""
	def prDanger(self,title,value,tab= 0):
		print(" "*tab,"[!]",title,":",value,self.restarColor)
	
	"""
	@method return the number of colomns in terminal screen
	"""
	def termenalSize(self):
		return get_terminal_size()