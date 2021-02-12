#Required for core functionality
import random
import pyperclip
from colour import Color

#Required for checking for updates
import requests
import json
from packaging import version
import os
from urllib3.exceptions import InsecureRequestWarning

try:
	from ahk import AHK
	from screeninfo import get_monitors
	from lolpython import lol_py
	ahk = AHK()
	redistributable = False
except:
	print("LANG_RedistributableCheck")
	redistributable = True


__version__ = "AUTO-REPLACED-VERSION"
#====================================================================================================================================
#====================================================================================================================================
#====================================================================================================================================


#Function let the user select the working mode
#Returns an int that can be either 1 or 2. 1=Rainbow mode; 2=Gradient mode
def selectWorkingMode():
	workingMode = 0
	#Let user pick a working mode
	while(workingMode not in range(1,3)):

		try:
			print("LANG_WorkingModeMenu")
			workingMode = int(input("LANG_WorkingModeQuery"))
			if(workingMode not in range(1,3)):
				print("LANG_InvalidSelection")

		except:
			print("LANG_InvalidSelectionBad")
	
	#When a working mode has been selected succesfully...
	print("LANG_Instructions")
	if(workingMode == 2): print("LANG_GradientInstructions")

	return int(workingMode)


#Function to let the user select the gradient colors to be used.
#Returns an array of length=2 with the colors to be used [activeGradientColor, targetGradientColor]
def modifyGradientColor(activeGradientColor, targetGradientColor):
	newValue = ""
	selectedGradientChange = 0
	oldColors = [activeGradientColor, targetGradientColor]

	#Let user pick wich color they want to change
	while(selectedGradientChange not in range(1,3)):
		print("-------------------------"+
			"LANG_GradientMenu" + 
			"\n-------------------------")
		
		try:
			selectedGradientChange = int(input("LANG_GradientQuery"))
			if(selectedGradientChange not in range(1,3)):
				print("LANG_InvalidSelection")
		except:
			print("LANG_InvalidSelectionBad")

	try:
		newValue = Color(input("LANG_NewGradientQuery"))
	except:
		print("LANG_NewGradientFail")
		return [oldColors[0], oldColors[1]]
	
	#If user wants to change the active gradient color...
	if(selectedGradientChange == 1):
		activeGradientColor = Color(newValue)
	else:
		targetGradientColor = Color(newValue)

	return [activeGradientColor,targetGradientColor]
	

#Core functionality
def keepMovin(workingMode, userText, monitorConf, activeGradientColor, targetGradientColor, bannedCharacters):

	finalText = ""

	#If using gradient working mode...
	if(workingMode == 2):
		#Generate a list of colors
		gradientColours = list(activeGradientColor.range_to(Color(targetGradientColor),len(userText)))

			
		#Sanitize the values for easier processing
		for color in range(0,int(len(gradientColours))):
			#Convert all values to their long hex value
			gradientColours[color] = gradientColours[color].hex_l
			#Remove the '#'
			gradientColours[color] = gradientColours[color][1:]

		for element in range(0,int(len(userText))):
			#Format it according to Terraria's chat format:
			#https://terraria.gamepedia.com/Chat
			if(userText[element] not in bannedCharacters):
				finalText = (finalText + "[c/" + str(gradientColours[element]) + ":" + str(userText[element]) + "]")

			else:
				finalText = (finalText + userText[element])

	#Else, rainbow working mode...
	else:
		for element in range(0,int(len(userText))):
			#generate random color
			#FROM: https://www.codespeedy.com/create-random-hex-color-code-in-python/
			random_number = random.randint(1118481,16777215)
			hex_number = str(hex(random_number))
			hex_number = hex_number[2:]
		
			#Format it according to Terraria's chat format:
			#https://terraria.gamepedia.com/Chat
			if(userText[element] not in bannedCharacters):
				finalText = (finalText + "[c/" + str(hex_number) + ":" +str(userText[element]) + "]")

			else:
				finalText = (finalText + userText[element])




	#Print generated text to the console
	print(finalText + "LANG_GeneratedTextSuccess")

	#Copy generated text to the clipboard
	pyperclip.copy(finalText)


	if(not redistributable):
		#Activate the terraria window
		ahk.mouse_position = (monitorConf[0], monitorConf[1])
		print("Moving mouse to terraria window..." + 
			"\n[INFO]: Moved mouse to (" + str(monitorConf[0]) + " ;" + str(monitorConf[1]) + ")")


#Function to get the user's monitor configuration. "On wich monitor is terraria?"
#Returns an array of length=2 that contains the center coordinates of the selected monitor [width, height]
def getMonitorConf():
	monitors = []
	selectedMonitor = -1
	monitorPos = ""

	for monitor in get_monitors():
		monitors.append(monitor)
	
	print(str(len(monitors)) + " monitors have been detected.\n")

	#Show list of monitors with index
	#for this function, all instances of range() that include "monitors" will have a +1 because the 2nd parameter on range() is exclusive
	for monitorCount in range(0,len(monitors)):
		print(str(monitorCount+1) + " - " + str(monitors[monitorCount]))
	
	#Ask user wich monitor to use
	while(selectedMonitor not in range(1,len(monitors)+1)):
		try:
			selectedMonitor = int(input("On wich monitor have you opened terraria?: "))

			if(selectedMonitor not in range(1,len(monitors)+1)):
				print("LANG_InvalidSelection")

		except:
			print("LANG_InvalidSelectionBad")
		


	#Ask user where (irl) is the selected monitor
	while(monitorPos not in ["left", "center", "right"]):

		print("-----------------------"+
			"\n\tleft" + 
			"\n\tcenter" + 
			"\n\tright" + 
			"\n-----------------------")
		monitorPos = input("Where (in real life) is the selected monitor?: ")

		if(monitorPos not in ["left", "center", "right"]):
			print("Invalid selection!")

	if(monitorPos=="left"):
		#Return array with the center coordinates of the monitor on the left
		return [((monitors[selectedMonitor-1].width / 2) - monitors[selectedMonitor-1].width),(monitors[selectedMonitor-1].height / 2 )]

	elif(monitorPos=="center"):
		#Return array with the center coordinates of the main monitor
		#selectedMonitor-1 bc arrays start at 0, and during listing of the monitors we showed the monitors index with a +1
		return [(monitors[selectedMonitor-1].width / 2 ),(monitors[selectedMonitor-1].height / 2)]

	else:
		#Return array with the center coordinates of the monitor on the right
		return [((monitors[selectedMonitor-1].width / 2) + monitors[selectedMonitor-1].width),(monitors[selectedMonitor-1].height / 2 )]

#====================================================================================================================================
#====================================================================================================================================
#====================================================================================================================================

def main():

	activeGradientColor = Color("#ff0066")
	targetGradientColor = Color("#ffffff")
	userText = ""
	monitorConf = []
	bannedCharacters = [" ", "/", "[", "]", ":"]
	depuratedUserText = ""
	bannedCharactersCounter = 0
	updateCheck = ""

	#Banner
	banner=(r" _____                        _" + 
	"\n" + r"|_   _|__ _ __ _ __ __ _ _ __(_) __ _" + 
	"\n" + r"  | |/ _ \ '__| '__/ _` | '__| |/ _` |" + 
	"\n" + r"  | |  __/ |  | | | (_| | |  | | (_| |" + 
	"\n" + r"  |_|\___|_|  |_|  \__,_|_|  |_|\__,_|" + 
	"\n" + 
	"\n" + r"  ____      _                   __       _ _    ____ _           _" + 
	"\n" + r" / ___|___ | | ___  _   _ _ __ / _|_   _| | |  / ___| |__   __ _| |_" + 
	"\n" + r"| |   / _ \| |/ _ \| | | | '__| |_| | | | | | | |   | '_ \ / _` | __|" + 
	"\n" + r"| |__| (_) | | (_) | |_| | |  |  _| |_| | | | | |___| | | | (_| | |_" + 
	"\n" + r" \____\___/|_|\___/ \__,_|_|  |_|  \__,_|_|_|  \____|_| |_|\__,_|\__|" + 
	"\n")
	if(redistributable):
		print(banner)
	else:
		lol_py(banner)


	#Check for updates
	#Disable plain HTTP warning. We're only getting a version number. Who cares?
	#https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
	requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

	print("LANG_CheckingForUpdates")
	updateCheck = requests.get('http://api.github.com/repos/PinkDev1/Terraria-Colourfull-Chat/releases/latest', verify=False)

	#If something happened, spit an error.
	if (updateCheck.status_code != 200):
		print("LANG_ConnectionError")

	else:
		#Get latest version from the GitHub REST API, parse response as JSON, get the tag_name (version), and remove the "v"
		#https://docs.github.com/en/rest/reference/repos#get-the-latest-release
		versionNumber = ((json.loads(updateCheck.text))["tag_name"])[1:]
		
		#Compare as version numbers
		#https://stackoverflow.com/questions/11887762/how-do-i-compare-version-numbers-in-python
		if(version.parse(versionNumber) > version.parse(__version__)):

			#Update found! Do you want to update?
			if(input("LANG_NewVersionFound").lower() == "LANG_Yes"):
				#Open link in browser
				#adf.ly shortened version of https://github.com/PinkDev1/Terraria-Colourfull-Chat/releases/latest
				#Development takes time and money ¯\_(ツ)_/¯
				os.system('cmd /c "start http://motriael.com/24801569/terrariacolourfullchatupdate"')
		
		else:
			#No update avalible. Currently using the latest version!
			print("LANG_NoUpdatesFound")


	#Gradient or rainbow?
	workingMode = selectWorkingMode()

	#If not .exe version, get monitors
	if(not redistributable):
		monitorConf = getMonitorConf()

	#Loop it until the user wants to exit
	while(userText != "EXIT"):
		userText = input("LANG_InitialInput")
		
		#Restart the contents of depuratedUserText
		depuratedUserText = ""
		#Restart this counter
		bannedCharactersCounter = 0

		#Depurate the user text, for processing later.. 
		#(remove all banned characters)
		for character in range(0,len(userText)):
			if(userText[character] not in bannedCharacters):
				depuratedUserText += str(userText[character])
			
			else:
				bannedCharactersCounter += 1
		

		if(userText == "ChangeWorkingMode"):
			workingMode = selectWorkingMode()

		elif(userText == "ChangeGradientColor"):
			newColors = modifyGradientColor(activeGradientColor,targetGradientColor)
			activeGradientColor = newColors[0]
			targetGradientColor = newColors[1]

		elif(userText == "EXIT"):
			print("Goodbye!")
		
		#Some servers handle long chat strings poorly, and might kick the player
		#Therefor, it's this script's duty to ensure no strings over-the-limit are generated
		#one character coverted to it's equivalent in hex color for terraria is * 12 it's original size.
		#During testing, the maximum length of the strings terraria servers could take b4 kicking the player is of 992 characters. OR: 82 characters with colors + 7 unformatted characters.
		elif(len(depuratedUserText) <= 82):
			keepMovin(workingMode, userText, monitorConf, activeGradientColor, targetGradientColor, bannedCharacters)

		#There's more than 82 valid chars. If there's less than 7 bannedchars... 
		elif(bannedCharactersCounter <= 7):
			keepMovin(workingMode, userText, monitorConf, activeGradientColor, targetGradientColor, bannedCharacters)

		#Both checks failed. Send error
		else:
			print("LANG_TextTooLongError")
main()