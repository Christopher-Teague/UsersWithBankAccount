class BankAccount:

    bank_name = "First National Dojo"
    
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.checking_account = BankAccount(0.01, 0)
        self.savings_account = BankAccount(0.02, 0)
        # self.account_balance = 0

    # def make_deposit(self,ammount):
    #     self.account_balance += ammount
    #     return self

    # def make_withdrawal(self, ammount):
    #     self.account_balance -= ammount
    #     return self

    # def display_user_balance(self):
    #     print(f"User: {self.name}, Balance: ${self.account_balance}")
    #     return self

    # def transfer_money(self, ammount, User):
    #     self.account_balance -= ammount
    #     User.account_balance += ammount
    #     return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
keanu = User("Keanu Reeves", "keanu@thematrix.com")

guido.savings_account.deposit(100)
guido.savings_account.display_account_info()
guido.savings_account.yield_interest()
guido.savings_account.display_account_info()
guido.checking_account.withdraw(5)
guido.checking_account.display_account_info()