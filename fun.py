from colour import Color

#OptStart
#Not needed on redistributable version
from screeninfo import get_monitors
#OptEnd

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

#OptStart
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
#OptEnd