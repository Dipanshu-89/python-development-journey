#for loop
# for char in range(5):
#     print(char,end=" ")
# var=int(input("enter your expected table: "))
# for i in range(1,11):
#     print(var,"X",i,"=",var*i)
# name="radhe Gupta"
# for i in name:
#     print(i)
# num=int(input("enter the number:"))
# rev=0
# while(num!=0):
#     r=num%10
#     rev=rev*10+r
#     num=num//10
# print("reverse number is",rev)
# num=input("enter a number:")
# reverse=''
# for digit in num:
#     reverse=digit+reverse
# print(reverse)
# num=int(input("enter your number:"))
# temp=num
# c=0
# while(temp>0):
#     r=temp%10
#     c+=1
#     temp=temp//10
# print(c)
# rev=0
# pow=num
# for i in range(c):
#     r=num%10
#     rev=rev+(r**3)
#     num=num//10
# if(pow==rev):
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")
# num=int(input("enter your number:"))
# temp=num
# c=0
# while(temp>0):
#     r=temp%10
#     c+=1
#     temp=temp//10
# print(c)
# rev=0
# pow=num
# for i in range(c):
#     r=num%10
#     rev=rev*10+r
#     num=num//10
# if(pow==rev):
#     print("Palindrome Number")
# else:
#     print("Not Palindrome Number")
# i=0
# while(i>=0):                            #infinite loop
#     print(i)
#     i+=1
# i=0
# while(True):
#     print("dipanshu")
#     i+=1
#     if(i==10):
#         break
#factorial number
# num=int(input("enter your number:"))
# fact=1
# while(num != 0):
#     # 5*4*3*2*1
#     fact=fact*num
#     num=num-1
# print(fact)
# find factorial using by for loop
# num=int(input("enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)
#function
# there are two types of functions
# 1.Built-in Function
# 2.User defined Functions
# types of arguments
# 1.default argument
# 2.keyword argument
# 3.required argument
# 4.variable-length argument
# def add(a,b):     #its a example of user defined function (default argument type)     
#     sum=a+b
#     return sum
# c=add(5,4)
# print(c)
# def gmean(a=1,b=2):     #keyword argument
#     mean=(a*b)/(a+b)
#     print(mean)
# gmean(b=3)
# def gmean(a,b=1):          #required argument
#     mean=(a*b)/(a+b)
#     print(mean)
# gmean(3)
# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#         avg=sum/len(numbers)
#     print(avg)
# average(10,10,10,10,10,10,10,10,10,10)
# global and local variable
# global variable create  outside the function
# local variable create inside the function and its access only inside function
# x=12
# print(x)
# def foo():
#     x=4
#     print("radhe")
#     print(f"the local variable x is {x}")
#     print(f"the global variable x is {x}")
# foo()
# print(x)
# x=12
# def fun():
#     y=2
#     print(y)
#     print(x)
# fun()
# # print(y)           this line raise error bcz y is defined in term of local variable and we do not access outside the function.
#how to change global variable
# x=23
# print(x)
# def rho():
#     y=45
#     global x
#     x=25
#     print(x)
#     print(y)
# rho()
# print(x)
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print("* "*i)
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print(" ")
# def fun(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n+fun(n-1)
# print(fun(int(input("enter a number:"))))
# def find_list(lst,idx=0):
#     if(idx==len(lst)):
#         return 
#     print(lst[idx])
#     find_list(lst,idx+1)
# f=['a','b','u','g']
# find_list(f)

            
        

    




