# l=[2,3,4,5,8]
# print(l)
# print(type(l))
# l=[]
# l1=int(input("enter a number"))
# l.append(l1)
# l2=int(input("enter a number"))
# l.append(l2)
# l3=int(input("enter a number"))
# l.append(l3)
# l4=int(input("enter a number"))
# l.append(l4)
# print(l)
# by loop
# l=[]
# size=int(input("enter your size:"))
# for i in range(size):
#     l.append(int(input()))
# print(l)
# l=[1,'harmonic',6.7,True,False]
# print(l)
# l=[2,3,41,75,24,42,68,43]
# print(l[:])
# print(len(l))
# print(l[1:6:2])
# name="rajesh,rahul,rohit"
# l=[i for i in name]
# print(l)
# l=[i for i in range(5,51,5)]
# print(l)
# print(tuple(l))
# print(set(l))
# list methods
# l=[3,5,4,34,35,34,54,24]
# l.append(45)
# l.sort()
# l.sort(reverse=True)
# l.reverse()
# l.insert(1,100)
# if 34 in l:
#     print("yes")
# print(l.clear())
# print(l.count(34))
# l.remove(34)
# print(l)
# m=l.copy()
# m[0]="dipanshu"
# print(m)
# t=tuple(map(int,input("enter elements:").split()))
# print(t) 
# t=input("enter elements:").split(" ")
# print(tuple(t))
# n=int(input("enter the size:"))
# l=[]
# for i in range(n):
#     element=int(input(f"enter element {i+1}:"))
#     l.append(element)
# print(tuple(l))
# l=[]
# a=int(input("enter your first element:"))
# l.append(a)
# b=input("enter your second element:")
# l.append(b)
# c=input("enter your third element:")
# l.append(c)
# d=int(input("enter your fourth element:"))
# l.append(d)
# e=int(input("enter your last and final element of this tuple:"))
# l.append(e)
# print(tuple(l))
# tuple=(1,2,3,4,5,2,2,6)
# print(tuple.count(2))
# print(tuple)
# print(tuple.index(2))
# print(tuple.index(2,2,7))
# print(len(tuple))
# print(max(tuple))
# print(min(tuple))
# print(sum(tuple))
# print(6 in tuple)
# if 6 in tuple:
#     print("yes")
# letter="hey my name is {} i am from {}"
# name="dipanshu"
# state="uttar pradesh"
# print(letter.format(name,state))
# letter="hey my name is {0} i am from {1}"
# name="dipanshu"
# state="uttar pradesh"
# print(letter.format(name,state))
# letter="hey my name is {1} i am from {0}"
# name="dipanshu"
# state="uttar pradesh"
# print(letter.format(name,state))
# letter="hey my name is {} i am from {}"
# name="dipanshu"
# state="uttar pradesh"
# print(f"hey my name is {name} i am from {state}")
# def square(n):
#     '''we find a square of n and this is function & its return square of n'''
#     return n*n
# c=square(3)
# print(c)
# print(square.__doc__)
# def square(n):
#     return n*n
#     "we find a square of n and this is function & its return square of n"
# c=square(3)
# print(c)
# print(square.__doc__)
# def square(n):
#     "we find a square of n and this is function & its return square of n"
#     return n*n
# c=square(3)
# print(c)
# print(square.__doc__)
# import time
# hour=int(time.strftime('%H'))
# if(hour>=0 and hour<12):
#     print("Good Morning Python")
# elif(hour>=12 and hour<=17):
#     print("Good Afternoon Python")
# elif(hour>17 and hour<=21):
#     print("Good evening python")
# elif(hour>21 and hour<=24):
#     print("Good Night python")
# print("welcome to our virtual kbc")
# question=["who is the current prime minister of india?","what is the capital of punjab?"]
# option_1=["option A. yogi adityanath","option B. Arvind kejariwal","option c. jawharlal nehru","option d.narender modi"]
# option_2=["option A. Lucknow","option B. Chandigarh","option c. jalandhar","option d.Ludhiana"]
# enter_1=int(input("please enter 1 key for playing the kbc:"))
# print("first question is your computer screen:")
# if(enter_1==1):
#     print(question[0])
# options_1=int(input("please enter 1 key for options:"))
# if(options_1==1):
#     print(option_1[0])
#     print(option_1[1])
#     print(option_1[2])
#     print(option_1[3])
# answer=input("enter your option in term (like a,b,c..):")
# if(answer=="d" or answer=="D"):
#     print("congrats,you got 50 lakh")
# else:
#     print("sorry, please leave")
# proceed=input("please type yes if you give correct answer bcz you are user at that time:")
# if(proceed=="yes" or proceed=="Yes"):
#     print("Next question comes on your computer screen:")
#     a=int(input("please enter 1 key:"))
#     if(a==1):
#         print(question[1])
#         options_2=int(input("please enter 2 key:"))
#         if(options_2==2):
#             print(option_2[0])
#             print(option_2[1])
#             print(option_2[2])
#             print(option_2[3])
#             answer_1=input("enter your option in term (like A,B,C,a..):")
#             if(answer_1=="b" or answer_1=="B"):
#                 print("you won the kbc and your prize money is rs.1crore")
#             else:
#                 print("better luck next time")
# else:
#     print("well try,but your luck is not to you ")
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*factorial(n-1)
# print("the factorial is",factorial(8))
# def fibonacci_series(n):
#     if(n<0):
#         print("fibonacci series are not find of negative number")
#     elif(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibonacci_series(n-1)+fibonacci_series(n-2)
# term=int(input('enter terms:'))
# print("fibonacci series:")
# for i in range(term):
#     print(fibonacci_series(i),end=" ")




