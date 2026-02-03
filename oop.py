# class Person:
#     name="dipanshu"
#     course="btech"
# p=Person()
# p.name='rk'
# print(p.name)
# class Person:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
#         print("name:",self.name,"gender:",self.gender)
# def greet(object):
#     print("hi",object.name,"you are",object.gender)
# obj=Person('dk','male')
# obj.name='rk'
# obj2=obj
# print(obj2.name)
# greet(obj)
# aggregation- one class has a relation
# class Customer:
#     def __init__(self,name,gender,address):
#         self.name=name
#         self.gender=gender
#         self.address=address
#     def customer_address(self):
#         print(self.address.landmark,self.address.city,self.address.pincode)
# class Address:
#     def __init__(self,landmark,city,pincode):
#         self.landmark=landmark
#         self.city=city
#         self.pincode=pincode
# a=Address('gandhi nagar','gurgaon',122001)
# c=Customer('dipanshu','male',a)
# c.customer_address()
class User:
    def __init__(self):
        self.name='dipanshu'
        print("welcome to our websites")
    def login():
        print("please login")
    def register(self):
        print("registered")
class Student (User):
    def __init__(self):
        super().register()
        super().__init__()
        print("i am student constructor")
    def enroll(self):
        print('you are enrolled in our batch')
obj=Student()
