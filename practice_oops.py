# class Student:
#     name="sarry"
#     classs=6
#     roll_no=8
#     # def __str__(self):
#     #     return f"name is {self.name} and roll no is {self.roll_no} from class {self.classs}"
#     # def __repr__(self):
#     #     return (f"name is {self.name} and roll no is {self.roll_no} from class {self.classs}")
# s1=Student()
# print(s1)
# class Student:
#     name="harry"
#     def __init__(self):
#         self.name="vikas"
# s=Student()
# print(s.name)
# class Business_man:
#     def __init__(self,name,role,stipend,work):
#         self.name=name
#         self.role=role
#         self.stipend=stipend
#         self.work=work
#     def show_details(self):
#         print(f"Name:{self.name}\nRole:{self.role}\nStipend:{self.stipend}\nWork: {self.work}")
# d=Business_man("dk",'software engineer',45000,"fresher")
# d1=Business_man("rakesh","data analyst",54000,"fresher")
# d.show_details()
# d1.show_details()
# class Hello:
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def greet():
#         print("Hello Sir/Madam")
# s1=Hello("Rajesh")
# s1.greet()
# print(s1.name)
# class Companies:
#     def __init__(self,name,role,salary,location,company):
#         self.name=name
#         self.role=role
#         self.salary=salary
#         self.location=location
#         self.company=company
# choice=input("enter your desired company:(only choose in google,microsoft,capgemini,jp morgan)")
# if(choice.lower()=='google'):
#     s1=Companies("dipanshu","software developer",45000,"delhi","google")
#     print("Name:",s1.name,"\nrole:",s1.role,"\nsalary:",s1.salary,"\nlocation:",s1.location,"\ncompany:",s1.company)
#     s2=Companies("dk","Network engineer",55000,"Mumbai","google")
#     print("Name:",s2.name,"\nrole:",s2.role,"\nsalary:",s2.salary,"\nlocation:",s2.location,"\ncompany:",s2.company)
# if(choice.lower()=='microsoft'):
#     s3=Companies("rakesh","Data analyst",45000,"gurugram","Microsoft")
#     print("Name:",s3.name,"\nrole:",s3.role,"\nsalary:",s3.salary,"\nlocation:",s3.location,"\ncompany:",s3.company)
#     s4=Companies("aman","cyber security expert",75000,"chennai","Microsoft")
#     print("Name:",s4.name,"\nrole:",s4.role,"\nsalary:",s4.salary,"\nlocation:",s4.location,"\ncompany:",s4.company)
# if(choice.lower()=='capgemini'):
#     s5=Companies("radhe","software developer",65000,"weat bengal","capgemini")
#     print("Name:",s5.name,"\nrole:",s5.role,"\nsalary:",s5.salary,"\nlocation:",s5.location,"\ncompany:",s5.company)
#     s6=Companies("ritik","Data science",35000,"delhi","capgemini")
#     print("Name:",s6.name,"\nrole:",s6.role,"\nsalary:",s6.salary,"\nlocation:",s6.location,"\ncompany:",s6.company)
# if(choice.lower()=='jp morgan'):
#     s7=Companies("abhinav","backend developer",105000,"banglore","jp morgan")
#     print("Name:",s7.name,"\nrole:",s7.role,"\nsalary:",s7.salary,"\nlocation:",s7.location,"\ncompany:",s7.company)
#     s8=Companies("chirag","frontend developer",250000,"hyderabad","jp morgan")
#     print("Name:",s8.name,"\nrole:",s8.role,"\nsalary:",s8.salary,"\nlocation:",s8.location,"\ncompany:",s8.company)
# class Toyota:
#     def __init__(self,milage,mode):
#         self.milage=milage
#         self.mode=mode
# class Fortuner(Toyota):
#     def __init__(self,brand,color,milage,mode):
#         self.brand=brand
#         self.color=color
#         super().__init__(milage,mode)
# c1=Fortuner("z5","black",85,"diesel")
# print(c1.milage,c1.mode)
# class Vector_2D:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def __str__(self):
#         return f"{self.i}i + {self.j}j"
# class Vector_3D(Vector_2D):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
# obj=Vector_2D(3,5)
# print(obj)
# obj1=Vector_3D(3,5,6)
# print(obj1)
# class Vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def __str__(self):
#         return f"{self.i}i+ {self.j}j+ {self.k}k"
#     def __add__(self,p):
#         x=self.i+p.i
#         y=self.j+p.j
#         z=self.k+p.k
#         return Vector(x,y,z)
# obj=Vector(3,4,7)
# obj1=Vector(5,6,7)
# print(f"{obj}\n{obj1}")
# print("sum:-",obj+obj1)







