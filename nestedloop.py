#project color code

try:
    color_code = int(input("Enter the color code"))
except ValueError:
    print("Please enter the correct format")
    exit()


def cod_predictor():

    if color_code <= 449:
        print("Violet")
    elif color_code < 484:
        print("Blue")
    elif color_code < 499:
        print("cyan")
    elif color_code < 564:
        print("Green")
    elif color_code < 589:
        print("Yellow")
    elif color_code < 624:
        print("Orange")
    else:
        print("Red")


cod_predictor()






