# Challenge 4: Implement a Banking Account

# 🔴 In this challenge, implement a banking account using the concepts of inheritance.
# Problem statement

# Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.

# Task 1

# 👉 Implement properties as instance variables, and set them to None or 0.

# Account has the following properties:

#     • title
#     • Balance
# SavingsAccount has the following properties:

#     • interestRate
# Task 2

# Create an initializer for Account class. The order of parameters should be the following, where Ashish is the title, and 5000 is the account balance:

# Account("Ashish", 5000)

# Task 3

# Implement properties as instance variables, and set them to None or 0.

# Create an initializer for the SavingsAccount class using the initializer of the Account class in the order below:

# Account("Ashish", 5000, 5)

# Here, Ashish is the title and 5000 is the balance and 5 is the interestRate.



class Account:     #parent Class
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance


#Child Class
class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate     #(additional property)


#creating "Account" object
account = Account("Ashish", 5000)
print(account.title)    
print(account.balance)  


#Creating "SavingsAccount" object
savings_account = SavingsAccount("Ashish", 5000, 5)
print(savings_account.title)         
print(savings_account.balance)       
print(savings_account.interestRate)  



