color_options = {"branco":"white", "preto":"black", "azul":"bluel", "rosa":"pink", "vermelho":"red", "verde":"green"}

def color_validator(color):
    global color_options
    try:
        for color in color_options:
            if color == color.key:
                return color.value
    except ValueError:
        print("Oops! Cor inválida")
