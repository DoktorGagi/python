print("Welcome to the TipCalculator!!!")
total_bill = float(input("What was the total bill?\n"))
percentage = int(input("What percentage would u like to give:10,12 or 15%\n"))
split = int(input("And how many people will split the bill?\n"))
amount_per_person = (total_bill * (1 + percentage / 100)) / split
print("Every person should pay:",round(amount_per_person, 2),"euros")