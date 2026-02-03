# a=int(input("enter a number:"))
# b=int(input("enter a number"))
# print(a+b)
# try:
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     print("sum:",a+b)
# except Exception as e:
#     print(e)

# try:
#     n=int(input("enter a number"))
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")
# except:
#     print("invalid literal")
# finally:
#     print("I am always print")
# print("end of our program")
# real use of finally keyword
# def add(a,b):
#     try:
#         return a+b
#     finally:
#         print("i am always occured")
# c=add(4,6)
# print(c)
# try:
#     num=int(input("enter the number:"))
#     for i in range(num):
#         print(i)
# except ValueError:
#     print("sorry,its halted")
# n=input("please enter rohan:")
# if(n=="rohan"):
#     raise ValueError(print("I am dipanshu "))
# print(n)
# short_hand if-else
# num=int(input("enter a number:"))
# if(num>5):
#     print("num is greater than 5")
# else:
#     print("num is less than 5")
# we use short hand if else
# n=int(input("enter a num:"))
# print("number is greater than 0") if(n>0) else print("number is equal to zero") if(n==0) else print("Number is negative")
# n=int(input("enter a number:"))
# print("even") if(n % 2==0) else print("number is odd")
#enumerate
# l=[1,2,3,4,5]
# str="abhinav"
# for i in str:
    # print(i)
# marks=[100,98,95,76,87,95,99]
# i=0
# for char in marks:
#     print(char,i)
#     print("your marks are low in the class") if(i==3) else""
#     i+=1
# by using enumerate function
# marks=[14,65,45,34,31,21,71,99]
# for index,char in enumerate(marks):
#     print(index,char)
# we want to print index start from 1 then we do
# marks=[14,65,45,34,31,21,71,99]
# for index,char in enumerate(marks,1):
#     print(index,char)


