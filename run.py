# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import pyfiglet
import colorama
from colorama import Fore
colorama.init()
from tabulate import tabulate
from functions import typewrite, restart_program


print(Fore.GREEN + pyfiglet.figlet_format("Investment Calculator", justify="center", font="slant"))

print(Fore.WHITE)
typewrite('''"Most people overestimate what they can do in one year and underestimate
what they can do in ten years."- Bill Gates \n''')
print("\n")

typewrite("""This calculator has been built to show the power of consistent long term
saving and investing.\n""")
print("\n")

user_selections = [
    ["BALANCE", "INTEREST RATE", "TIMEFRAME", "ADDITIONAL DEPOSIT", "YEARS"]
]

final_list = [
    ["INCREMENTS", "DEPOSITS", "GAIN", "BALANCE"],
    ]

selections = []

increment_list = ["daily", "daily ", "weekly", "weekly ", "monthly", "monthly ", "yearly", "yearly "]

while True:
    try:
        starting_balance = float(input("Please enter your starting balance:\n"))
        print("\n")
        break
    except ValueError:
        print(Fore.RED)
        typewrite("Please enter a number as your starting balance....\n")
        print(Fore.WHITE + "\n")

while True:
    try:
        interest_rate = float(input("Please enter the interest rate:\n"))
        print("\n")
        break
    except ValueError:
        print(Fore.RED)
        typewrite("Please enter a number as the interest rate....\n")
        print(Fore.WHITE + "\n")

INCREMENT_RATE = input("Increment timeframe (daily, weekly, monthly, yearly):\n")
INCREMENT_RATE = INCREMENT_RATE.lower()
while INCREMENT_RATE not in increment_list:
    print(Fore.RED)
    typewrite("Please enter either daily, weekly, monthly or yearly....\n")
    print(Fore.WHITE + "\n")
    INCREMENT_RATE = input("Increment timeframe (daily, weekly, monthly, yearly):\n")
    print("\n")
    INCREMENT_RATE = INCREMENT_RATE.lower()

while True:
    try:
        print("\n")
        additional_deposit = float(input("Additional deposit at each increment stage:\n"))
        print("\n")
        break
    except ValueError:
        print(Fore.RED)
        typewrite("Please enter a number as the deposit amount....\n")
        print(Fore.WHITE + "\n")

while True:
    try:
        compound_period = int(input("Investment period length in years:\n"))
        print("\n")
        break
    except ValueError:
        print(Fore.RED)
        typewrite("Please enter a number as the investment period length....\n")
        print(Fore.WHITE + "\n")

selections.append(starting_balance)
selections.append(interest_rate)
selections.append(INCREMENT_RATE)
selections.append(additional_deposit)
selections.append(compound_period)
user_selections.append(selections)

typewrite("Your selections are as follows:\n")
print("\n")

print(tabulate(user_selections, tablefmt="grid"))
print("\n")

while True:
    calculate_list = ["yes", "yes ", "y", "y "]
    reload_list = ["no", "no ", "n", "n "]
    calculate = input("Are you happy with your selections?:\n")
    print("\n")
    if calculate.lower() in reload_list:
        restart_program()
    elif calculate.lower() in calculate_list:
        typewrite(f"Your annual results over an investment period of {compound_period} years are as follows:\n")
        time.sleep(1.0)
        print("\n")
        break
    else:
        print(Fore.RED)
        typewrite("Please enter yes or no to proceed....\n")
        print(Fore.WHITE + "\n")


if INCREMENT_RATE == "daily":
    INCREMENT_RATE = 365
elif INCREMENT_RATE == "weekly":
    INCREMENT_RATE = 52
elif INCREMENT_RATE == "monthly":
    INCREMENT_RATE = 12
else:
    INCREMENT_RATE = 1

real_interest_rate = interest_rate * 0.01
increments = INCREMENT_RATE * compound_period

GAIN = 0
i = 0
while i < increments:
    year_end_list = []
    deposits = additional_deposit * i
    GAIN_LENGTH = len(str(GAIN))
    BALANCE_LENGTH = len(str(starting_balance))
    if i % INCREMENT_RATE == 0:
        year_end_list.append(i)
        year_end_list.append(format(deposits, '.2f'))
        if GAIN_LENGTH > 20:
            year_end_list.append(format(GAIN, '20e'))
        else:
            year_end_list.append(format(GAIN, '.2f'))
        if BALANCE_LENGTH > 20:
            year_end_list.append(format(starting_balance, '20e'))
        else:
            year_end_list.append(format(starting_balance, '.2f'))
        final_list.append(year_end_list)
    GAIN = GAIN + starting_balance * (1 + real_interest_rate) - starting_balance
    starting_balance = starting_balance * (1 + real_interest_rate) + additional_deposit
    i += 1
    if i == increments:
        year_end_list = []
        deposits = additional_deposit * i
        year_end_list.append(i)
        year_end_list.append(format(deposits, '.2f'))
        if GAIN_LENGTH > 20:
            year_end_list.append(format(GAIN, '20e'))
        else:
            year_end_list.append(format(GAIN, '.2f'))
        if BALANCE_LENGTH > 20:
            year_end_list.append(format(starting_balance, '20e'))
        else:
            year_end_list.append(format(starting_balance, '.2f'))
        final_list.append(year_end_list)
        break

print(tabulate(final_list, tablefmt="grid"))
print(Fore.GREEN + "\n")
typewrite("""If you're lucky enough to be a Quintillionaire or better at the end of
your investment, your results will be displayed as exponential numbers.""")
print(Fore.WHITE + "\n")
