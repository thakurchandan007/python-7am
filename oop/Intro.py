# class Introduction:
#     def __init__(self,p,t,r):
#         self.data=[p,t,r]
#
#     def calculate(self):
#         x=self.data[0]
#         y= self.data[1]
#         z = self.data[2]
#         return x*y*z/100
#     def display(self):
#         return self.calculate()
#
# obj=Introduction(10,10,10)
# print(obj.calculate())
#####################################################
# class Introduction:
#     def __init__(self,p,t,r):
#         self.data=[p,t,r]
#
#     def calculate(self):
#         x=self.data[0]
#         y= self.data[1]
#         z = self.data[2]
#         return x*y*z/100
#     def display(self):
#         return self.calculate()
# a=int(input("Enter the p:"))
# b=int(input("Enter the t:"))
# c=int(input("Enter the r:"))
# obj=Introduction(a,b,c)
# print(obj.calculate())
##########################################################
# class Introduction:
#     def __init__(self):
#         p = int(input("Enter the a:"))
#         t = int(input("Enter the b:"))
#         r = int(input("Enter the c:"))
#         self.data=[p,t,r]
#
#     def calculate(self):
#         x=self.data[0]
#         y= self.data[1]
#         z = self.data[2]
#         return x*y*z/100
#     def display(self):
#         return self.calculate()
#
# obj=Introduction()
# print(obj.calculate())
##################################################################
# class  Introduction:
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return "I am OOP"
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls)
#
# Introduction()
# print("Name")
#cd op -for open new files.
####################################################
# class mobile:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     x=10
#
#     def get_brand(self):
#         return f"Brand Name:{self.brand}"
#     def get_price(self):
#         return f"Price-Rs.:{self.price}"
#
# class Mi(mobile):
#     def __init__(self,brand,price,company):
#         super().__init__(brand,price)
#         self.cmp=company
#     def get_company(self):
#         return f"Company Name:{self.cmp}"
# obj=Mi("Apple",1000,'America(calfornia).co.ltd.')
#
# print(obj.get_company())
# print(obj.get_brand())
# print(obj.get_price())
########################################################################################################
# learn pattern design.
# class Example:
#     --name=''
#
#     def __init__(self):
#         pass
#     @property
#     def get_name(self):
#         return self.__name
#
#     @get_name.setter
#     def get_name(self,b):
#         self.__name=b
# obj=Example()
# obj.get_name='sita'
################################################################################################################
# class myself:
#     pass
# chandan=myself()
# chandan.name="aditya thakur"
# chandan.relation="Brother"
# names=myself()
# names.name="Chandan Thakur"
# names.STD='BCA'
# names.sec='A'
# names.college='Delhi College University(D.U)'
# print("'----my-detail----'")
# print(f"MY name is:{names.name}")
# print(f"I am studying:{names.STD}")
# print(f"My section is:{names.sec}")
# print(f"My college name is:{names.college}")
# print(f"my name is {names.name}\nmy college is {names.college}\nI study in {names.STD}")
# print(f"My brother name is {chandan.name}\nHe is my {chandan.relation}")
################################################################################################################
# class myself:
#     school="D.A.V"
#     pass
# stdudent=myself()
# Boys=myself()
# stdudent.name="Chandan thakur"
# Boys.name="Ram Charan"
# stdudent.age=19
# Boys.age=30
# print(f"Student name :{stdudent.name}\nStudent School:{myself.school}\n")
# print(f"boys name:{Boys.name}\nboys school:{Boys.school}")
############################################################################################################
class student:
    def student_detail(self):
        return (f"Student name-{self}\nstudent Class-{self}/nstudent sec-{self}/nstudent college-{self}")
std_name=student
std_name.name="Chandan Thakur"
std_name.Class=+2
std_name.sec='A'
std_name.College='DAV'
college=student
college.name="Aditya Thakur"
college.Class=+2
college.sec='B'
college.College='ST.Xaviers'
print(std_name.name)
