import random
print("Welcome to the PasswordGenerator!!!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print()
num_of_letters = int(input("How many letters would u like in your password?\n"))
num_of_symbols = int(input("How many symbols would u like in your password?\n"))
num_of_numbers = int(input("How many numbers would u like in your password?\n"))
storage = []

for letter in range(num_of_letters):
    storage.append(random.choice(letters))
for symbol in range(num_of_symbols):
    storage.append(random.choice(symbols))
for num in range(num_of_numbers):
    storage.append(random.choice(numbers))
print((storage))
random.shuffle(storage)
password = ''.join(storage)
print(password)
