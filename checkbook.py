'''
Write python version 3 code creates a checkbook program that runs once the file is opened from the command line. The checkbook program needs to welcome
the user with '\n~~~ Welcome to your command line checkbook ~~~\n'. The program then prompts the user 'What would you like to do?\n'. The file ledger.txt will
be used to store the float current_balance. If the variable current_balance doesn't exist, create it. The following will be displayed to the users as their choices:
'1) view current_balance', '2) record a debt (withdrawl)', '3) record a credit(deposit)', '4) exit'. If the user enters 1, then the program displays the
current_balance from the ledger.txt file. If the user enters 2, then the program will prompt the user with 'How much is the debit?\n\n' and the entered float will 
be checked to make sure it is a valid float and then subtracted from the current_balance and saved as the new current_balance. If the user enters 3, then the program 
will prompt the user with 'How much is the credit\n\n? and the entered float will be checked to make sure it is a valid float and then added to the current-balance 
and saved as the new current_balance. If the user enter 4, then the program will display 'Thanks, have a great day!\n' and exit back to the terminal prompt. If the 
user enters any other response, then display 'That response is not allowed'. The program needs to continue to loop until the user selects 4 to exit.

'''

# checkbook program

# print the welcome message
print("\n~~~ Welcome to your command line checkbook ~~~\n")

# initialize the balance to 0 if it doesn't exist in ledger.txt
try:
    with open("ledger.txt", "r") as ledger_file:
        current_balance = float(ledger_file.read().strip())
except FileNotFoundError:
    with open("ledger.txt", "w") as ledger_file:
        ledger_file.write("0")
    current_balance = 0

# loop until user selects option 4 for exit
while True:
    # prompt the user for their choice
    choice = input("What would you like to do?\n"
                   "1) view current balance\n"
                   "2) record a debt (withdrawl)\n"
                   "3) record a credit (deposit)\n"
                   "4) exit\n\n")

    # view current balance
    if choice == "1":
        print("\nCurrent balance:", current_balance, "\n")

    # record a debt (withdrawl)
    elif choice == "2":
        debit = input("How much is the debit?\n\n")
        try:
            debit = float(debit)
            current_balance -= debit
            with open("ledger.txt", "w") as ledger_file:
                ledger_file.write(str(current_balance))
        except ValueError:
            print("Invalid debit amount. Please enter a valid number.\n")

    # record a credit (deposit)
    elif choice == "3":
        credit = input("How much is the credit?\n\n")
        try:
            credit = float(credit)
            current_balance += credit
            with open("ledger.txt", "w") as ledger_file:
                ledger_file.write(str(current_balance))
        except ValueError:
            print("Invalid credit amount. Please enter a valid number.\n")

    # exit the program
    elif choice == "4":
        print("\nThanks, have a great day!\n")
        break

    # invalid choice
    else:
        print("That response is not allowed.\n")
