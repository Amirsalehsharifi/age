# num_char = len(input("whats your name?"))
# new_num_char = str(num_char)
# print("your name has " + new_num_char + " characters." )
# print(type(num_char))
# 🚨 Age Calculator 👇
age = input("What is your current age?") 👆
# age input type is str
# change the type of age to int
ageinInt=int(age) 
currentAgeMonth=ageinInt*12
currentAgeWeeks=ageinInt*52
currentAgeDays=ageinInt*365
totalAgeMonth =90*12
totalAgeDays=90*365
totalAgeWeeks=90*52
leftDays=totalAgeDays-currentAgeDays
leftMonths=totalAgeMonth-currentAgeMonth
leftWeeks=totalAgeWeeks-currentAgeWeeks
leftDays=str(leftDays)
leftMonths=str(leftMonths)
leftWeeks=str(leftWeeks)
print("You have "+leftDays+" days, "+leftWeeks+" weeks, and "+leftMonths+" months left if you live 90 years.")
