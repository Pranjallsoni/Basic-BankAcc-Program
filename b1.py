class Account:
    def __init__(self,balc,acc):
        self.balance = balc 
        self.account = acc
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount , "was debited from your account.")
        print("Total amount debited was = ", self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited from your account.")
        print("Total amount credited was = ", self.get_balance())

    def get_balance(self):
        return self.balance
        
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(7000)