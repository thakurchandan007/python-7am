#Wap a program to find the greatest of four numbers entered by the users.
# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# num3=int(input("Enter the third number:"))
# num4=int(input("Enter the fourth number:"))
# if num1>num4:
#     f1=num1
# else:
#     f1=num4
# if num2>num3:
#     f2=num2
# else:
#     f2=num3
#
# if f1>f2:
#     print(" greater:"+str(f1))
# else:
#     print(" greater:"+str(f2))

#"""WAp to find out whether a student is pass or fail it it requires a total of 40% for pass and at least  33% for pass.
# a=int(input("Enter fist-sub marks:"))
# if a>100 or a<0:
#     a=0
# b=int(input("Enter seccond-sub marks:"))
# if b>100 or b<0:
#     b=0
# c=int(input("Enter third-sub marks:"))
# if c>100 or c<0:
#     c=0
# per=(((a+b+c)/300)*100)
# print(f"Percentage%:{per}")
#
# if per<=38 and  per>=40:
#     print("You are pass")
# else:

#     print("Fail!")
# A = [
#     ['a','b','c'],
#     [1,2,3],
#     ['d','e','f']
#     ]
# for a in A:
#     for b in a:
#         if b=='a' or b==2 or b=='f':
#             print(b,end="-")
#             break
#find even or odd using for loop:
# num = int(input("Enter the number:"))
# for i in range(0, num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#WAP to list by while loop:
# veg=['Cabbage','Cauli-flower','Radish','Carrot']
# a=0
# while a<len(veg):
#     print(veg[a]+str(a),end="   ")
#     a+=1
#1.Write a program to print the multiplication table of a given number using for loop.
# num=int(input("Enter the multiplication Table no:"))
# for a in range(1,11):
#     print(f"{num}x{a}={num*a}")
#     print(str(num)+ "x" +str(a)+ "=" +str(a*num))

#2.Write a program to greet all the person names stored in a list l1 and which starts with S.
#l1 = [“Harry”, “Sohan”, “Sachin”, “Rahul”]
#name.startswith():
# a=['Rohan','Rohit','Laxman','Shyam']
# for name in a:
#     if name.startswith("S"):
#         print("HI   "+name)

#3.Attempt problem 1 using a while loop.
# num=int(input("Enter the Table :"))
# x=1
# while x<=10:
#     print(f"{num}x{x}={num*x}")
#     x+=1
#4.Write a program to find whether a given number is prime or not.
# num = int(input("Enter the number:"))
# prime = True
# for i in range(2, num):
#     if (num % i == 0):
#         prime = False
#         break
# if prime:
#         print("This is prime.")
# else:
#         print("This is not prime.")

#4.Write a program to find the sum of first n natural numbers using a while loop.
# num=int(input("Enter the number:"))
# while (num > 0):
#     sum += num
#     num -= 1
# print(f"The sum is{sum}")
# pass
#Write a program to calculate the factorial of a given number using for loop.
#factorial=5!=5*4*3*2*1
#factorila=n!=1*2*3*.....*n
# num = int(input("Enter the number:"))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print(f"The factorial of {num} is {factorial}")

#7.Write a program to print the following star pattern.
 #   *

#    ***

#***** for n=3

#8 Write a program to print the following star pattern:
# *
#
# **
#
# *** for n = 3

# n=3
# for i in range (3):
#     print(f"*"*(i+1))
#Fuction-Practice:
# def my_function():
#     print("Hello! fuction from me...")
#
# my_function()
##############################
# def name(First_name):
#     print(f"{First_name} Thakur")
#
# name('Hari')
# name('Radhe')
# name('Ram')
# name('shyam')
################################
# def name(First_name,Last_name):
#     print(First_name + Last_name)
#
# name('Ram','Parsad')
# name('Rohan','Bahadur')
# name('Salman','Khan')
##################################
# def my(*name):
#     print(f"my father is{name[2]}")
# my('Ram','Rohan','Vijay','Sohan')
###################################
# def world(a,b,c):
#     print(f"my son is {b}")
# world(a='Ram',b="Shyam",c="harry")
###################################????????????????????????
# def my_function(**kid):
#   print(f"His last name is {kid(lname)}")
#
# my_function(fname = "Tobias", lname = "Refsnes")
# ###############################################################
# def my_function(country = "Nepal"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("Norway")
# my_function("India")
# my_function("Brazil")
# my_function()
######################################################
# def my_function(food):
#     for a in food:
#         print(a)
#
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# #    or
# def my_food(*food):
#     for i in food:
#             print(i)

# my_food("MO:Mo","Burger","Pizza","KFC")
#############################################################################
# def my(name,age):
#     print(f"Hello!{name}")
#     print("How are you?")
#     print("-I am fine.")
#     print("how old are you?")
#     print(f"-I am {age}years old.")
#
# my("Rahu-Kumar",19)

# def add(num1,num2):
#     sum=num1+num2
#     print(f"The sum is:{sum}")
#     diff = num1 - num2
#     print(f"The diff is:{diff}")
#
# a=4
# b=1
# add(a,b)
#######################################################################################
# def add(n1,n2):
#     result=n1+n2
#     return result
#
# result=add(1,2)
# print(f"My sum is {result}")
#############################################################
# marks=[1,2,3,4,5]
# length=len(marks)
# print(f"length of marks is:{length}")
# marks_sum=sum(marks)
# print("total-marks:",marks_sum)
########################################################
#Function to find average  marks?
# def average_marks(marks):
#     sum_of_marks = sum(marks)
#     total_subject = len(marks)
#     average = sum_of_marks / total_subject
#     return average
#
#
# marks = [10, 20, 30, 40, 50]
# average = average_marks(marks)
# print("The average marks:", average)
########################################################
#Calculate the grade and return it
# def find_average_marks(marks):
#     sum_of_marks=sum(marks)
#     totao_subject=len(marks)
#     average_marks=sum_of_marks/totao_subject
#     return average_marks
# def computer_grade(average_marks):
#     if average_marks>=80:
#         Grade="A"
#     elif average_marks>=60:
#         Grade="B"
#     elif average_marks>=40:
#         Grade="C"
#     else:
#         Grade="D"
#         return Grade
# marks=[55,64,75,80,65]
# average_marks=find_average_marks(marks)
# print("Your average marks is:",average_marks)
#
# Grade=computer_grade(average_marks)
# print("Your grade is",Grade)
#################################################################
# import csv
#
# with open('data.csv', 'w', newline='')as files:
#     header = ['S.N', 'Name', 'Age', 'Address']
#     fs = csv.DictWriter(files, fieldnames=header)
#     fs.writerheader()
#     fs.writerow({"S.N": 1, "Name": "Chandan", "Age": 19, "Address": "ktm"})
#     fs.writerow({"S.N": 2, "Name": "ram", "Age": 18, "Address": "ktm"})
##########################################################################
#decorator
# def decor(result_fun):
#     def distinction(marks):
#         for m in marks:
#             if m>=75:
#                 print("Distinction")
#         result_fun(marks)
#     return distinction
#  @decor
# def result(marks):
#     for m in marks:
#         if m>=33:
#             pass
#         else:
#             print("Fail")
#             break
#     else:
#         print("PAss")
# result([50,60,54,40,35])
##############################################################33
# def sample_dec(fun):
#     def add_fun():
#         print("This is added to the actual function.")
#         fun()
#     return add_fun
# @sample_dec
# def actual_function():
#     print("This is actual function.")
#
#
# actual_function()
###################################################################
# def boys_name(*name):
#     def b_name():
#         name("Ram","Akshay","Hari","Krishna")
#     return b_name
#
#
# @boys_name
# def girl_name(*name):
#     print("The girl name are-", name)
#
#
# girl_name('Sita', 'Gita', 'Rita', 'Padma')
#################################################################
# def fun2(function):
#     def fun3():
#         print("Hello!")
#     function()
#     return fun3
# @fun2
# def fun1():
#     print("I am using python")
# fun1()
####################################################################
# data=lambda p,t,r:(p*t*r/100)#"""lambda =function"""
#
# print(f"Si={data(20,10,2)}")
#@property-funtion or method convert:
#############################################
# def ask(b):
#     print("hey!mr.")
#     def ask1():
#         print("What is your name?")
#     b()
#     return ask1
#
#
# @ask
# def name():
#     print("Hello!")
#
#
# name()
####################################################
# def res(marks):
#     def top():
#         for a in marks:
#             if a>=75:
#                 print("Distinction")
#     marks([80,90,50,85,98])
#     return top
#
# @res
# def result(marks):
#     for a in marks:
#         results = a / 5 * 100
#     if results >= 30:
#         print('PASS')
#     else:
#         print("FAIL")
#
#
# result([80, 90, 60, 75, 80])

def call(ph):
    print(f"My number:{ph}")
call(9841243778)
