class BankAccount:
    account_balance = 0
    accounts =[]
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")
        return self
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * self.int_rate
        else:
            print("false")
        return self
    @classmethod
    def print_all_accounts(cls):
        for accounts in cls.accounts:
            accounts.display_account_info()

#TODO create 2 accounts
mondo = BankAccount(.02,200)
# print(mondo.int_rate)
jessica = BankAccount(.01,400)

#TODO To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
mondo.deposit(400).deposit(200).deposit(400).withdraw(600).yield_interest().display_account_info()

#TODO To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
jessica.deposit(1200).deposit(800).withdraw(200).withdraw(600).withdraw(200).withdraw(400).yield_interest().display_account_info()

BankAccount.print_all_accounts()