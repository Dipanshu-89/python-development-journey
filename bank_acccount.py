class Account:
    def __init__(self,bal,acc_no):
        self.balance=bal
        self.account_number=acc_no
    def debit(self,amount):
        self.balance-=amount
        print("your debit amount was rs.",amount)
        print("your available balance is rs.",self.balance)
    def credit(self,amount_1):
        self.balance+=amount_1
        print("your credit amount is rs.",amount_1)
        print("your available balance is rs.",self.balance)
    def check_balance(bal):
        return bal
A1=Account(int(input("enter your bank balance:")),int(input("enter your account number:")))
print("your acc. no.:",A1.account_number)
print("your bank balance is:",A1.balance)
A1.debit(int(input("enter your amount for debit: ")))
A1.credit(int(input("enter your credited amount:")))

    