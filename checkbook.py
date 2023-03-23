'''
Write python version 3 code creates a checkbook program that runs once the file is opened from the command line. The checkbook program needs to welcome
the user with '\n~~~ Welcome to your command line checkbook ~~~\n'. The program then prompts the user 'What would you like to do?\n'. The file ledger.txt will
be used to store the float current_balance. If the variable current_balance doesn't exist, create it. The following will be displayed to the users as their choices:
'1) view current_balance', '2) record a debt (withdrawl)', '3) record a credit(deposit)', '4) exit'. If the user enters 1, then the program displays the
current_balance from the ledger.txt file. If the user enters 2, then the program will prompt the user with 'How much is the debit?\n\n' and the entered float will 
be subtracted from the current_balance and saved as the new current_balance. If the user enters 3, then the program will prompt the user with 'How much is the 
credit\n\n? and the entered float will be added to the current-balance and saved as the new current_balance. If the user enter 4, then the program will display 
'Thanks, have a great day!\n' and exit back to the terminal prompt. The program needs to continue to loop until the user selects 4 for exit.

'''

# Code to create a checkbook program

# Import necessary libraries
import os

# Welcome the user
print("\n~~~ Welcome to your command line checkbook ~~~\n")

# Check if the ledger.txt file exists
if os.path.exists("ledger.txt"):
    # Read the current_balance from the ledger.txt file
    with open("ledger.txt", "r") as ledger_file:
        current_balance = float(ledger_file.read().strip())
else:
    # Create the ledger.txt file and initialize the current_balance as 0
    with open("ledger.txt", "w") as ledger_file:
        current_balance = 0
        ledger_file.write(str(current_balance))

# Continuously prompt the user for a choice until they choose to exit
while True:
    print("What would you like to do?")
    print("1) view current_balance")
    print("2) record a debt (withdrawl)")
    print("3) record a credit (deposit)")
    print("4) exit\n")
    choice = int(input().strip())
    
    # View the current_balance
    if choice == 1:
        print("\nYour current_balance is: $%.2f\n" % current_balance)
    # Record a debt (withdrawl)
    elif choice == 2:
        debt = float(input("\nHow much is the debit?\n\n"))
        current_balance -= debt
        # Save the new current_balance to the ledger.txt file
        with open("ledger.txt", "w") as ledger_file:
            ledger_file.write(str(current_balance))
    # Record a credit (deposit)
    elif choice == 3:
        credit = float(input("\nHow much is the credit?\n\n"))
        current_balance += credit
        # Save the new current_balance to the ledger.txt file
        with open("ledger.txt", "w") as ledger_file:
            ledger_file.write(str(current_balance))
    # Exit the program
    elif choice == 4:
        print("\nThanks, have a great day!\n")
        break
    # Invalid choice
    else:
        print("\nInvalid choice, please enter a valid choice\n")
