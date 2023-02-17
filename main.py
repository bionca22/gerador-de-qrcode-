import qrcode

from functions import color_validator

message = input("que menssagem seu QRcode trará? ")

print('''escolha uma cor para o seu QRcode!
[BRANCO]
[PRETO]
[AZUL]
[ROSA]
[VERMELHO]
[VERDE]''')
color_bars = input(">")
color_bars = color_bars.lower
if color_bars == "":
    print("seu QRcode terá uma cor padrão então!")
    color_bars = "black"
else:
    color_bars = color_validator(color_bars)

print('''escolha uma cor para o background do seu QRcode!
[BRANCO]
[PRETO]
[AZUL]
[ROSA]
[VERMELHO]
[VERDE]''')
background = input(">")
background = background.lower
if background == "":
    print("seu background terá uma cor padrão então!")
    background = "white"
else:
    background = color_validator(background)

img = qrcode.make(data)

img.save()

