name = input("Please enter te player's name: ")
score1 = float(input("Please enter the first score: "))
score2 = float(input("Please enter the second score: "))
score3 = float(input("Please enter the third score: "))
avg = (score1 + score2 + score3) / 3
print(f"{name:>20s}, your average score is {avg:5.2f}")