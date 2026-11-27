#1.
found = False
while not found:
    try:
        decnumber = float(input("pls enter a decimal number: "))
        found = True
    except ValueError:
        print("that's not a number, try again")

print("You entered", decnumber)

