'''
print("hello python")
input1=input("enter your input:")
print(input1)'''
#calculator
# print("welcome to my calculator")
# input1=int(input("enter the value1:"))
# input2=int(input("enter the value2:"))
# add=input1+input2
# sub=input1-input2
# mul=input1*input2
# div=input1/input2
# opr=input("enter your operation:(or +,-,*,/):")
# if(opr=="add" or opr=="+"):
#     print("your output: ",add)
# elif(opr=="sub" or opr=="-"):
#     print("your result: ",sub)
# elif(opr=="mul" or opr=="*"):
#     print("your output: ",mul)
# elif(opr=="div" or opr=="/"):
#     print("your output: ",div)
# n=int(input("enter the number:"))
# for i in range(n):
#     print(i+1)
#     print(type(i))
# import math
# a=5;
# b=6;
# print(math.ceil(a/b))
#data types in python
#Integer
# print(45)
# #float/decimal
# print(3.422)
# #boolean
# print(True)
# #text/string
# print("python is not a snake its programming language")
# #max integer
# print(1e308)   # same for float
# #complex
# print(3+4j)
# #list
# print([3,2,5,9,2])
# #tuple
# print((32,53,2,42,53))
# #dictionary
# print({"name":"dipanshu","age":19,"course":"btech"})
# #set
# print({3,5,3,4,6,2})
# print(type([2,2,53,24,25]))
# input=input("enter your name:")
# print(input)  # literals are just variables value
# a=0b1010
# b=0b1011
# print(a+b)
# a=0o1456       #octal representation
# print(a)
# f=3.2e5             #3.2*10^5
# print(f)
# string="""this is multiline string"""
# print(string)
# _=5             it's also a way of declare a variable and store value
# print(_)
# print('d' in "delhi")
# print(1 not in [3,2,5,6,6])
# a=int(input("enter a number"))
# f=a//100
# l=a%10
# m=(a%100)//10
# sum=f+l+m
# print(sum)
#subtraction without using sub operator
# number=int(input("enter a first number:"))
# number2=int(input("enter a second number:"))
# sub=number+(~number2+1)
# print(sub)
# first_number=int(input("enter the first number:"))
# second_number=int(input("enter the second number:"))
# third_number=int(input("enter the third number:"))
# if first_number < second_number:
#     if first_number < third_number:
#         print("first number is smaller than both")
#     else:
#         print("third number is smaller than both")
# else:
#     if(second_number < third_number):
#         print("second number is smaller than both")
#     else:
#         print("third number is smaller than both")
# import math 
# print(math.floor(6.743))
# print(math.ceil(6.242))
# print(math.factorial(4))
# print(math.cos(0))
# help("modules")
# import keyword
# print(keyword.kwlist)
# import datetime
# print(datetime.datetime.now())
# import random
# print(random.randint(1,5))
# import random
# computer=random.randint(1,100)
# print("welcome to our guessing game")
# score=0
# while True:
#     user=int(input("enter your guess:"))
#     if(user==computer):
#         print("you won",computer)
#         score+=1
#         break
#     elif(user > computer):
#         print("guess is higher, think lower")
#         score+=1
#     else:
#         print("guess is lower,think higher")
#         score+=1
# print("your score is:",score)
# total_population=10000
# for i in range(1,11 ,1):
#     total_population=total_population+(total_population*(10/100))
#     print(i,"year",total_population)
#sequence sum
# number=int(input("enter the value where you want to stop series:"))
# fact=1
# seq_sum=0
# for i in range(1,number+1):
#     fact*=i
#     seq_sum=seq_sum+(i/fact)
#     print(i,"series ",seq_sum)
# for i in range(1,4):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# rows=int(input("enter a number:"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for k in range(i-1,0,-1):
#         print(k,end=)
#     print()
# for i in range(1,101):
#     for j in range(2,4):
#         if i % j == 0:
#             break
#     else:
#         print(i)
# for i in range(1,10):
#     if i==4:
#         continue
#     print(i)
# print(len("hello world"))
# print("hello" and "world")
# print("D"   in "delhi")
# a="hello world"
# print(len(a))
# print(max(a))
# print(min(a))
# print(sorted(a))
# print(sorted(a,reverse=True))
# email=input("enter your email")
# a=email.find("@")
# print("username:",email[:a])
# str="hello how are you he"
# print(str.count('how'))
# str=input("enter the string:")
# count=0
# find=input("enter word do you want to find:")
# for i in str:
#     if find==i:
#         count+=1
# print(count)
# string =input("enter your string:")
# remove=input("enter element:")
# new_string=''
# for i in string:
#     if i==remove:
#         pass
#     else:
#         new_string+=i
# print(new_string)
# n=input("enter the string:")
# s=n[::-1]
# if(s==n):
#     print("palindrome string")
# else:
#     print("not palindrome")
# s=input("enter the string:")
# length=len(s)
# rev=''
# for i in range(length-1,-1,-1):
#     rev=rev+s[i]
# if rev==s:
#     print("palindrone string")
# else:
#     print("not palindrone")
# s=input('enter the string:')    # fail where there is one or more spaces
# c=1
# for i in s:
#     if i == ' ':
#         c+=1
# print(c)
# s=input("enter the string:")
# l=[]
# str=''
# for i in s:
#     if i != ' ':
#         str=str+i
#     else:
#         l.append(str)
#         str=''
# l.append(str)
# print(len(l))
# s=int(input("enter the value:"))
# digit='0123456789'
# result=''
# while s != 0:
#     result=digit[s%10]+result
#     s=s//10
# print(result)
# l=[4,2,2,5,6]
# print(id(2))
# print(l)
# l.append(6)
# print(l)
# print(id(l[3]))
# l=[1,3,5,3,4,2,6]
# l1=[[1,3],[4,6]]
# print(l1[1][0])   #indexing
# print(l[3:6])   #slicing
# list methods to add
# list=[5,2,8,3,9]
# print(list.append(5))       # its return none
# print(list)
# l=[1,6,3,7,8]
# l.extend(['rk','ek','pi'])
# print(l)
l=[2,'rk',5,8,9]
# l.insert(1,'dipanshu')
# print(l)
# del l[0]
# l.remove('rk')
# l.pop()
# l.pop(2)
# l.clear()
# print(l)
# l=[1,3,2]
# print(l*(3+3))
# l1=[1,2,3,[4,5]]
# print([4] in l1)
# l=[]
# for i in range(6):
#     n=int(input("enter element:"))
#     l.append(n)
# print(l)
# l=[3,4,5,6]
# list=[i*i for i in l]
# print(list)
# list=['python','javascript','php','java','typescript']
# item=[i for i in list if i[0]=='p']
# print(item)
# tup=()
# l=[]
# for i in range(0,5):
#     n=int(input("enter elements:"))
#     l.append(n)
# tup=tuple(l)
# print(tup)
# t=(2,)
# print(t)
# set1=set()
# set1.add(5)
# set1.update((4,5,6))
# print(set1)
# s={4,5,6,9,1}
# del s
# s.discard(4)   # quality if elements does not found it's not give an error
# s.remove(5)      # it's throws an error when there is no value found in set
# s.pop()
# print(s)
# s1={1,3,5,6}
# s2={5,6,3,2}
# print(s1.intersection(s2))
# print(s1.union(s2))
# fs=frozenset([1,2,4])
# fs1=frozenset({4,2,7,3})
# print(fs | fs1)
# s=frozenset({1,2,3,frozenset((4,5,2))})    # 2-D set possible
# print(s)
# dict={
#     'name' : "dipanshu",
#     'class' : 12,
#     'rollno': 23,
#     'gender': 'male'
# }
# print(dict.keys())
# dict={i:i**2 for i in range(1,11)}
# print(dict)
# function
# def even_number(n):
#     """
#     this is docstring and this function returns number is even or odd
#     """
#     if type(n)== int:
#         if n % 2 == 0:
#             return "even"
#         else: 
#             return "odd"
#     else:
#         return "sorry your input is invalid please check!"
# print(even_number('hello'))
# def power(a=1,b=1):
#     return a**b
# print(power(b=3))
# def addition(*args):  args allow to pass non-keyword variable to the function
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(addition(1,3,4,5))
# def foo(**kwargs):
#     for i,j in kwargs.items():
#         print(i,'=',j)
# foo(india='delhi',japan='tokyo',usa='washington',nepal='kathmandu')
# a=lambda x:x**2
# print(a(2))
# y=lambda a:input("enter the char:") in a
# print(y("dipanshu"))
# a=5
# print("even" if a % 2 == 0 else "odd")
# fun=lambda z: 'even' if z % 2 == 0 else 'odd'
# print(fun(7))
# def cube(n):
#     return n**3
# def higher_order_function(fun,list):
#     output_list=[]
#     for i in list:
#         output_list.append(fun(i))
#     print(output_list)
# l=[1,2,3,5]
# higher_order_function(cube,l)
#use of lambda function
# def higher_order_function(fun,list):
#     output_list=[]
#     for i in list:
#         output_list.append(fun(i))
#     print(output_list)
# l=[1,2,3,5]
# higher_order_function(lambda x:x**3,l)
#map function
# t=(91,3,43,64,35,24,63,8)
# print(list(map(lambda x:'even' if x % 2 == 0 else 'odd',t )))
# l=[91,3,43,64,35,24,63,8]
# print(set(map(lambda x:'even' if x % 2 == 0 else 'odd',l )))
# print(list(filter(lambda a:a>4,(3,5,2,5,1,4,7,5))))
# print(list(filter(lambda a:a>4,(3,5,2,5,1,4,7,5))))
# import functools
# print(functools.reduce(lambda a,b:a+b,[1,2,3,4,5]))
# print(functools.reduce(lambda x,y:x if x<y else y,[1,2,3,4,5]))