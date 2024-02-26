import time 
import os
while True:
    print("Welcome to LeapYearCalculator!!!")
    year = int(input("Type here the year u wanted to check:\n"))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is leap!!")
            else:
                print(f"{year} is not leap!!")
        else:
            print(f"{year} is leap!!")
    else:
        print(f"{year} is not leap!!")
    time.sleep(5)
    os.system("cls")