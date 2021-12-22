total = 0


def welcome():
    name = input("What is your name? ")
    print("Welcome to the local coffee shop " + name)


def roast():
    roast_type = input("Would you like dark roast(D) or light roast(L)? ")
    roast_type = roast_type.upper()
    if roast_type == "D" or roast_type == "DARK ROAST" or roast_type == "DARK":
        size_dark(total)
    elif roast_type == "L" or roast_type == "LIGHT ROAST" or roast_type == "LIGHT":
        size_light(total)
    else:
        print("Invalid Input")


def size_dark(total):
    size = input(
        "What size would you like for your dark roast coffee? \nSmall($2.99)\nMedium($3.65)\nLarge($4.65)\n")
    # asking user what size of dark roast they would like
    size = size.upper()
    if size == "SMALL" or size == "S":
        total += 2.99
        milk(size, roast, total)
    elif size == "MEDIUM" or size == "M":
        total += 3.65
        milk(size, roast, total)
    elif size == "LARGE" or size == "L":
        total += 4.65
        milk(size, roast, total)
    else:
        print("Invalid Input")


def size_light(total):
    size = input(
        "What size would you like for your light roast coffee? \nSmall ($3.10)\nMedium($3.80)\nLarge($4.80)\n")
    # asking for size of light roast
    size = size.upper()
    if size == "SMALL" or size == "S":
        total += 3.10
        milk(size, roast, total)
    elif size == "MEDIUM" or size == "M":
        total += 3.80
        milk(size, roast, total)
    elif size == "LARGE" or size == "L":
        total += 4.80
        milk(size, roast, total)
    else:
        print("Invalid Input")


def milk(size, roast_type, total):
    # asking user if they would like milk
    answer = input(
        "Would you like milk (Y or N), that would be an extra 20 cents? ")
    answer = answer.upper()
    if answer == "Y" or answer == "YES":
        total += 0.20
        print("Okay sure thing.")
        milk = True
        if milk == True:
            milk_yes_no = "MILK"
        elif milk == False:
            milk_yes_no = "NO MILK"
        else:
            print("Error")
        receipt(size, milk_yes_no, total)
    elif answer == "N" or answer == "NO":
        print("Okay no problem.")
        milk = False
        if milk == True:
            milk_yes_no = "MILK"
        elif milk == False:
            milk_yes_no = "NO MILK"
        else:
            print("Error")
        receipt(size, milk_yes_no, total)
    else:
        print("Invalid Input")


def receipt(size, milk_yes_no, total):

    # print statements for receipt
    print("Okay here is your receipt...")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("                           Local Coffee Shop")
    print("=======================================================================")
    print(" ITEM: \n " + str(size) + " COFFEE " + str(milk_yes_no))
    print("\n SUBTOTAL: " + str(total))
    tax = 0.04
    total += tax
    # rounding total to the hundredths place
    total = round(total, 2)
    print("\n TOTAL: $" + str(total))
    print("=======================================================================")
    print(" Local Coffee Shop Receipt")
    print("=======================================================================")
    print(" Thank you for your business!")
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
