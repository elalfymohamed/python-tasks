from termcolor import colored


def colorText(text):
    color = input("Please enter a color:")
    try:
        print(colored(text, color))
    except:
        print("color not available \n please try again")


def bgColorText(text):
    bg = input("Please enter a background:")
    color = input("Please enter a color:")
    try:
        print(colored(text, color, bg))
    except:
        print("color not available \n please try again")


if __name__ == "__main__":
    print(''' select number
       1 - background and color text
       2 - color text ''')
    select = input("enter number: ")
    text = input("Please enter a text: ")
    if select == "1":
        bgColorText(text)
    elif select == "2":
        colorText(text)
    else:
        print("please try again")
