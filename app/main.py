import qrcode

from model import color_validator

message = input("que menssagem seu QRcode trará? ")

print('''escolha uma cor para o seu QRcode!
[BRANCO]
[PRETO]
[AZUL]
[ROSA]
[VERMELHO]
[VERDE]''')
color_bars = input(">\n")
if color_bars == "":
    print("seu QRcode terá uma cor padrão então!")
    color_bars = "black"
else:
    color_bars = color_bars.lower
    color_bars = color_validator(color_bars)

print('''escolha uma cor para o background do seu QRcode!
[BRANCO]
[PRETO]
[AZUL]
[ROSA]
[VERMELHO]
[VERDE]''')
background = input("> \n")
if background == "":
    print("seu background terá uma cor padrão então!")
    background = "white"
else:
    background = background.lower
    background = color_validator(background)

qr =qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(message)

qr.make(fit =True)
img = qr.make_image(fill_color = color_bars, back_color = background)
img.save('/user/home/bianca/QRCode')