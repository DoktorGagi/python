import random
print("Welcome to BillRoulette!")
print()

names_string = "John, Mary, James, Emily, Michael, Sarah, David, Jennifer, Christopher, Jessica"
names = names_string.split(", ")
length_of_list = len(names)
payer = random.choice(names)
print("Well today is paying",payer)