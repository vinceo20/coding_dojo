class BankAccount:

    all_accounts = []

    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print("================")
        print(f"Current Balance: ${self.balance}")
        print(f"Interest rate: {self.interest_rate}%")
        print("================")

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def display_all_account_info(cls):
        for account in cls.all_accounts:
            print("================")
            print(f"Current Balance: ${account.balance}")
            print(f"Interest rate: {account.interest_rate}%")
            print("================")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, interest_rate = 0.2, balance = 0):
        new_account = BankAccount(interest_rate, balance)
        self.accounts.append(new_account)
        return self

    def make_deposit(self, account_index, amount):
        if account_index < len(self.accounts):
            self.accounts[account_index].balance += amount
        else :
            print("Account doesn't exist.")
        return self

    def make_withdrawal(self, account_index, amount):
        if account_index < len(self.accounts):
            self.accounts[account_index].balance -= amount
        else:
            print("Account doesn't exist.")
        return self

    def display_user_info(self):
        print("********************************")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Total accounts: {len(self.accounts)}")
        index = 0
        for account in self.accounts:
            print("---------------------")
            print(f"Account number: {index}")
            print(f"Account Balance: ${account.balance}")
            index += 1
            print("---------------------")
        print("********************************")
        return self

    def transfer_money(self, amount, other_user, my_account_index, other_account_index):
        if my_account_index < len(self.accounts) and other_account_index < len(other_user.accounts):
            if self.accounts[my_account_index].balance > amount:
                self.make_withdrawal(my_account_index, amount)
                other_user.make_deposit(other_account_index, amount)
            else:
                print("ALERT: Unable to process the transfer; Not enough balance")
        else :
            print("Account doesn't exist. Please check accounts info.")


user_1 = User("Jihwan Eo", "email@email.com")
user_1.add_account().make_deposit(0,1000).display_user_info()

user_2 = User("Luan Zou", "email2@gmail.com")
user_2.add_account().make_deposit(0,1000).display_user_info()

user_1.transfer_money(10000, user_2, 0, 0)

user_1.display_user_info()
user_2.display_user_info()