import random
import pyperclip
import sys
from colour import Color
from lolpython import lol_py

from ahk import AHK
if("ahk.autohotkey" in sys.modules):
	ahk = AHK()
	ahkImported = True
	from screeninfo import get_monitors
else:
	ahkImported = False
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
			print("-------------------------"+
				"\n1 - Rainbow mode" + 
				"\n2 - Gradient mode" + 
				"\n-------------------------")
			workingMode = int(input("What mode do you want to run this script in?: "))
			if(workingMode not in range(1,3)):
				print("That's not a valid mode selection!")

		except:
			print("That's not a valid mode selection!!")
	
	#When a working mode has been selected succesfully...
	return int(workingMode)


#Function to let the user select the gradient colors to be used.
#Returns an array of length=2 with the colors to be used [activeGradientColor, targetGradientColor]
def modifyGradientColor(activeGradientColor, targetGradientColor):
	newValue = ""
	selectedGradientChange = 0

	#Let user pick wich color they want to change
	while(selectedGradientChange not in range(1,3)):
		print("-------------------------"+
			"\n1 - Active gradient color" + 
			"\n2 - Target gradient color" + 
			"\n-------------------------")
		
		try:
			selectedGradientChange = int(input("Wich gradient color do you want to modify?: "))
			if(selectedGradientChange not in range(1,3)):
				print("Invalid selection!")
		except:
			print("Invalid selection!")

	try:
		newValue = Color(input("Enter the NEW color: "))
	except:
		print("Invalid value inputted! Keeping old colour...")
		return
	
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
				finalText = (finalText + "[c/" + str(hex_number) + ":"+str(userText[element]) + "]")

			else:
				finalText = (finalText + userText[element])




	#Print generated text to the console
	print(finalText + "\nGenerated text been copied to the clipboard!")

	#Copy generated text to the clipboard
	pyperclip.copy(finalText)


	if(ahkImported):
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
				print("Invalid monitor selected!")

		except:
			print("Invalid monitor selected!!")
		


	#Ask user where (irl) is the selected monitor
	while(monitorPos not in ["left", "center", "right"]):

		print("-----------------------"+
			"\n\tleft" + 
			"\n\tcenter" + 
			"\n\tright" + 
			"\n-----------------------")
		monitorPos = input("Where (in real life) is the selected monitor?: ")

		if(monitorPos not in ["left", "center", "right"]):
			print("Invalid position selected!")

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
	lol_py(banner)

	#Gradient or rainbow?
	workingMode = selectWorkingMode()

	#If using the redistributable version, skip this, since we won't use the data anyway
	if(ahkImported):
		monitorConf = getMonitorConf()

	print("Enter 'EXIT' to exit." + 
		"\nEnter 'ChangeWorkingMode' to change mode." + 
		"\nEnter 'ChangeGradientColor' to change the color used in gradient mode.")

	#Loop it until the user wants to exit
	while(userText != "EXIT"):
		userText = input("Enter your text: ")
		
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
			print("The string you entered is too long! No conversion will be made." + 
				"\n The string you entered had " + str(len(depuratedUserText)) + " valid characters, and " + str(bannedCharactersCounter) + " banned characters." 
				"\n For info in this limitation, refer to the README.md")
main()