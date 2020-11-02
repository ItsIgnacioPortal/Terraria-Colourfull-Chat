# Terraria Colourfull Chat
[![HitCount](http://hits.dwyl.com/pinkdev1/Terraria-Colourfull-Chat.svg)](http://hits.dwyl.com/pinkdev1/Terraria-Colourfull-Chat)    

This is a script made in python 3.7 that aids users in quickly creating and sending colourfull chat messages. Whether that be using the random colours generator, or the gradient generator.

# Installation
`git clone https://github.com/PinkDev1/Terraria-Colourfull-Chat.git`    
`cd Terraria-Colourfull-Chat`    
`python3 -m pip install -r requirements.txt`    

# Usage
Usage is really intuitive (for the most part) if you have the hability to read :)
`python3 TerrariaRainbowChat.py`

At some point the script will ask you if you have opened Terraria on your right monitor. If you only have a single monitor connected, then answer whathever. But if you have two monitors, this script will use [Auto Hot Key](https://www.autohotkey.com/) to automatically move your mouse to the Terraria window, and click it. I made this so the script would be faster to use while playing terraria. 

By default the script has `red` as the "Active gradient colour", and `white` as the "Target gradient colour". What this means, is that the message's colour will start being red (Active gradient colour), and gradually go to white (Target gradient colour). If you want to change these colours you can type it's value in many many formats; This is thanks to the amazing `[colour](https://pypi.org/project/colour/)` library. All the following are valid ways of typing the **black** colour:

* RGB `rgb=(0, 0, 0)`
* HSL `hsl=(0, 0.0, 0.0)`
* 6-digit hex `#000`
* 3-digit hex `#000000`
* human color `black`

# Example:
The following is a message generated with this script:
`[c/008000:t][c/048401:h][c/078702:i][c/0b8a02:s] [c/149104:m][c/189405:e][c/1d9806:s][c/219b07:s][c/269e08:a][c/2ba109:g][c/30a40b:e] [c/3baa0d:w][c/40ad0f:a][c/45b010:s] [c/50b513:a][c/56b814:u][c/5cbb16:t][c/61bd18:o][c/67c019:m][c/6dc21b:a][c/73c51d:t][c/79c71f:i][c/7eca21:c][c/84cc22:a][c/8ace24:l][c/90d026:l][c/96d328:y] [c/a1d430:c][c/a5d335:r][c/aad339:e][c/aed23e:a][c/b2d243:t][c/b6d148:e][c/b9d14c:d] [c/c0d055:w][c/c3d05a:i][c/c6d05e:t][c/c8cf63:h] [c/cdcf6b:T][c/cfcf70:e][c/cfcd74:r][c/cfcb78:r][c/cfca7c:a][c/d0c980:r][c/d0c784:i][c/d0c788:a] [c/d1c590:C][c/d1c594:o][c/d2c598:l][c/d2c59c:o][c/d3c59f:u][c/d3c5a3:r][c/d4c6a7:f][c/d5c6aa:u][c/d5c7ae:l][c/d6c8b1:l] [c/d8cab8:C][c/d9ccbb:h][c/dacdbe:a][c/dbcec2:t] [c/ddd2c8:i][c/ded4cb:n] [c/e0d7d1:j][c/e2d9d4:u][c/e3dbd7:s][c/e4ddda:t] [c/e7e2df:a] [c/ebe6e5:f][c/ece8e7:e][c/eeebea:w] [c/f1efef:s][c/f3f2f1:e][c/f5f4f4:c][c/f7f6f6:o][c/f9f8f8:n][c/fbfbfb:d][c/fdfdfd:s][c/ffffff:!]`

To view it, just copy it, open the terraria chat and press `CTRL + V` (paste) :)
