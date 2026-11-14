print("Welcome to the David Goggins Quiz!")

while True:
    level = int(input("\nChoose your level of difficulty (1-3), or 0 to exit: "))
#\n means next line

    if level == 0:
        print("\nThanks for playing!")
        break

    elif level == 1:
        age = int(input("\nHow old is David Goggins? "))

        if age == 51:
            print("\nCorrect!")
        else:
            print("\nIncorrect. David Goggins is 51 years old.")

    elif level == 2:
        height = int(input("\nWhat is David Goggins' height in centimeters? "))

        if height == 185:
            print("\nCorrect!")
        else:
            print("\nIncorrect. David Goggins is 185 cm tall.")

    elif level == 3:
        book = int(input(
            "\nWhat is the title of David Goggins' book?\n"
            "1) Can't Hurt Me\n"
            "2) Can't Stop Me\n"
            "3) Can't Break Me\n"
            "Choose: "
        ))

        if book == 1:
            print("\nCorrect!")
        else:
            print("\nIncorrect. The answer is Can't Hurt Me.")

    else:
        print("\nInvalid difficulty! Choose 1, 2 or 3.")
