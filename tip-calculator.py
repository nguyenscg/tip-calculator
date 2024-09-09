# This should print as the first message
print("Welcome to the Tip Calculator!")
# first question prompt
bill = float(input("What was the total bill? $"))
tip = input("How much tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
finalTotal = (bill * tip / people)
print("Each person should pay: " + str(finalTotal))
