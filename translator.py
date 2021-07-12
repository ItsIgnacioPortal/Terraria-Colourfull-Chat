import shutil
import json
import os
import glob

languages = {
	"ENG": "ENGLISH",
	"ESP" : "ESPAÑOL"
}

#targetLanguage: String or Bool
#   possible values: "ENG", "ESP", False
#sourceWasCopied: Bool
#languages: List containing short and long form of language values
#   example:
#   	languages = {
#		"ENG": "ENGLISH",
#		"ESP" : "ESPAÑOL"
#	}

def translateSourceCode(targetSourceCodePath, targetLanguage, makeCopyOfSourceCode):
	if(makeCopyOfSourceCode):
		#Make a copy of the original source code
		shutil.copyfile(targetSourceCodePath, "dist/TEMP_" + targetSourceCodePath)
		targetSourceCodePath = "dist/TEMP_" + targetSourceCodePath

	#Load and parse the contents of the lang.json
	#NOTE: Due to parsing, the line jumps (\n) MUST be scaped, otherwise they'll be interpreted while replacing the strings below.
	lang = json.load(open('lang.json', 'r'))

	if(targetLanguage == False):
		#English or Spanish?
		targetLanguage = (input("Wich language do you want to compile this for? (ENG/ESP): ")).upper()
		if targetLanguage != "ESP" and targetLanguage != "ENG":
			print("Invalid language entered. Assuming English...")
			targetLanguage = "ENG"

	print("Replacing LangStrings in source code...\n")
	#https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
	#Open and read source code file as read only
	with open(targetSourceCodePath, 'r') as file:
		sourceCode = file.read()
		#file is closed automatically by the 'with'.
		
		#Replace strings in-memory
		for LANGKey in range(0,len(list(lang.keys()))):
			#https://stackoverflow.com/questions/3097866/access-an-arbitrary-element-in-a-dictionary-in-python#comment28476565_17085251
			#https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
			sourceCode = sourceCode.replace( str(list(lang.keys())[LANGKey]), str(lang[str(list(lang.keys())[LANGKey])][targetLanguage]) )

		#Write changes to the file
		with open(targetSourceCodePath, 'w') as file:
			file.write(sourceCode)
			#file is closed automatically by the 'with'.

	finalName = targetSourceCodePath[:-3] + "_" + languages[targetLanguage] + ".py"
	#Remove old copies of translated source code
	try:
		os.remove(finalName)
	except FileNotFoundError:
		print("[translator.py][INFO]: Attempted to remove old copies, but no old copies found.")

	#Add "language" string to final source code file name
	os.rename(targetSourceCodePath, finalName)

	return finalName