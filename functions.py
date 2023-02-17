color_options = {"branco":"white", "preto":"black", "azul":"bluel", "rosa":"pink", "vermelho":"red", "verde":"green"}

def color_validator(color):
    global color_options
    try:
        for color.key in color_options:
            if color.ky == color:
                return color.value
    except ValueError:
        print("Oops! Cor inválida")
