# class Student:
#     name="dipanshu"
# s1=Student()
# print(s1.name)
# class Student:         #also we call using class function
#     name="dipanshu"
# s1=Student()
# print(Student.name)
# class Student:
#     def __init__(self,fname):
#         self.n=fname
# s=Student("avinash")
# print(s.n)
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def avg(self):
#         sum=0
#         for num in self.marks:
#             sum+=num
#         print("name:",self.name,",your avg score is:",sum/3)
# s1=Student("Aman",[99,84,96])
# s2=Student("Rakesh",[86,98,97])
# s3=Student("Dipanshu",[78,85,29])
# s1.avg()
# s2.avg()
# s3.avg()
# class Passenger:
#     def __init__(self,name,age,gender,address,identity,destination):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.address=address
#         self.identity=identity
#         self.destination=destination
#     @staticmethod
#     def hello():
#         str="welcome to our gupta's tour and travel"
#         print(str.center(60))
#     hello()
# p1=Passenger("raja",17,"male","shanti nagar,gurugram","aadhar card","mathura")
# p2=Passenger("krishna",22,"male","shakti park,gurugram","Pan card","lucknow")
# p3=Passenger("Neha",19,"female","Ganghi nagar,gurugram","Driving License","Noida")
# p4=Passenger("vineet",21,"male","vikas nagar,gurugram","pan card","kanpur")
# p5=Passenger("Rahul",22,"male","shivaji nagar,Gurugram","aadhar card","Varanasi")
# p6=Passenger("Abhinav",25,"male","shakti park,Gurugram","driving license","agra")
# p7=Passenger("nikhil",28,"male","om nagar,gurugram","Passport","Bihar border")
# p8=Passenger("riya",20,"female","raj nagar,gurugram","id card","ghaziabad")
# p9=Passenger("vikas",27,"male","kadipur,gurugram","aadhar card","Aligarh")
# p10=Passenger("vinay",26,"male","Amar colony,gurugram","Pan card","etah")
# choice=input("enter your passenger name:")
# if(choice.lower()=="raja"):
#     print("Name:",p1.name,"\nAge:",p1.age,"\nGender:",p1.gender,"\naddress:",p1.address,"\nidentity:",p1.identity,"\ndestination:",p1.destination)
# elif(choice.lower()=="krishna"):
#     print("Name:",p2.name,"\nAge:",p2.age,"\nGender:",p2.gender,"\naddress:",p2.address,"\nidentity:",p2.identity,"\ndestination:",p2.destination)
# elif(choice.lower()=="neha"):
#     print("Name:",p3.name,"\nAge:",p3.age,"\nGender:",p3.gender,"\naddress:",p3.address,"\nidentity:",p3.identity,"\ndestination:",p3.destination)
# elif(choice.lower()=="vineet"):
#     print("Name:",p4.name,"\nAge:",p4.age,"\nGender:",p4.gender,"\naddress:",p4.address,"\nidentity:",p4.identity,"\ndestination:",p4.destination)
# elif(choice.lower()=="rahul"):
#     print("Name:",p5.name,"\nAge:",p5.age,"\nGender:",p5.gender,"\naddress:",p5.address,"\nidentity:",p5.identity,"\ndestination:",p5.destination)
# elif(choice.lower()=="abhinav"):
#     print("Name:",p6.name,"\nAge:",p6.age,"\nGender:",p6.gender,"\naddress:",p6.address,"\nidentity:",p6.identity,"\ndestination:",p6.destination)
# elif(choice.lower()=="nikhil"):
#     print("Name:",p7.name,"\nAge:",p7.age,"\nGender:",p7.gender,"\naddress:",p7.address,"\nidentity:",p7.identity,"\ndestination:",p7.destination)
# elif(choice.lower()=="riya"):
#     print("Name:",p8.name,"\nAge:",p8.age,"\nGender:",p8.gender,"\naddress:",p8.address,"\nidentity:",p8.identity,"\ndestination:",p8.destination)
# elif(choice.lower()=="vikas"):
#     print("Name:",p9.name,"\nAge:",p9.age,"\nGender:",p9.gender,"\naddress:",p9.address,"\nidentity:",p9.identity,"\ndestination:",p9.destination)
# elif(choice.lower()=="vinay"):
#     print("Name:",p10.name,"\nAge:",p10.age,"\nGender:",p10.gender,"\naddress:",p10.address,"\nidentity:",p10.identity,"\ndestination:",p10.destination)
# else:
#     print("Invalid Input please run the program again.... ")
# class Personal_account:
#     name="dipanshu"
#     __password=123453
#     def prints(self):
#         print("password:",self.__password)
# s1=Personal_account()
# print(s1.name)
# s1.prints()
# class Car:
#     @staticmethod
#     def start(self):
#         print("car started")
#     @staticmethod
#     def stop(self):
#         print("car stoped")
# class toyota_car(Car):
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
# car1=toyota_car("fortuner","red")
# print(car1.start(1))
# class Car:
#     def __init__(self,type):
#         self.type=type
#     def start(self):
#         print("car started..")
#     def stop(self):
#         print("car stoped...")
# class Toyota_car(Car):
#     def __init__(self,brand,color,type):
#         self.brand=brand
#         self.color=color
#         super().__init__(type)
#         super().start()
# c1=Toyota_car("prius","blue","diesel")
# # print(c1.brand,c1.color)
# # print(c1.start())
# # print(c1.stop())
# print(c1.type)
# multiple inheritance
# class A:
#     varA="welcome to Class A"
# class B:
#     varB="welcome to class B"
# class C(A,B):
#     varC="welcome to class c "
# c1=B()
# print(c1.varA)
# class Calculator:
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     add=a+b
#     diff=a-b
#     mul=a*b
#     square=a**b
#     div=a/b
#     @staticmethod
#     def greet():
#         print("welcome to our python calci")
#     greet()
# a1=Calculator()
# choice=input("enter your opertion:")
# if(choice=="+" or choice=="addition" or choice=="add"):
#     print(a1.add)
# elif(choice=="-" or choice=="subtraction" or choice=="difference" or choice=="sub"):
#     print(a1.diff)
# elif(choice=="*" or choice=="multiplication" or choice=="mul" or choice=="product"):
#     print(a1.mul)
# elif(choice=="/" or choice=="division" or choice=="divide" ):
#     print(a1.div)
# elif(choice=="^" or choice=="square"):
#     print(a1.square)
# class Circle:
#     def __init__(self,r,pi):
#         self.r=r
#         self.pi=pi
#     def area(self):
#         a=self.pi*(self.r**2)
#         return a
#     def perimeter(self):
#         p=2*self.pi*self.r
#         return p
# c1=Circle(4,3.142)
# print(c1.area())
# print(c1.perimeter())
# class Complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
#     def show_number(self):
#         print(self.r,"i +",self.i,"j")
#     def __add__(c1,c2):
#         nr=c1.r+c2.r
#         ii=c1.i+c2.i
#         return Complex(nr,ii)
#     def __sub__(self,c2):
#         nr=self.r-c2.r
#         ni=self.i-c2.i
#         return Complex(nr,ni)
#     def mul(self,c2):
#         nr=self.r*c2.r
#         ni=self.i*c2.i
#         return Complex(nr,ni)
# c1=Complex(3,5)
# c1.show_number()
# c2=Complex(7,5)
# c2.show_number()
# na=c1+c2
# na.show_number()
# ns=c1-c2
# ns.show_number()
# nm=c1.mul(c2)
# print(nm.show_number())
# class Person:
#     def __init__(self,name,clv):
#         self.name=name
#         self.clv=clv
# class Student(Person):
#     def __init__(self,roll):
#         self.roll_no=roll
#         super().__init__("dipanshu",7)
# p1=Student(76)
# print(p1.name,p1.roll_no,p1.clv)
# def create_list(n):
#     l=[]
#     for i in range(n):
#         l.append(int(input("enter elements:")))
#     print(l)
# create_list(int(input("enter the size:")))
#decorator 
# class Student_marks:
#     def __init__(self,marks,grade):
#         self.marks=marks
#         self.grade=grade
#     @property
#     def fun(self):
#         return 10*self.marks
#     @fun.setter
#     def fun(self,val):
#         self.marks=val/10
# m1=Student_marks(40,"F")
# m1.fun=int(input("enter marks"))
# # print(m1.fun)
# print(m1.marks)
# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Good Morning")
#         fx(*args,**kwargs)
#         print("thank you")
#     return mfx
# @greet
# def hello():
#     print("hello world!")
# # @greet
# def add(a,b):
#     print(a+b)
# hello()
# greet(add)(3,4)          #also we do from @greet
# class Employee:
#     company_name="Google"
#     def __init__(self,name,employee_id):
#         self.name=name
#         self.id=employee_id
#     @classmethod
#     def change_company(cls):
#         cls.company_name="nestle"   
# s1=Employee("dk",78463)
# s1.change_company()
# print(Employee.company_name)
#class method as alternatives constructor
# class Person:
#     names="rakesh"
#     def __init__(self,name,classs):
#         self.name=name
#         self.classs=classs
#     @classmethod
#     def from_str(cls,str):
#         return cls(str.split("-")[0],str.split("-")[1])
# s1=Person("dipanshu",6)
# print("name:",s1.name,"\nclass:",s1.classs)
# s2=Person.from_str("dk-8")
# print("name:",s2.name,"\nclass:",s2.classs)
#same question without class method
# class Student:
#     def __init__(self,name,classs):
#         self.name=name
#         self.classs=classs
# s1=Student("dipanshu",6)
# print("name:",s1.name,"\nclass:",s1.classs)
# string="dk-8"
# s2=Student(string.split("-")[0],string.split("-")[1])
# print("name:",s2.name,"\nclass:",s2.classs)
# x=['a','b','c']
# print(dir(x))
# class Student:
#     def __init__(self,name,section):
#         self.name=name
#         self.section=section
# s1=Student("dipanshu",8)
# print(s1.__dict__)
# print(help())






    

 








