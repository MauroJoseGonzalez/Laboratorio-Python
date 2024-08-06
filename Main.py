import os
import platform

from Laboratorio import (
    BankAccount,
    SavingsAccount,
    CheckingAccount,
    AccountManagement
)

def cleanScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def showMenu():
    print("===== Bank Account Management =====")
    print("1. Add savings account")
    print("2. Add checking account")
    print("3. Search account by number")
    print("4. Update status")
    print("5. Delete account by number")
    print("6. Show all accounts")
    print("7. Exit")
    print("===================================")

def addAccount(manage, account_type):
    try:
        account_number = input("Enter account number: ")
        balance = input("Enter balance: ")
        holder = input("Enter account holder: ")
        currency = input("Enter currency: ")
        status = input("Enter account status: ")

        if account_type == "1":
            withdrawal_limit = float(input("Enter withdrawal limit: "))
            interest_rate = float(input("Enter interest rate: "))
            account = SavingsAccount(account_number, balance, holder, currency, status, withdrawal_limit, interest_rate)
        elif account_type == "2":
            monthly_fee = float(input("Enter monthly fee: "))
            account = CheckingAccount(account_number, balance, holder, currency, status, monthly_fee)
        else:
            print("Invalid option.")
            return

        manage.createAccount(account)
        input("Press Enter to continue...")

    except ValueError as e:
        print(f"Error: {e}.")
    except Exception as e:
        print(f"Unexpected error: {e}.")

def searchAccountByNumber(manage):
    number = input("Enter account number to search: ")
    manage.readAccount(number)
    input("Press Enter to continue...")

def deleteAccountByNumber(manage):
    number = input("Enter account number to delete: ")
    manage.deleteAccount(number)
    input("Press Enter to continue...")

def update_Status(manage):
    try:
        number = input("Enter account number to update status: ")
        status = input("Enter new status for the account [active/inactive]: ").lower()
        
        if status not in ["active", "inactive"]:
            raise ValueError("Invalid status. Only 'active' or 'inactive' are allowed.")   
        manage.updateAccount(number, status)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        input("Press Enter to continue...")


def showAccounts(manage):
    print("============ Full Account List ============")
    for account in manage.readData().values():
        if "interest_rate" in account:
            print(f"{account['account_number']} - interest rate: {account['interest_rate']}")
        else:
            print(f"{account['account_number']} - monthly fee: {account['monthly_fee']}")
    print("===========================================")
    input("Press Enter to continue...")

if __name__ == "__main__":
    file_accounts = "accounts_db.json"
    manage_accounts = AccountManagement(file_accounts)

    while True:
        cleanScreen()
        showMenu()
        option = input("Select an option: ")

        if option == '1' or option == '2':
            addAccount(manage_accounts, option)

        elif option == '3':
            searchAccountByNumber(manage_accounts)

        elif option == '4':
            update_Status(manage_accounts)

        elif option == '5':
            deleteAccountByNumber(manage_accounts)

        elif option == '6':
            showAccounts(manage_accounts)

        elif option == '7':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please enter a valid option: [1-7].")
            input("Press Enter to continue...")
