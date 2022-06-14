# Write your code to expect a terminal of 80 characters wide and 24 rows high

import math
import sys
import time
import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init()
from tabulate import tabulate
from functions import typewrite


print(Fore.GREEN + pyfiglet.figlet_format("Investment Calculator", justify="center", font="slant"))

print(Fore.WHITE)
typewrite('"Most people overestimate what they can do in one year and underestimate\nwhat they can do in ten years."- Bill Gates \n')
print("\n")

typewrite("This calculator has been built to show the power of consistent long term\nsaving and investing.\n")
print("\n")

user_selections = [
    ["BALANCE", "INTEREST RATE", "TIMEFRAME", "DEPOSIT", "YEARS"]
]

selections = []

while True:
    try:
        starting_balance = float(input("Please enter your starting balance:\n"))
        print("\n")
        break
    except ValueError:
        print(Fore.RED)
        typewrite("Please enter a number as your starting balance....\n")
        print(Fore.WHITE + "\n")

selections.append(starting_balance)

while True:
    try:
        interest_rate = float(input("Please enter the interest rate:\n"))
        print("\n")
        break
    except ValueError:
        print(Fore.RED)
        typewrite("Please enter a number as the interest rate....\n")
        print(Fore.WHITE + "\n")
selections.append(interest_rate)

increment_list = ["daily", "daily ", "weekly", "weekly ", "monthly", "monthly ", "yearly", "yearly "]
increment_rate = input("Increment timeframe (daily, weekly, monthly, yearly):\n")
increment_rate = increment_rate.lower()

while (increment_rate not in increment_list):
    print(Fore.RED)
    typewrite("Please enter either daily, weekly, monthly or yearly....\n")
    print(Fore.WHITE + "\n")
    increment_rate = input("Increment timeframe (daily, weekly, monthly, yearly):\n")
    print("\n")
    increment_rate = increment_rate.lower()
selections.append(increment_rate)

while True:
    try:
        additional_deposit = float(input("Additional deposit at each increment stage:\n"))
        print("\n")
        break
    except ValueError:
        print(Fore.RED)
        typewrite("Please enter a number as the deposit amount....\n")
        print(Fore.WHITE + "\n")

selections.append(additional_deposit)

while True:
    try:
        compound_period = int(input("Investment period length in years:\n"))
        print("\n")
        break
    except ValueError:
        print(Fore.RED)
        typewrite("Please enter a number as the investment period length....\n")
        print(Fore.WHITE + "\n")

selections.append(compound_period)

user_selections.append(selections)

typewrite("Your selections are as follows:\n")
print("\n")

print(tabulate(user_selections, tablefmt="plain"))
print("\n")



if increment_rate == "daily":
    increment_rate = 365
elif increment_rate == "weekly":
    increment_rate = 52
elif increment_rate == "monthly":
    increment_rate = 12
else:
    increment_rate = 1

real_interest_rate = interest_rate * 0.01

increments = increment_rate * compound_period

final_list = [
    ["MONTH","BALANCE","DEPOSITS","GAIN"],
    ]

gain = 0
i = 0
while i < increments:
    year_end_list = []
    deposits = additional_deposit * i
    if i%increment_rate == 0:
        year_end_list.append(i)
        year_end_list.append(format(starting_balance, '.2f'))
        year_end_list.append(deposits)
        year_end_list.append(format(gain, '.2f'))
        final_list.append(year_end_list)
    gain = gain + starting_balance * (1 + real_interest_rate) - starting_balance
    starting_balance = starting_balance * (1 + real_interest_rate) + additional_deposit
    i += 1
    if i == increments:
        year_end_list = []
        deposits = additional_deposit * i
        year_end_list.append(i)
        year_end_list.append(format(starting_balance, '.2f'))
        year_end_list.append(deposits)
        year_end_list.append(format(gain, '.2f'))
        final_list.append(year_end_list)
        break
    
print(tabulate(final_list, tablefmt="plain"))