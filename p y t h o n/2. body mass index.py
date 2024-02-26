print("Welcome to the BodyMassIndex")
weight = int(input("Type here your weight:\n"))
height = float(input("Type here your height:\n"))
bmi = weight / (height * height)
bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your Body Mass Index is: {bmi}. You are underweight!")
elif bmi < 25:
    print("You have normall weight!")
elif bmi < 30:
    print("You are slightly overweight!")
elif bmi < 35:
    print("You are obese!")
else:
    print("You are clinically obese !!!")
    