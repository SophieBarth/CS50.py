#get input from the user
h = int(input("What height would you like the tree to be?\n"))
#check if input is invalid, if so, ask for new input and repeat until input is valid
while(h<0 or h > 24):
    print("That is an invalid input, the height must be between 1 and 24.\n")
    h = int(input("What height would you like the pyramid to be?\n"))
#print the # according to the user input
for i in range(1, h + 1):
    print((h-i) *" " + i * "#" + ' ' + i * "#" + (h - i) * " ", end="")
    print()
