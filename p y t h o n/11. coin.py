import random
print("Welcome to TailsOrHeads!!!")
choice = input("Ok then,chosse head or tail?  ('H' or 'T')\n").lower()
result = random.randint(0,1)
print(result)
if choice == "h" and result == 0:
    print("Wow,nice,you win this time!")
else:
    print("U lose,try again!")