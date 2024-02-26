import random
print("Wecome to the HangMan!!!")
print()
words = ["ardwark","baboon","camel"]
guess_word = random.choice(words)
hidden_guess_word = []


for _ in guess_word:
    hidden_guess_word += "_"
print("  ".join(hidden_guess_word))



attempts = 6
while attempts > 0:
    letter = input("Enter letter to guess?\n").lower()
    
    for i in range(len(guess_word)):
        if guess_word[i] == letter:
            hidden_guess_word[i] = letter
    print("You  still have ",attempts,"attempts left!")
    print("  ".join(hidden_guess_word))


    if letter in guess_word:
        attempts == attempts
        print("Nice! Continue...")
    else:
        print("Sorry,that letter is not in word!")
        attempts -= 1
        print("You have ",attempts,"attempts left!")

    if "_" not in hidden_guess_word:
        print("Congratulation's you won !!!")
        exit()



else:
    print("Game over! You lost!")
    exit()