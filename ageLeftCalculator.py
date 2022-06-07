# num_char = len(input("whats your name?"))
# new_num_char = str(num_char)
# print("your name has " + new_num_char + " characters." )
# print(type(num_char))
# 🚨 Age Calculator 👇
age = input("What is your current age?") 
# age input type is str
# change the type of age to int
ageinInt=int(age) 
remain_age_years = 90-ageinInt
leftDays=remain_age_years*365
leftWeeks=remain_age_years*52
leftMonths=remain_age_years*12
message=f"You have {leftDays} days, {leftWeeks} weeks, and {leftMonths} months left."
print(message)
