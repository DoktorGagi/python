print("Welcome to the LoveCalculator!!!")

name = input("What is your name: \n")
partner = input("What is your partner name: \n")
combine = name + partner
compare = ["t","r","u","e","l","o","v","e"]
score = 0
points = 0

for letter in name:
    if letter in compare:
        score += 1
for letter in name:
    if letter in compare:
        points += 1
str_points = str(points)
str_score = str(score)
love_points = str_points + str_score
print("Your love score is",love_points,"points!!!")
integer_points = int(love_points)

if integer_points <= 10 or integer_points >= 90:
    print("You two go together like mentos and coke!!!")
elif integer_points >= 40 and integer_points <= 50:
    print("You are alright together")
else:
    print("Your score is",integer_points,"points!")