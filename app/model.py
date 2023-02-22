color_options = {
    "branco":"white", "preto":"black", "azul":"bluel", "rosa":"pink", "vermelho":"red", "verde":"green"
    }

def color_validator(color):
    try:
        for key in color_options.keys():
            if key == color:
                return color_options.values()
            print(color_options.values())
    except ValueError:
        print("Oops! Cor inválida")
