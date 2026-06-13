class Bank:
    def __init__(self, Name, Balance):
        self.Name = Name
        self.Balance = Balance
    def deposit(self, Amount):
        self.Balance = self.Balance + Amount
    def withdraw(self, Amount):
        if Amount > self.Balance:
            print("Insufficient balance!")
        else:
            self.Balance = self.Balance - Amount

self = Bank("Sujitha", 5000)
self.deposit(2000)
self.withdraw(1000)
print(self.Name)
print(self.Balance)

acc1= Bank("Sujitha", 5000)
acc1.deposit(2000)
acc1.withdraw(8000)
print(acc1.Name)
print(acc1.Balance)

