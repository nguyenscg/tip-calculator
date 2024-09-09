# This should print as the first message
print("Welcome to the Tip Calculator!")
# first question prompt
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
total_bill = tip / 100 * bill + bill
bill_per_person = total_bill / people
final_total = round(bill_per_person, 2) #This will round to 2 decimal places
print(f"Each person should pay ${final_total}")
