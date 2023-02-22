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

qr =qrcode.QRcode(version = 1, box_sixe = 10, border = 5)

qr.add_data(message)

qr.make(fit =True)
img = qr.make_image(fill_color = color_bars, back_color = background)
img.save('C:/users/home/bianca/QRCode')