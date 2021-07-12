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

import fun

try:
	from ahk import AHK
	from lolpython import lol_py
	ahk = AHK()
	redistributable = False
except:
	print("LANG_RedistributableCheck")
	redistributable = True


__version__ = "AUTO-REPLACED-VERSION"

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

print("LANG_CheckingForUpdates")

#Check for updates
#Disable plain HTTP warning. We're only getting a version number. Who cares?
#https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
#https://github.com/PyCQA/pylint/issues/4584
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning) # pylint: disable=no-member
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
workingMode = fun.selectWorkingMode()

#OptStart
#If not .exe version, get monitors
if(not redistributable):
	monitorConf = fun.getMonitorConf()
#OptEnd

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
		workingMode = fun.selectWorkingMode()

	elif(userText == "ChangeGradientColor"):
		newColors = fun.modifyGradientColor(activeGradientColor,targetGradientColor)
		activeGradientColor = newColors[0]
		targetGradientColor = newColors[1]

	elif(userText == "EXIT"):
		print("Goodbye!")
	
	#Some servers handle long chat strings poorly, and might kick the player
	#Therefor, it's this script's duty to ensure no strings over-the-limit are generated
	#one character coverted to it's equivalent in hex color for terraria is * 12 it's original size.
	#During testing, the maximum length of the strings terraria servers could take b4 kicking the player is of 992 characters. OR: 82 characters with colors + 7 unformatted characters.
	elif(len(depuratedUserText) <= 82 and bannedCharactersCounter <= 7):
		
		#Actual core of the app
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

		#OptStart
		if(not redistributable):
			#Activate the terraria window
			ahk.mouse_position = (monitorConf[0], monitorConf[1])
			print("Moving mouse to terraria window..." + 
				"\n[INFO]: Moved mouse to (" + str(monitorConf[0]) + " ;" + str(monitorConf[1]) + ")")
		#OptEnd
	#Both checks failed. Send error
	else:
		print("LANG_TextTooLongError")