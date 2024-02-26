print("Welcome to FizzBuzz!!!")
print()
for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzzzzz")
    elif num % 3 == 0:
        print("Fizzz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
