class BankAccount:
    def __init__(self,owner,balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.owner = owner
        self.balance = balance
        
     
    
    def deposit(self,amount):
        if amount < 0:
            raise ValueError("Deposit cannot be negative")
        self.balance += amount
        return self.balance
        
    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("Withdraw amount can't be more than balance")
        self.balance -= amount
        return self.balance

acc1 = BankAccount("Rahul",100)
print(acc1.deposit(20))
print(acc1.withdraw(10))