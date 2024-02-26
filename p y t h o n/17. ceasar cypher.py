print("Welcome to the CeasarCypher!!!")
print()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Would u like 'decode' or 'encode'?\n")
shift = int(input("Choose the scale of shift's:\n"))
mesagge = input("Enter your text here:\n")
decoded_message = []

if direction == "encode":
    for letter in mesagge:
        if letter in alphabet:
            index = alphabet.index(letter)
            shifted_index = (index + shift) % 26
            print(alphabet[shifted_index],end='')
elif direction == "decode":
    for letter in mesagge:
        if letter in alphabet:
            index = alphabet.index(letter)
            shifted_index = (index - shift) % 26
            print(alphabet[shifted_index],end='')
