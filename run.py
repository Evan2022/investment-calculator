# Write your code to expect a terminal of 80 characters wide and 24 rows high

import math
import pyfiglet

print(pyfiglet.figlet_format("Investment Calculator", justify = "center", font = "slant"))

# User input questions with number restrictions
while True:
    try:
        starting_balance = float(input("Please enter your starting balance:\n"))
        break
    except ValueError:
        print("Please enter a number as your starting balance....")

while True:
    try:
        interest_rate = float(input("Please enter the interest rate:\n"))
        break
    except ValueError:
        print("Please enter a number as the interest rate....")

# User input question with text 

increment_rate = input("Increment timeframe (daily, weekly, monthly, yearly):\n")
increment_rate = increment_rate.lower()

while increment_rate != "daily" and increment_rate != "weekly" and increment_rate != "monthly" and increment_rate != "yearly":
    increment_rate = input("Please enter either daily, weekly, monthly or yearly:\n")
    increment_rate = increment_rate.lower()

while True:
    try:
        additional_deposit = float(input("Additional deposit at each increment stage (optional):\n"))
        break
    except ValueError:
        print("Please enter a number as the deposit amount....")

while True:
    try:
        compound_period = int(input("Investment period length in years:\n"))
        break
    except ValueError:
        print("Please enter a number as the investment period length....\n")


# Working on calculate input
"""
calculate = input("Would you like to calculate?:\n")
"""

# Calculating the correct rate as a decimal
real_interest_rate = interest_rate * 0.01

# If statement based on the users increment_rate input
if increment_rate == "daily":
    increment_rate = 365
elif increment_rate == "weekly":
    increment_rate = 52
elif increment_rate == "monthly":
    increment_rate = 12
else:
    increment_rate = 1

# Create while statement to loop through increments and increment balance by interest rate and additional deposit rate

increments = increment_rate * compound_period
i = 0
while i < increments:
    starting_balance = starting_balance * (1 + real_interest_rate) + additional_deposit
    i += 1
    if i == increments:
        break

#print(starting_balance)
print(format(starting_balance, '.2f'))