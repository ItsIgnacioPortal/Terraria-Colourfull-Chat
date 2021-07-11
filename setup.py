from distutils.core import setup
import py2exe
import os
import shutil
import glob
import re
import translator
from translator import languages

version = "4.1.0"

#=====================================================================================
#=====================================================================================
#=====================================================================================

def addCleanDataRecursively(dataDir, folderName):
	allCleanData = str(addDataRecursively(dataDir, folderName))
	
	#Purge all double quote (") characters
	allCleanData = allCleanData.replace('\"', '')

	#Replace cuadruple \\\\ artifacts with \\
	allCleanData = allCleanData.replace('\\\\','\\')

	#Remove "[" at the start, and "]" at the end.
	#These characters were added for some reason
	#allCleanData = (allCleanData[1:])[:-1]

	print("\n\nData has been purged. The new data is: \n\n")
	print(str(allCleanData))

	return allCleanData


#yeah, this is big brain time
def addDataRecursively(dataDir, folderName):

	allData = []

	for file in os.listdir(dataDir):
		f1 = dataDir + "\\" + file
		if(os.path.isdir(f1)):
			#https://stackoverflow.com/questions/33141595/how-can-i-remove-everything-in-a-string-until-a-characters-are-seen-in-python
			#https://www.geeksforgeeks.org/python-find-last-occurrence-of-substring/
			#hmm spaguetty
			nestedFolderName = (f1[(f1.rindex('\\')):])[1:]

			#Get data recursively, replicating the file structure
			recursiveData = str(addDataRecursively(f1, (folderName + "\\" + nestedFolderName)))

			#Remove problematic "[" and "]" characters
			recursiveData = (recursiveData[1:])[:-1]

			allData.append(recursiveData)

		else:
			f2 = (str(folderName), [f1])
			allData.append(f2)
			print("Appended "+ str(f2))

	print("\nReturning: " + str(allData) + "\n\n\n\n")
	return allData

#=====================================================================================
#=====================================================================================
#=====================================================================================

#Make a copy of the original source code
shutil.copyfile('TerrariaRainbowChat.py', 'dist/TEMP_TerrariaRainbowChat.py')

#English or Spanish?
targetLanguage = (input("Wich language do you want to compile this for? (ENG/ESP): ")).upper()
if targetLanguage != "ESP" and targetLanguage != "ENG":
	print("Invalid language entered. Assuming English...")
	targetLanguage = "ENG"

#https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
#Open and read source code file as read only
with open('dist/TEMP_TerrariaRainbowChat.py', 'r') as file:
	sourceCode = file.read()
	#file is closed automatically by the 'with'.
	
	#Replace version number
	sourceCode = sourceCode.replace("AUTO-REPLACED-VERSION", version)

	#https://stackoverflow.com/questions/8784396/how-to-delete-the-words-between-two-delimiters#8784436
	print("Optimizing code for redistributable...")
	sourceCode = re.sub('(#OptStart)[^>]+(#OptEnd)', '',sourceCode)

	#Write changes to the file
	with open('dist/TEMP_TerrariaRainbowChat.py', 'w') as file:
		file.write(sourceCode)
		#file is closed automatically by the 'with'.

#Invoke translator
translator.translateSourceCode(targetLanguage, True)


useAHK = (input("Do you want to build this with AHK included? (Y/N): ")).upper()
if useAHK != "Y" and useAHK != "N":
	print("Invalid option selected. Defaulting to \"no\"")
	useAHK = "N"



if(useAHK == "Y"):
	ahkTemplatesDir = str(input("Enter the location of the templates folder in the AHK library (full path): "))

	ahkTemplates = addCleanDataRecursively(ahkTemplatesDir, "templates")

	print("Good luck.")
	setup(
			console = ['TEMP_TerrariaRainbowChat.py'],
			options = {'py2exe': {'bundle_files': 1, 'compressed': True, 'optimize': 2,"dll_excludes": ["libcrypto-1_1.dll", "libssl-1_1.dll"]}},
			zipfile = None,
			data_files = ahkTemplates,
			name ='Terraria Colourfull Chat',
			version = version
		)
else:
	setup(
			console = ['TEMP_TerrariaRainbowChat.py'],
			options = {'py2exe': {'bundle_files': 1, 'compressed': True, 'optimize': 2, 'excludes': ['AHK','screeninfo', 'lolpython', 'ahk', 'get_monitors', 'lol_py'], "dll_excludes": ["libcrypto-1_1.dll"]}},
			zipfile = None,
			name = 'Terraria Colourfull Chat',
			version = version
		)

#Cleanup
os.remove('TEMP_TerrariaRainbowChat.py')

#https://stackoverflow.com/a/1039747/11490425
for file in glob.glob("dist/TerrariaRainbowChat_" + languages[targetLanguage] + "*"):
	os.remove(file)

#Give the compiled file a meaningfull name
os.rename(r'dist/TEMP_TerrariaRainbowChat.exe',"dist/TerrariaRainbowChat_" + languages[targetLanguage] + "_" + version + ".exe")