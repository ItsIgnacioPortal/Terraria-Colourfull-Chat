import shutil
import json
import re
import os
import glob

languages = {
	"ENG": "ENGLISH",
	"ESP" : "ESPAÑOL"
}

#targetLanguage: String
#   possible values: "NO", "ENG", "ESP"
#sourceWasCopied: Bool
#languages: List containing short and long form of language values
#   example:
#   	languages = {
#		"ENG": "ENGLISH",
#		"ESP" : "ESPAÑOL"
#	}

def translateSourceCode(targetLanguage, sourceWasCopied):
	if(not sourceWasCopied):
		#Make a copy of the original source code
		shutil.copyfile('TerrariaRainbowChat.py', 'TEMP_TerrariaRainbowChat.py')

	#Load and parse the contents of the lang.json
	#NOTE: Due to parsing, the line jumps (\n) MUST be scaped, otherwise they'll be interpreted while replacing the strings below.
	lang = json.load(open('lang.json', 'r'))

	if(targetLanguage != "NO"):
		#English or Spanish?
		targetLanguage = (input("Wich language do you want to compile this for? (ENG/ESP): ")).upper()
		if targetLanguage != "ESP" and targetLanguage != "ENG":
			print("Invalid language entered. Assuming English...")
			targetLanguage = "ENG"

	print("Replacing LangStrings in source code...\n")
	#https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
	#Open and read source code file as read only
	with open('dist/TEMP_TerrariaRainbowChat.py', 'r') as file:
		sourceCode = file.read()
		#file is closed automatically by the 'with'.
		
		#Replace strings in-memory
		for LANGKey in range(0,len(list(lang.keys()))):
			#https://stackoverflow.com/questions/3097866/access-an-arbitrary-element-in-a-dictionary-in-python#comment28476565_17085251
			#https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
			sourceCode = sourceCode.replace( str(list(lang.keys())[LANGKey]), str(lang[str(list(lang.keys())[LANGKey])][targetLanguage]) )

		#Write changes to the file
		with open('dist/TEMP_TerrariaRainbowChat.py', 'w') as file:
			file.write(sourceCode)
			#file is closed automatically by the 'with'.

	#https://stackoverflow.com/a/1039747/11490425
	for file in glob.glob("dist/TerrariaRainbowChat_" + languages[targetLanguage] + "*"):
		os.remove(file)

	#Add language to final source code file name
	targetPath = "dist/TerrariaRainbowChat_" + languages[targetLanguage] + ".py"
	os.rename(r'dist/TEMP_TerrariaRainbowChat.py',targetPath)

	return targetPath