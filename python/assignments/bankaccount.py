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

account_1 = BankAccount(0.1,1000)
account_2 = BankAccount(0.2,10000)

account_1.deposit(100).deposit(200).deposit(800).withdraw(100).yield_interest().display_account_info()
account_2.deposit(10000).deposit(20000).withdraw(1000).withdraw(2000).withdraw(3000).withdraw(4000).yield_interest().display_account_info()

BankAccount.display_all_account_info()
# account_1.deposit(100).deposit(200).deposit(800).withdraw(100).yield_interest()
# account_1.display_account_info