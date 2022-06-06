# Write your code to expect a terminal of 80 characters wide and 24 rows high

import math
import pyfiglet

print(pyfiglet.figlet_format("Investment Calculator", justify = "center", font = "slant"))

# User input questions 
starting_balance = int(input("Please enter your starting balance: "))
interest_rate = float(input("Please enter the interest rate: "))
increment_rate = input("Increment timeframe (daily, weekly, monthly, yearly: ")
additional_deposit = int(input("Additional deposit at each increment stage (optional): "))
compound_period = int(input("Investment period length in years: "))
calculate = input("Would you like to calculate?: ")
