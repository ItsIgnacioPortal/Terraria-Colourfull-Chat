import random
import pyperclip
import time
from ahk import AHK
ahk = AHK()
from colour import Color


#====================================================================================================================================
#====================================================================================================================================
#====================================================================================================================================



def selectWorkingMode():
	workingMode = 0
	#Let user pick a working mode
	while(workingMode not in range(1,3)):
		print("-------------------------"+
			"\n1 - Rainbow mode" + 
			"\n2 - Gradient mode" + 
			"\n-------------------------")
		workingMode = int(input("What mode do you want to run this script in?: "))
		if(workingMode not in range(1,3)):
			print("That's not a valid mode selection!")
	
	#When a working mode has been selected succesfully...
	return int(workingMode)


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
	


def keepMovin(workingMode, userText, terrariaRight, activeGradientColor, targetGradientColor):

	finalText = ""
	bannedCharacters = [" ", "/", "[", "]", ":"]

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
	print(finalText)

	#Copy generated text to the clipboard
	pyperclip.copy(finalText)

	#Activate the terraria window
	if(terrariaRight == "yes"):
		ahk.mouse_position = (100, 100)
	else:
		ahk.mouse_position = (-100, 100)
	ahk.click()


#====================================================================================================================================
#====================================================================================================================================
#====================================================================================================================================

def main():

	yesno = ["yes", "no"]
	terrariaRight = ""
	activeGradientColor = Color("#ff0066")
	targetGradientColor = Color("#ffffff")
	userText = ""
	workingMode = selectWorkingMode()

	while(terrariaRight not in yesno):
		terrariaRight = str(input("Is terraria on the right monitor?(yes/no): "))
		if(terrariaRight not in yesno):
			print("Enter a valid answer!")

	print("Enter 'EXIT' to exit." + 
		"\nEnter 'ChangeWorkingMode' to change mode." + 
		"\nEnter 'ChangeGradientColor' to change the color used in gradient mode.")

	#Loop it until the user wants to exit
	while(userText != "EXIT"):
		userText = input("Enter your text: ")

		if(userText == "ChangeWorkingMode"):
			workingMode = selectWorkingMode()

		elif(userText == "ChangeGradientColor"):
			newColors = modifyGradientColor(activeGradientColor,targetGradientColor)
			activeGradientColor = newColors[0]
			targetGradientColor = newColors[1]

		elif(userText == "EXIT"):
			print("Goodbye!")
		
		else:
			keepMovin(workingMode, userText, terrariaRight, activeGradientColor, targetGradientColor)

main()