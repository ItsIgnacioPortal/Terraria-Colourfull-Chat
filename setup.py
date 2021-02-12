from distutils.core import setup
import py2exe
import os
import shutil
import json
import fileinput

nextVersion="3.2.0"

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

#Make a copy of the original source code
shutil.copyfile('TerrariaRainbowChat.py', 'TEMP_TerrariaRainbowChat.py')

#Load and parse the contents of the lang.json
#NOTE: Due to parsing, the line jumps (\n) MUST be scaped, otherwise they'll be interpreted while replacing the strings below.
lang = json.load(open('lang.json', 'r'))

#English or Spanish?
targetLanguage = (input("Wich language do you want to compile this for? (ENG/ESP): ")).upper()
if targetLanguage != "ESP" and targetLanguage != "ENG":
	print("Invalid language entered. Assuming English...")
	targetLanguage = "ENG"

print("\nReplacing LangStrings in source code...\n")
#https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
#Open and read source code file as read only
with open('TEMP_TerrariaRainbowChat.py', 'r') as file:
	sourceCode = file.read()
	#file is closed automatically by the 'with'.
	
	#Replace strings in-memory
	for LANGKey in range(0,len(list(lang.keys()))):
		#https://stackoverflow.com/questions/3097866/access-an-arbitrary-element-in-a-dictionary-in-python#comment28476565_17085251
		#https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
		sourceCode = sourceCode.replace(str(list(lang.keys())[LANGKey]), str(lang[str(list(lang.keys())[LANGKey])][targetLanguage]) )

	#Replace version number
	sourceCode = sourceCode.replace("AUTO-REPLACED-VERSION", nextVersion)

	#Write changes to the file
	with open('TEMP_TerrariaRainbowChat.py', 'w') as file:
		file.write(sourceCode)
		#file is closed automatically by the 'with'.



useAHK = (input("Do you want to build this with AHK included? (y/n): ")).upper()
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
			version = nextVersion
		)
else:
	setup(
			console = ['TEMP_TerrariaRainbowChat.py'],
			options = {'py2exe': {'bundle_files': 1, 'compressed': True, 'optimize': 2, 'excludes': ['AHK','screeninfo', 'lolpython', 'ahk', 'get_monitors', 'lol_py'], "dll_excludes": ["libcrypto-1_1.dll"]}},
			zipfile = None,
			name = 'Terraria Colourfull Chat',
			version = nextVersion
		)

#Cleanup
#os.remove('TEMP_TerrariaRainbowChat.py')
os.remove(r'dist/TerrariaRainbowChat.exe')
os.rename(r'dist/TEMP_TerrariaRainbowChat.exe',r'dist/TerrariaRainbowChat.exe')