# File Name:    Project.py
# Author:       Deirdre Connolly
# Description:  Project - 25%
# Due:          22/04/2018


import os
import random


line = ("-" * 50)


# WELCOME MESSAGE
welcome = "~~~~~~~~~~~~~~~ Welcome to CIT Bank ~~~~~~~~~~~~~~~"
print(welcome)


# MENU
def menu():
    accounts = load_bank("bank.txt")
    menu = ("Press 1 to open an account" + "\n" +
            "Press 2 to close an account" + "\n" +
            "Press 3 to withdraw money" + "\n" +
            "Press 4 to deposit money" + "\n" +
            "Press 5 to generate a report" + "\n" +
            "Press 6 to quit")

    while True:
        print(menu)
        option = int(input("Option selected >>> "))

        if option == 6:                                         # Quit, writes data to file
            break
        elif option == 1:                                       # Open account
            open_account(accounts)
        elif option == 2:                                       # Close account
            close_account(accounts)
        elif option == 3:                                       # Withdraw money
            withdraw_money(accounts)
        elif option == 4:                                       # Deposit money
            deposit_money(accounts)
        elif option == 5:                                       # Generate report
            gen_report(accounts)
        else:
            print("Invalid input, please try again.")

        save_bank("bank.txt", accounts)


# OPEN ACCOUNT
def open_account(accounts):
    print(line)
    print("OPENING NEW ACCOUNT")
    account_num = new_account(accounts)
    balance = input_money(accounts, "Enter balance >>> €")

    while True:
        name = input("Account name >>> ")
        name = check_name(name)                                 # Name can only consist of letters/spaces
        if name is None:
            print("Invalid input, please try again.")
        else:
            break

    accounts[account_num] = {"Balance": balance, "Name": name}
    print("Account #{} has successfully been opened.".format(account_num))


# CLOSE ACCOUNT
def close_account(accounts):
    print(line)
    print("CLOSING ACCOUNT")
    account_num = input_account_num(accounts)
    del accounts[account_num]
    print("Account #{} has been deleted.".format(account_num))


# WITHDRAW MONEY
def withdraw_money(accounts):
    print(line)
    print("WITHDRAW MONEY")
    account_num = input_account_num(accounts)
    withdraw_money = input_money(accounts, "Amount to withdraw >>> €")
    balance = accounts[account_num]["Balance"]
    if balance >= withdraw_money:
        new_balance = (balance - withdraw_money)
        accounts[account_num] = {"Balance": new_balance, "Name": accounts[account_num]["Name"]}
        print("Withdrawal successful. New balance >>> €{}".format(new_balance))
    else:                                                      # Insufficient funds to withdraw
        print("Insufficient funds. Your balance >>> €{}".format(balance))


# DEPOSIT MONEY
def deposit_money(accounts):
    print(line)
    print("DEPOSIT MONEY")
    account_num = input_account_num(accounts)
    deposit_money = input_money(accounts, "Amount to deposit >>> €")
    balance = accounts[account_num]["Balance"]
    new_balance = (balance + deposit_money)
    accounts[account_num] = accounts[account_num] = {"Balance": new_balance, "Name": accounts[account_num]["Name"]}
    print("Deposit successful. New balance >>> €{}".format(new_balance))


# GENERATE REPORT
def gen_report(accounts):
    print(line)
    print("GENERATE REPORT")
    total_balance = 0
    max_deposit = None

    for x, y in accounts.items():
        total_balance += y["Balance"]

        if max_deposit is None:
            max_deposit = y["Balance"]
        elif max_deposit < y["Balance"]:
            max_deposit = y["Balance"]

        print("Account Number: #{}, Balance: €{}, Name: {}".format(x, y["Balance"], y["Name"]))

    print("\n" + "TOTAL BALANCE: €{}".format(total_balance) + "\n")


# OPEN FILE
def load_bank(file_name):
    if os.path.isfile(file_name):
        with open(file_name) as f:                              # F for file
            accounts = {}
            for line in f:
                account, balance, name = line.split(",")        # Separates info in line with a comma
                accounts[account.strip()] = {"Balance": int(balance.strip()),
                                             "Name": name.strip()}
            return accounts
    else:
        return {}


# WRITE TO FILE
def save_bank(file_name, accounts):
    with open(file_name, "w") as f:                             # W for write to file
        for n, v in accounts.items():
            f.write("{}, {}, {}\n".format(n, v["Balance"], v["Name"]))


# NEW ACCOUNT NUMBER RANDOMLY GENERATED
def new_account(accounts):
    account_num = ""                                            # Starts off empty
    while True:
        for i in range(0, 6):                                   # 6-digit number
            num = random.randint(0,9)                           # Using integers 0-9
            account_num += str(num)
        if account_num not in accounts:                         # If number already exists, generates another
            break
    return account_num


def convert_money(balance_str):
    try:                                                        # Convert money from a string to an integer
        balance = int(balance_str)
        if balance >= 0:                                        # Balance must be positive
            return balance
        else:
            return None
    except ValueError:                                          # Not an integer
        return None


# CHECK NAME
def check_name(name):                                           # Name can only consist of letters/spaces
    for c in name:                                              # C for character
        if not(c.isalpha() or c == " "):
            return None
    return name


def input_account_num(accounts):
    while True:
        account_num = input("Enter account number >>> #")
        if account_num not in accounts:                         # Check that the account exists
            print("ERROR: Account #{} does not exist.".format(account_num))
        else:                                                   # Account exists, returns account number
            return account_num


def input_money(accounts, msg="Amount to deposit >>> €"):
    while True:
        money_str = input(msg)
        money = convert_money(money_str)                        # Check for positive integer
        if money is None:
            print("Invalid input, please try again.")
        else:
            return money


menu()                                                          # Runs the function that begins the program

