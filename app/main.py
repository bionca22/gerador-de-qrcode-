import qrcode

from model import get_user_option
from config import PATH_TO_FOLDER

message = input("que menssagem seu QRcode trará? ")

color_bars = get_user_option(
    """escolha uma cor para o seu QRcode!
    [BRANCO]
    [PRETO]
    [AZUL]
    [ROSA]
    [VERMELHO]
    [VERDE]"""
)

background = get_user_option(
    """escolha uma cor para o background do seu QRcode!
    [BRANCO]
    [PRETO]
    [AZUL]
    [ROSA]
    [VERMELHO]
    [VERDE]"""
)


qrname = input("Com qual nome deseja salvar seu QR code? ")
if not qrname:
    print("Certo, vamos de nome padrão para seu QR code também.")
    qrname = "qrcode"
qrname = qrname.replace(" ", "")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(message)
qr.make(fit=True)
img = qr.make_image(fill_color=color_bars, back_color=background)
img.save(PATH_TO_FOLDER + qrname)
