from distutils.core import setup
import py2exe
import os
import shutil
import glob
import re

#To do custom imports
#https://stackoverflow.com/a/4383597/11490425
import sys
sys.path.insert(1, (os.getcwd() + "\\dist"))
print(sys.path)

import translator
from translator import languages
version = "4.1.0"

#=====================================================================================
#=====================================================================================
#=====================================================================================

def addCleanDataRecursively(dataDir, folderName):
	allCleanData = str(addDataRecursively(dataDir, folderName))
	
	#Purge all double quote (") characters
	allCleanData = allCleanData.replace("\"", "")

	#Replace cuadruple \\\\ artifacts with \\
	allCleanData = allCleanData.replace("\\\\","\\")

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
			nestedFolderName = (f1[(f1.rindex("\\")):])[1:]

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

#Optimize source code and replace version number
def sourceCodeParser(sourceCodePath, replaceVersion, version):
	#Make a copy of the original source code
	shutil.copyfile(sourceCodePath, "dist\\" + sourceCodePath[:-3] + "_optimized" + sourceCodePath[-3:])
	sourceCodePath = "dist\\" + sourceCodePath[:-3] + "_optimized" + sourceCodePath[-3:]

	#Open and read source code file as read only
	#file will be closed automatically by the "with".
	with open(sourceCodePath, "r") as file:
		sourceCode = file.read()
		
		if(replaceVersion):
			#Replace version number
			sourceCode = sourceCode.replace("AUTO-REPLACED-VERSION", version)

		#https://stackoverflow.com/questions/8784396/how-to-delete-the-words-between-two-delimiters#8784436
		print("Optimizing code for redistributable...")
		sourceCode = re.sub("(#OptStart)[^>]+?(#OptEnd)", "",sourceCode)

		#Write changes to the file
		#file will be closed automatically by the "with".
		with open(sourceCodePath, "w") as file:
			file.write(sourceCode)

	return sourceCodePath

#After all of the code gets optimized, "fun.py" has changed name, but not it"s relative location. This function will patch that:
#WARNING: Modifies original file
def replaceInFile(targetFilePath, textToReplace, replaceWith):

	#Open and read source code file as read only
	#file will be closed automatically by the "with".
	with open(targetFilePath, "r") as file:
		targetFileContents = file.read()

		targetFileContents = targetFileContents.replace(textToReplace, replaceWith)

		#Write changes to the file
		#file will be closed automatically by the "with".
		with open(targetFilePath, "w") as file:
			file.write(targetFileContents)

#=====================================================================================
#=====================================================================================
#=====================================================================================

#English or Spanish?
targetLanguage = (input("Wich language do you want to compile this for? [ENG/esp]: ")).upper()
if targetLanguage == "":
	targetLanguage = "ENG"
elif targetLanguage != "ESP" and targetLanguage != "ENG":
	print("Invalid option selected. Defaulting to \"ENG\"")
	targetLanguage = "ENG"

#Optimize source code
mainSourceCodePath = sourceCodeParser("TerrariaRainbowChat.py", True, version)
#Optimize functions code
funCodePath = sourceCodeParser("fun.py", False, "")

#Translate source code
mainSourceCodePath = translator.translateSourceCode(mainSourceCodePath, targetLanguage, False)
#Translate functions source code
funCodePath = translator.translateSourceCode(funCodePath, targetLanguage, False)


#Replaces in original files
#funCodePath is relative to the base of the project
#"[5:]" removes the "dist\"
#"[:-3]" removes the ".py"
replaceInFile(mainSourceCodePath, "fun.", funCodePath[5:][:-3] + ".")

#Remove previous compilated files
#https://stackoverflow.com/a/1039747/11490425
os.chdir("dist")
for file in glob.glob("*.exe"):
	os.remove(file)
os.chdir("..")

useAHK = (input("Do you want to build this with AHK included? [Y/n]: ")).upper()
if useAHK == "":
	useAHK = "N"
elif useAHK != "Y" and useAHK != "N":
	print("Invalid option selected. Defaulting to \"N\"")
	useAHK = "N"

if(useAHK == "Y"):
	ahkTemplatesDir = str(input("Enter the location of the templates folder in the AHK library (full path): "))

	ahkTemplates = addCleanDataRecursively(ahkTemplatesDir, "templates")

	print("Good luck.")
	setup(
			console = [mainSourceCodePath],
			options = {"py2exe": {"bundle_files": 1, "compressed": True, "optimize": 2,"dll_excludes": ["libcrypto-1_1.dll", "libssl-1_1.dll"]}},
			zipfile = None,
			data_files = ahkTemplates,
			name ="Terraria Colourfull Chat",
			version = version
		)
else:
	#"includes": ["ssl", "_socket", "_ssl", "socket", "selectors", "select", "base64", "binascii", "_hashlib", "urllib3.util.ssltransport", "requests.packages.urllib3.util.ssltransport"]
	#ImportError: No module named 'requests.packages.urllib3'; requests.packages is not a package 🤔
	#Probably the cause of the inconsistent builds
	setup(
			console = [mainSourceCodePath],
			options = {"py2exe": {"bundle_files": 1, "compressed": True, "optimize": 2, "excludes": ["AHK","screeninfo", "lolpython", "ahk", "get_monitors", "lol_py", "fun"], "dll_excludes": ["libcrypto-1_1.dll"], "includes": [funCodePath[5:][:-3]]}},
			zipfile = None,
			name = "Terraria Colourfull Chat",
			version = version
		)

#Give the compiled file a meaningfull name
os.rename(mainSourceCodePath[:-3] + ".exe", mainSourceCodePath[:-3] + "_" + version + ".exe")