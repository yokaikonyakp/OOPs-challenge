# Challenge 5: Handling a Bank Account
# 🔴 In this challenge, you will define methods for handling a bank account using concepts of inheritance.

# Problem statement

# In this challenge, we will be extending the previous challenge and implementing methods in the parent class and its corresponding child class.

# The initializers for both classes have been defined for you.

# Task 1

# In the Account class, implement the getBalance() method that returns balance.

# Task 2

# In the Account class, implement the deposit(amount) method that adds amount to the balance.

# It does not return anything.

# Sample input

# balance = 2000
# deposit(500)
# getbalance()
# Sample output

# 2500
# Task 3

# In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance.

# It does not return anything.

# Sample input

# balance = 2000
# withdrawal(500)
# getbalance()
# Sample output

# 1500
# Task 4

# In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance.

# Below is the formula for calculating the interest amount:

# Sample input

# balance = 2000
# interestRate = 5
# interestAmount()
# Sample output

# 100
# The following figure shows what the result should logically look like:


class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

#using get method to return the value of 'balance'
    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate


#'interestAmount' method is implemented to calculate and return
# the interest amount based on current 'balance'
    def interestAmount(self):
        return (self.balance * self.interestRate) / 100




account = Account("Ashish", 2000)
print(account.getBalance())  

account.deposit(500)
print(account.getBalance()) 

account.withdrawal(500)
print(account.getBalance())  

savings_account = SavingsAccount("Ashish", 2000, 5)
print(savings_account.interestAmount())  
