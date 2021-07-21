import sys  
#@purpose : to print hello world 
#@concept : the idea is to write a basic code and check it's exeuction  in terms of all setup accurate .
#@Hashtag : #python #coding 
#@code 

class BankAccount:
    def __init__(self, account_number):
        self.account_number = str(account_number)
        self.balance = 0

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")

    def deposit(self, amount):
        self.balance += amount


def transfer_amount(acc_1, acc_2, amount):
    acc_1.withdraw(amount)
    acc_2.deposit(amount)


user_1 = BankAccount("001")
user_2 = BankAccount("002")
user_1.deposit(250)
user_2.deposit(100)

print "Input money at User1 and User2 :"

print("User 1 Balance : {}/-".format(user_1.get_balance()))
print("User 2 Balance : {}/-".format(user_2.get_balance()))

transfer_amount(user_1, user_2, 50)

print("Transferring 50/- from User 1 to User 2")

print("User 1 Balance : {}/-".format(user_1.get_balance()))
print("User 2 Balance : {}/-".format(user_2.get_balance()))

#@output : hello world 
