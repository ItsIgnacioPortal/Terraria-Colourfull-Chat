# Terraria Colourfull Chat
[![HitCount](http://hits.dwyl.com/pinkdev1/Terraria-Colourfull-Chat.svg)](http://hits.dwyl.com/pinkdev1/Terraria-Colourfull-Chat)    

This is a script made in python 3.7 that aids users in quickly creating and sending colourfull chat messages. Whether that be using the random colours generator, or the gradient generator.

# Installation

Go to [the releases tab](https://github.com/PinkDev1/Terraria-Colourfull-Chat/releases) and download the latest version.
Once downloaded, just open it like any other .exe

OR, if you have **git** and **python3** installed:
```
git clone https://github.com/PinkDev1/Terraria-Colourfull-Chat.git
cd Terraria-Colourfull-Chat
python3 -m pip install -r requirements.txt 
```   

# Usage
Usage is really intuitive (for the most part) if you have the hability to read :)

Open your downloaded **.exe**

OR, if you downloaded from source:
`python3 TerrariaRainbowChat.py`

1. Select the working mode
2. Select the monitor on wich terraria is open (if you have only one monitor, answer anything, it won't break anything.)
3. Select where the selected monitor is (in real life)
4. Start using!

After the text is generated, it will be automatically pasted into your clipboard. 
This script will use [Auto Hot Key](https://www.autohotkey.com/) to automatically move your mouse to the Terraria window after generating text. I made this so the script would be faster to use while playing terraria. 

# Customization
By default the script has `red` as the **Active gradient colour**, and `white` as the **Target gradient colour**. What this means, is that the message's colour will start being red (Active gradient colour), and gradually go to white (Target gradient colour). If you want to change these colours you can type it's value in many many formats; This is thanks to the amazing [colour library](https://pypi.org/project/colour/). All the following are valid ways of typing the **black** colour:

* RGB `rgb=(0, 0, 0)`
* HSL `hsl=(0, 0.0, 0.0)`
* 6-digit hex `#000`
* 3-digit hex `#000000`
* human color `black`

# Example:
The following is a message generated with this script (Active gradient colour = green; Target gradient colour = white):

`[c/008000:m][c/048401:s][c/098802:g] [c/129004:g][c/179405:e][c/1c9706:n][c/229b07:e][c/279f09:r][c/2da20a:a][c/33a60b:t][c/39a90d:e][c/3fac0e:d] [c/4cb312:b][c/52b613:y] [c/5fbc17:a] [c/6cc21b:s][c/73c51d:c][c/7ac81f:r][c/81ca21:i][c/88cd23:p][c/8ed026:t]: [c/a2d430:h][c/a7d336:t][c/acd23c:t][c/b0d241:p][c/b5d147:s]://[c/c4d05c:g][c/c7d061:i][c/cacf66:t][c/cdcf6b:h][c/cfcf70:u][c/cfcd75:b][c/cfcb79:.][c/d0c97e:c][c/d0c883:o][c/d0c787:m]/[c/d1c590:P][c/d1c595:i][c/d2c599:n][c/d2c59e:k][c/d3c5a2:D][c/d4c6a6:e][c/d5c6aa:v][c/d5c7ae:1]/[c/d7cab6:T][c/d8cbba:e][c/d9cdbe:r][c/dbcec1:r][c/dcd0c5:a][c/ddd2c9:r][c/ded4cc:i][c/e0d6d0:a][c/e1d9d3:-][c/e3dbd7:C][c/e4ddda:o][c/e6e0dd:l][c/e8e2e0:o][c/eae5e3:u][c/ece8e6:r][c/edeae9:f][c/efedec:u][c/f1f0ef:l][c/f4f2f2:l][c/f6f5f5:-][c/f8f7f7:C][c/fafafa:h][c/fdfdfd:a][c/ffffff:t]`

To view it, just copy it, open the terraria chat and press `CTRL + V` (paste) :)

# Building
Previously this program used the pyfiglet library to generate the fancy banner, but [pyinstaller hates pyfiglet](https://stackoverflow.com/questions/36970026/pyinstaller-importerror-no-module-named-pyfiglet-fonts) so I decided to remove it and instead put the output into a string and just print that.

To compile this yourself, just do:
`pyinstaller --onefile --add-data "C:\Program Files\Python37\Lib\site-packages\ahk";ahk TerrariaRainbowChat.py`
