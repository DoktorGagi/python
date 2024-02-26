import os
import time
print("Welcome to OddOrEvenNumberDetector!!!")
while True:
    number = int(input("Enter the number u wanna check: \n"))
    if number % 2 == 0:
        print("Numer is even!")
    else:
        print("Number is odd!")
    time.sleep(4)
    os.system ("cls")