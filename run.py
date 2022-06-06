# Write your code to expect a terminal of 80 characters wide and 24 rows high

import math
import pyfiglet

print(pyfiglet.figlet_format("Investment Calculator", justify = "center", font = "slant"))

# User input questions, need to add restrictions on inputs
starting_balance = float(input("Please enter your starting balance:\n"))
interest_rate = float(input("Please enter the interest rate:\n"))
increment_rate = input("Increment timeframe (daily, weekly, monthly, yearly):\n")
additional_deposit = int(input("Additional deposit at each increment stage (optional):\n"))
compound_period = int(input("Investment period length in years:\n"))
calculate = input("Would you like to calculate?:\n")


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


print(starting_balance)
