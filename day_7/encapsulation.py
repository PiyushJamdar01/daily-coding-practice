class BankAccount:
    
    def __init__(self,balance):
        self.__balance = balance
        
    def deposite(self, amount):
        self.__balance += amount
        print("Deposited:", amount)
        
    def withdraw(self, amount):
        
        if amount <= 0:
            print("Enter a Valid Amount")
            
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw:",amount)
            
        else:
            print("Insufficient Balance")
            
    def show_balance(self):
        print("Balance:",self.__balance)
        
account = BankAccount(100000)

account.withdraw(10000)

account.show_balance()