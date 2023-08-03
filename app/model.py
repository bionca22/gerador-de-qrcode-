color_options = {
    "branco": "white",
    "preto": "black",
    "azul": "blue",
    "rosa": "pink",
    "vermelho": "red",
    "verde": "green",
}


def get_user_option(message):
    while True:
        user_input = input(f"{message}\n").lower()
        if user_input in color_options:
            return color_options[user_input]
        else:
            raise ValueError("Opção inválida. Tente novamente.")


""" def color_validator(trigger, color):
    try:
        if color == "":
            print("seu QRcode terá uma cor padrão então!")
            color_bars = default_color_bars
        else:
            color_bars = color_validator(color_bars)
    except ValueError:
"""
