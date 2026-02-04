print("welcome to our virtual python calci")
num_1=int(input("enter your first number:"))
num_2=int(input("enter your second number:"))
arithmetic_operation=input("enter your operation:")
addition=num_1+num_2
subtraction=num_1-num_2
multiplication=num_1*num_2
division=num_1//num_2
exponent=num_1**num_2
remainder=num_1%num_2
if(arithmetic_operation=='addition' or arithmetic_operation=="+"):
    print(addition)
if(arithmetic_operation=="subtraction" or arithmetic_operation=="-"):
    print(subtraction)
if(arithmetic_operation=="multiplication" or arithmetic_operation=="*"):
    print(multiplication)
if(arithmetic_operation=="division" or arithmetic_operation=="/"):
    print(division)
if(arithmetic_operation=="exponent" or arithmetic_operation=="**"):
    print(exponent)
if(arithmetic_operation=="remainder" or arithmetic_operation=="%"):
    print(remainder)