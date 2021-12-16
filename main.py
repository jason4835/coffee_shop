#cofee shop ask customer what they want small, medium, large two options dark roast and light roast, add prices with final total saying "Here is you [roast_type], [size] sized coffee would you like milk" ask if customer wants milk then give final toatal

#NOTE: WHEN USING YOU MAY NEED TO MAKE THE CONSOLE LARGER

name = input("What is your name? ")
print("Welcome to the local coffee shop " + name)

total = 0

#asking user if they would like dark or light roast saving to roast_type
roast_type = input("Would you like dark roast(D) or light roast(L)? ")
roast_type = roast_type.upper()
if roast_type == "D" or roast_type == "DARK ROAST" or roast_type == "DARK":
	size = input("What size would you like for your dark roast coffee? \nSmall($2.99)\nMedium($3.65)\nLarge($4.65)\n")
	#asking user what size of dark roast they would like
	size = size.upper()
	if size == "SMALL" or size == "S":
		total += 2.99
	elif size == "MEDIUM" or size == "M":
		total += 3.65
	elif size == "LARGE" or size == "L":
		total += 4.65
	else:
		print("Invalid Input")

elif roast_type == "L" or roast_type == "LIGHT ROAST" or roast_type == "LIGHT":
	size = input("What size would you like for your light roast coffee? \nSmall ($3.10)\nMedium($3.80)\nLarge($4.80)\n")
	#asking for size of light roast
	size = size.upper()
	if size == "SMALL" or size == "S":
		total += 3.10
	elif size == "MEDIUM" or size == "M":
		total += 3.80
	elif size == "LARGE" or size == "L":
		total += 4.80
	else:
		print("Invalid Input")

else:
	print("Invalid Input")

#asking user if they would like milk
answer = input("Would you like milk (Y or N), that would be an extra 20 cents? ")
answer = answer.upper()
if answer == "Y" or answer == "YES":
	total += 0.20
	print("Okay sure thing.")
elif answer == "N" or answer == "NO":
	print("Okay no problem.")
else:
	print("Invalid Input")

#rounding total to the hundredths place
total = round(total, 2)

#print statements for receipt
print("Okay here is your receipt...")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("                           Local Coffee Shop")
print("=======================================================================")
print(roast_type + " ROAST" + " " + size)

print("\nTOTAL: $" + str(total))
print("=======================================================================")
print ("Local Coffee Shop Receipt")
print("=======================================================================")
print(" Thank you for your business!")
print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")

