class Atm:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.interface()
    def interface(self):
        user_input=input("""Welcome to virtual atm \nEnter 1 for create pin\nEnter 2 for change pin\nEnter 3 for check balance\nEnter 4 for withdraw\nEnter 5 for deposit\nanything for exit: """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        elif user_input == '5':
            self.deposit()
        else:
            exit()
    def create_pin(self):
        pin=input("create your pin:")
        self.pin=pin
        print("your green pin created successfully")
        self.balance=int(input("enter your balance:"))
        self.interface()
    def change_pin(self):
        user_pin=input("enter your green pin:")
        if user_pin == self.pin:
            new_pin=input("enter the new pin:")
            self.pin=new_pin
            print("your pin is changed successfully")
        else:
            print("your green pin is incorrect,please try again")
            self.interface()
    def check_balance(self):
        user_input=input("please enter your pin:")
        if user_input == self.pin:
            print("your balance is:",self.balance)
        else:
            print("incorrect pin,please check")
        self.interface()
    def withdraw(self):
        user_input=input("enter your pin:")
        if user_input == self.pin:
            amount=int(input("enter the value you want to withdraw:"))
            if amount <= self.balance:
                self.balance=self.balance-amount
                print("Available balance:",self.balance)
            else:
                print("insufficient balance,please check balance")
        else:
            print("your pin is incorrect,please check")
        self.interface()
    def deposit(self):
        user_input=input("enter your green pin:")
        if user_input == self.pin:
            amount=int(input("enter the amount you want to deposit:"))
            self.balance+=amount
            print("your available balance is:",self.balance)
        else:
            print("your pin is incorrect,please check")
        self.interface()
atm=Atm()
    
            
        
        

         