import json

class BankAccount:
    def __init__(self, account_number, balance, holder, currency, status):
        self.__account_number = self.validateAccountNumber(account_number)
        self.__balance = self.validateBalance(balance)
        self.__holder = self.validateHolder(holder)
        self.__currency = self.validateCurrency(currency)
        self.__status = self.validateStatus(status)

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def holder(self):
        return self.__holder
    
    @property
    def currency(self):
        return self.__currency
    
    @property
    def status(self):
        return self.__status
    
    @balance.setter
    def balance(self, new_balance):
        self.__balance = self.validateBalance(new_balance)

    @account_number.setter
    def account_number(self, new_account_number):
        self.__account_number = self.validateAccountNumber(new_account_number)
    
    @holder.setter
    def holder(self, new_holder):
        self.__holder = self.validateHolder(new_holder)
    
    @currency.setter
    def currency(self, new_currency):
        self.__currency = self.validateCurrency(new_currency)

    @status.setter
    def status(self, new_status):
        self.__status = self.validateStatus(new_status)

    def validateBalance(self, balance):
        try:
            balance_number = float(balance)
            if balance_number < 0:
                raise ValueError("Balance must be a positive number or equal to zero.")
            return balance_number            
        except ValueError:
            raise ValueError("Balance must be a valid number.")
        
    def validateAccountNumber(self, account_number):
        try:
            account = int(account_number)
            if len(str(account_number)) != 12:
                raise ValueError("The account number must be 12 digits long.")
            if account <= 0:
                raise ValueError("The account number must be a positive number.")  
            return account        
        except ValueError:
            raise ValueError("The account number must be numeric and 12 digits long.")
    
    def validateHolder(self, holder):
        try:
            if not holder or not holder.replace(" ", "").isalpha():
                raise ValueError("Holder must be a non-empty string containing only alphabetic characters and spaces.")
            return holder
        except ValueError:
            raise ValueError("The holder's name is invalid.")
    
    def validateCurrency(self, currency):
        try:
            currency = currency.lower()
            if currency not in ["pesos", "dolares", "euros", "guaranies"]:
                raise ValueError(f"Currency must be one of the following: 'pesos', 'dolares', 'euros', 'guaranies'.")
            return currency
        except Exception as e:
            raise ValueError(f"Invalid currency: {e}")
        
    def validateStatus(self, status):
        try:
            status = status.lower()
            if status not in ["active", "inactive"]:
                raise ValueError("Status must be 'active' or 'inactive'.")
            return status
        except Exception as e:
            raise ValueError(f"Invalid status: {e}")
    
    def toDict(self):
        return {
            "account_number": self.account_number,
            "balance": self.balance,
            "holder": self.holder,
            "currency": self.currency,
            "status": self.status
        }
    
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, holder, currency, status, withdrawal_limit, interest_rate):
        super().__init__(account_number, balance, holder, currency, status)
        self.__withdrawal_limit = self.validateWithdrawalLimit(withdrawal_limit)
        self.__interest_rate = self.validateInterestRate(interest_rate)

    @property
    def withdrawal_limit(self):
        return self.__withdrawal_limit
    
    @property
    def interest_rate(self):
        return self.__interest_rate
    
    @withdrawal_limit.setter
    def withdrawal_limit(self, new_withdrawal_limit):
        self.__withdrawal_limit = self.validateWithdrawalLimit(new_withdrawal_limit)
    
    @interest_rate.setter
    def interest_rate(self, new_interest_rate):
        self.__interest_rate = self.validateInterestRate(new_interest_rate)

    def validateWithdrawalLimit(self, withdrawal_limit):
        try:
            withdrawal_limit = float(withdrawal_limit)
            if withdrawal_limit < 0:
                raise ValueError("The withdrawal limit cannot be negative.")
            if self.currency == "Pesos":
                if not (80000 <= withdrawal_limit <= 170000):
                    raise ValueError(f"The withdrawal limit for Argentine pesos must be between 80,000 and 170,000.")
            elif self.currency == "Dolares":
                if not (200 <= withdrawal_limit <= 300):
                    raise ValueError(f"The withdrawal limit for U.S. dollars must be between 200 and 300.")
            elif self.currency == "Euros":
                if not (200 <= withdrawal_limit <= 300):
                    raise ValueError(f"The withdrawal limit for euros must be between 200 and 300.")
            elif self.currency == "Guaranies":
                if not (150000000 <= withdrawal_limit <= 280000000):
                    raise ValueError(f"The withdrawal limit for guaraníes must be between 150,000,000 and 280,000,000.")
            return withdrawal_limit
        except ValueError:
            raise ValueError("The withdrawal limit is invalid. It must be a non-negative numerical value.")

    def validateInterestRate(self, interest_rate):
        try:
            interest_rate = float(interest_rate)
            if interest_rate < 0:
                raise ValueError("The interest rate cannot be negative.")
            if self.currency == "Pesos":
                if not (30 <= interest_rate <= 35):
                    raise ValueError(f"The interest rate for Argentine pesos should be between 30% and 35%.")
            elif self.currency == "Dolares":
                if not (20 <= interest_rate <= 25):
                    raise ValueError(f"The interest rate for U.S. dollars should be between 20% and 25%.")
            elif self.currency == "Euros":
                if not (20 <= interest_rate <= 30):
                    raise ValueError(f"The interest rate for euros should be between 20% and 30%.")
            elif self.currency == "Guaranies":
                if not (30 <= interest_rate <= 35):
                    raise ValueError(f"The interest rate for guaraníes should be between 30% and 35%.")
            return interest_rate
        except ValueError:
            raise ValueError("The interest rate is invalid. It must be a non-negative numerical value.")

    def toDict(self):
        data = super().toDict()
        data['withdrawal_limit'] = self.withdrawal_limit
        data['interest_rate'] = self.interest_rate
        return data

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, holder, currency, status, monthly_fee):
        super().__init__(account_number, balance, holder, currency, status)
        self.__monthly_fee = self.validateMonthlyFee(monthly_fee)

    @property
    def monthly_fee(self):
        return self.__monthly_fee
    
    @monthly_fee.setter
    def monthly_fee(self, new_monthly_fee):
        self.__monthly_fee = self.validateMonthlyFee(new_monthly_fee)

    def validateMonthlyFee(self, monthly_fee):
        try:
            monthly_fee = float(monthly_fee)
            if monthly_fee < 0:
                raise ValueError("The monthly fee cannot be negative.")
            if monthly_fee > 20:
                raise ValueError("The monthly fee cannot exceed 20.")
            return monthly_fee
        except ValueError:
            raise ValueError("The monthly fee is invalid. It must be a non-negative numerical value not exceeding 20.")

    def toDict(self):
        data = super().toDict()
        data['monthly_fee'] = self.monthly_fee
        return data
    
class AccountManagement:
    def __init__(self, file):
        self.file = file

    def readData(self):
        try:
            with open(self.file, 'r') as f:
                dat = json.load(f)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception (f"Error reading data from file: {error}.")
        else:
            return dat

    def saveData(self, dat):
        try:
            with open(self.file, 'w') as f:
                json.dump(dat, f, indent=4)
        except IOError as error:
            print(f"Error trying to save data to {self.file}: {error}.")
        except Exception as error:
            print(f"Unexpected error: {error}.")

    def createAccount(self, account):
        try:
            data = self.readData()
            account_number = account.account_number
            if not str(account_number) in data.keys():
                data[account_number] = account.toDict()
                self.saveData(data)
                print(f"Account {account_number} saved successfully.")
            else:
                print(f"Account {account_number} already exists.")
        except Exception as error:
            print (f"Unexpected error creating account: {error}.")

    def readAccount(self, account_number):
        try:
            data = self.readData()
            if str(account_number) in data:
                account_data = data[str(account_number)]

                account_data_transformed = {
                "account_number": account_data["account_number"],
                "balance": account_data["balance"],
                "holder": account_data["holder"],
                "currency": account_data["currency"],
                "status": account_data["status"]
            }
                
                if "interest_rate" in account_data:
                    account_data_transformed["withdrawal_limit"] = account_data["withdrawal_limit"]
                    account_data_transformed["interest_rate"] = account_data["interest_rate"]
                    account = SavingsAccount(**account_data_transformed)
                else:
                    account_data_transformed["monthly_fee"] = account_data["monthly_fee"]
                    account = CheckingAccount(**account_data_transformed)

                print(f"Account found with number {account_number}.")
                for key, value in account_data_transformed.items():
                    print(key, ":", value)
                return account
            else:
                print(f"No account found with number {account_number}.")
            
        except Exception as e:
            print(f"Error reading account: {e}.")

    def updateAccount(self, account_number, new_status):
        try:
            data = self.readData()
            if account_number in data.keys():
                data[account_number]["status"] = new_status
                self.saveData(data)
                print(f"Status updated successfully for account {account_number}. Now it is {new_status}.")
            else:
                print(f"No account found with number {account_number}.")

        except Exception as e:
            print(f"Error updating account: {e}.")

    def deleteAccount(self, account_number):
        try:
            data = self.readData()
            if account_number in data.keys():
                del data[account_number]
                self.saveData(data)
                print(f"Account {account_number} deleted successfully.")
            else:
                print(f"No account found with number {account_number}.")

        except Exception as e:
            print(f"Error deleting account: {e}.")