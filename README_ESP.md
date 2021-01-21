# Terraria Colourfull Chat
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FPinkDev1%2FTerraria-Colourfull-Chat&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)  

Esto es un script echo en python 3.7 que ayuda a sus usuarios en la creacion de coloridos mensajes de chat en Terraria!. Actualmente hay dos modos: Arcoiris, y gradiente.

![banner](/img/banner.jpg)

# Instalación

Dirigete a [pagina de versiones](https://github.com/PinkDev1/Terraria-Colourfull-Chat/releases) y descarga la ultima version.
Una vez descargado, puedes abrirlo como cualquier otro _.exe_

O, si tienes **git** y **python3** instalado:
```
git clone https://github.com/PinkDev1/Terraria-Colourfull-Chat.git
cd Terraria-Colourfull-Chat
python3 -m pip install -r requirements.txt 
```
NOTA: La version de codigo fuente requiere tener AutoHotKey instalado.

# Como usar?
El uso es mayormente intuitivo si tiene la habilidad de leer :)

Abri el **.exe** que descargaste

O, si el codigo fuente:
`python3 TerrariaRainbowChat.py`

1. Elige el "modo de operacion"
2. SOURCE - Select the monitor on wich terraria is open (if you have only one monitor, answer anything, it won't break anything.)
3. SOURCE - Select where the selected monitor is (in real life)
4. Empieza a usarlo!
(Los pasos que dicen "SOURCE" solo aplican si estas usando la version con su codigo fuente).

Una vez que se generó el texto, este será copiado al portapapeles automaticamente! 
(Si estas ejecutando desde el codigo fuente) Este script usara [Auto Hot Key](https://www.autohotkey.com/) para mover tu mouse automaticamente a la ventana de Terraria despues de generar el texto. Diseñé esto asi, para que sea mas facil utilizar el script mientras juegas terraria. Si estas ejecutando la version _.exe_, tu mouse _no_ se movera automaticamente. 

# Personalizacion
De forma predeterminada, la secuencia de comandos tiene `rojo` como **Color degradado activo** y ` blanco` como **Color degradado de destino**. Esto significa que el color del mensaje comenzará a ser rojo (color de degradado activo) y gradualmente irá al blanco (color de degradado de destino). Si desea cambiar estos colores, puede escribir su valor en muchos formatos; Esto es gracias a la asombrosa [colour library](https://pypi.org/project/colour/). Todas las siguientes son formas válidas de escribir el color **negro**:

* RGB `rgb=(0, 0, 0)`
* HSL `hsl=(0, 0.0, 0.0)`
* hex 6-digitos `#000`
* hex 3-digitos `#000000`
* color humano `black`

# Example:
El siguiente es un mensaje generado con este script (color de degradado activo = verde; color de degradado de destino = blanco):

`[c/ff0066:M][c/fd0784:e][c/fa0fa0:n][c/f816b9:s][c/f61dd1:a][c/f424e7:j][c/e92af2:e] [c/bf38ee:g][c/ac3eed:e][c/9c45eb:n][c/8d4bea:e][c/8051e8:r][c/7458e7:a][c/6a5ee6:d][c/6466e5:o] [c/6f8ae3:p][c/759ae2:o][c/7ba9e1:r] [c/86c2e0:e][c/8bcce0:l] [c/95dedf:s][c/9adfd9:c][c/9fdfd2:r][c/a4dfcd:i][c/a9dfc9:p][c/aee0c5:t] [c/b7e0c2:T][c/bbe1c1:e][c/bfe1c1:r][c/c5e2c4:r][c/cce3c8:a][c/d2e4cc:r][c/d8e5d0:i][c/dde6d3:a][c/e1e7d7:C][c/e4e8db:o][c/e8eade:l][c/eaebe2:o][c/edede5:u][c/eeeee8:r][c/f0efec:f][c/f2f1ef:u][c/f4f3f2:l][c/f6f5f4:l][c/f8f7f7:C][c/fafafa:h][c/fdfdfd:a][c/ffffff:t]`

Para verlo, simplemente cópielo, abra el chat de terraria y presione `CTRL + V` (pegar) :)

# Compilar

Para compilar esto usted mismo, simplemente haga:
`py -3.7 setup.py py2exe`

El comando anterior usa python 3.7, pero cualquier python> = 3.7 debería funcionar.
Si desea compilarlo con la implementación de AHK, prepárese.