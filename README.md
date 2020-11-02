# Terraria Colourfull Chat
This is a script made in python 3.7 that aids users in quickly creating and sending colourfull chat messages. Whether that be using the random colours generator, or the gradient generator.

# Installation
`git clone https://github.com/PinkDev1/Terraria-Colourfull-Chat.git`    
`cd Terraria-Colourfull-Chat`    
`python3 -m pip install -r requirements.txt`    

# Usage
Usage is really intuitive (for the most part) if you have the hability to read :)
`python3 TerrariaRainbowChat.py`

At some point the script will ask you if you have opened Terraria on your right monitor. If you only have a single monitor connected, then answer whathever. But if you have two monitors, this script will use [Auto Hot Key](https://www.autohotkey.com/) to automatically move your mouse to the Terraria window, and click it. I made this so the script would be faster to use while playing terraria. 

When you want to change the colour of the gradients, you can type the colour in many many formats thanks to the amazing `[colour](https://pypi.org/project/colour/)` library. All of the following are valid ways of typing the black colour:

* RGB `rgb=(0, 0, 0)`
* HSL `hsl=(0, 0.0, 0.0)`
* 6-digit hex `#000`
* 3-digit hex `#000000`
* human color `black`