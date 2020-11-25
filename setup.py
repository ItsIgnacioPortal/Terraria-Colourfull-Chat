from distutils.core import setup
import py2exe
import os

nextVersion="1.0.4"

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


useAHK = input("Do you want to build this with AHK included? (y/n): ")

if(useAHK == "y"):
	ahkTemplatesDir = str(input("Enter the location of the templates folder in the AHK library (full path): "))

	ahkTemplates = addCleanDataRecursively(ahkTemplatesDir, "templates")

	print("Good luck.")
	setup(
			console=['TerrariaRainbowChat.py'],
			options = {'py2exe': {'bundle_files': 1, 'compressed': True, 'optimize': 2,"dll_excludes": ["libcrypto-1_1.dll", "libssl-1_1.dll"]}},
			zipfile = None,
			data_files = ahkTemplates,
			name='Terraria Colourfull Chat',
			version=nextVersion,
		)
else:
	setup(
			console=['TerrariaRainbowChat.py'],
			options = {'py2exe': {'bundle_files': 1, 'compressed': True, 'optimize': 2, 'excludes': ['AHK','screeninfo'], "dll_excludes": ["libcrypto-1_1.dll"]}},
			zipfile = None,
			name='Terraria Colourfull Chat',
			version=nextVersion,
		)