# x=20-INT
# y='Chandan'-STR
# z=12.5-FLOAT
# a = 1j-complex
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))
# first_name =input ("Enter your fname:")
# Last_name = input("Enter your lname:")
# print(first_name + "-" + Last_name)
# name="Ram Bahadur"
# print(f"my name is {name}")-format
# x = int(input("Enter the number:"))
# y = int(input("Enter the number:"))
# sum = x + y
# print("sum",sum)
# x=5
# y=10
# x=y
# print("x=",x)
# print("y=",y)
#list[-]-mutable(changeable)
# data=["ram","123","shyam","sita","laxmi"]
# data[2]="786"
# data[0]="Hari"
# print(data)

# Name=["Zyan","Amir","Sushant","pankaj","Manoj"]
# Name[0]="Salman"
# Name[3]="Sharukh-khan"
# print(Name[0:4])

# users=[
#     ["Ram","shyam","hari","krishna"],
#     ["sita","Gita","Rita","Lalita"],
#     ["zyan-malik","Arjit-singh","Sonu-Nigam","Vishak-Shekhar"]
#
#
# ]
# print(users[2][1])

# users=[
#           ["Ram","Ravan","Rohit"],
#     ["lAXMI","ANEY","GAYATRI"],
#     ["Madan","Hari","Pradip",[["Sopia"]]]
#        ]
# print(users[2][3][0][0])

# data={"Ram","Shyam","Hari","Ram"}
# print(data)

# users = [
#     {"Name": "Chandan Thakur", "Age": 19, "Address": "Dhobighat,lalitpur"},
#     {"Name": "Ram", "Age": 20, "Address": "Bhaktapur"},
#     {"Name": "Shyam", "Age": 22, "Address": [
#         {"loc": "BKT"}
#
#     ]}
# ]
# print(users[2]["Address"][0]["loc"])

#Conditional statement-If,elif,else:
# x=10
# y=15
# if x>y:
#     print("x is larger ")
# else:
#     print("y is larger")
# #
# x=10
# y=20
# z=30
#
# if x>y and x>z:
#     print("x is greater ")
#
# elif y>x and y>z:
#     print("y is greater ")
# else:
#     print("z is greater")

# x= 10
# y = 20
# z = 30
#
# if x > y and x > z:
#     print("x")
# elif y > x and y > z:
#     print("y")
# else:
#     print("z")

#nep,eng,math,sci,pop:
#total-100
#total%div,35to 45-pass \45to60-secand\60to75-first\75-100-top
#ask users for p,t,r
#si=p*t*r/100


#username&password check
#admin and admin002 or ram p=ram002

#ask users for passswords and id
# user = input("Enter your Id=")
# password = input("Enter your password=")
# if user == "admin" and password == "admin002":
#     print("Welcome to cyber world!")
# elif user == "ram" and password == "ram123":
#     print("welcome to cyber world!")
# else:
#     print("your Id and Password are in-correct")
########################################################################################################################
#ask user for interest,privipal,time and calculate simple interest.

# p=int(input("Enter the Principal="))
# t=int(input("Enter the Time="))
# r=int(input("Enter the Rate="))
# SI=p*t*r/100
# print(f"The Simple-Interest={SI}")
########################################################################################################################
#Show the result of students:
# print("*****Marks-sheet*****")
# a = int(input("Enter the English marks:"))
# if a>100:
#     print("Invalid!")
#     exit()
# b = int(input("Enter the Science marks:"))
# if  b>100:
#     print("Invalid!")
#     exit()
# c = int(input("Enter the Maths marks:"))
# if c>100:
#     print("Invalid!")
#     exit()
# d = int(input("Enter the Socila marks:"))
# if  d>100:
#     print("Invalid!")
#     exit()
# e = int(input("Enter the Nepali marks:"))
# if  e>100:
#     print("Invalid!")
#     exit()
# Grand_total = a + b + c + d + e
# total=Grand_total/5
# print(f"Total-marks:{Grand_total}")
# print(f"Percentage:{total}")
# if total >= 35 and total< 45:
#     print("*Div-Pass")
# elif total >= 45 and total< 60:
#     print("*Div-Second")
# elif total >= 60 and total< 75:
#     print("*Div-first")
# elif total >= 75 and total< 100:
#     print("*Div-Top")
# else:
#     print("*Div-Fail")
#######################################################################################################################
#-ASk customer for choose to buy computer:

# print("*********Cpmputer-Bazar*********")
# print("1.Dell-40000 and dis-10% with Vat-13%")
# print("2.HP-35000 and dis-15% with Vat-13%")
# print("3.Mac-60000 and dis-5% with Vat-13%")
# print("4.Asus-28000 and dis-20% with Vat-13%")
# print("a.Delivery in Ktm-1000")
# print("b.Personal-pickup-Free")
# Laptop=int(input(f"*Choose the laptop(1/2/3/4):"))
# Delivery=input(f"*Choose the Delivery(a/b):")
# if Laptop==1 and Delivery=="a" or Delivery=="b":
#     a=40000
#     b=int(input("*Enter the Quantity:"))
#     c=a*b
#     dis=c*10/100
#     vat=c*13/100
#     tot=c-dis+vat
#     print(f"total:{c}")
#     print(f"Discount-10%:{dis}")
#     print(f"Vat-13%:{vat}")
#     print(f"Grand-Total:{tot}")
#
# elif Laptop==2:
#         a = 35000
#         b = int(input("Enter the Quantity:"))
#         c = a * b
#         dis = c * 15 / 100
#         vat = c * 13 / 100
#         tot = c - dis + vat
#         print(f"total:{c}")
#         print(f"Discount-10%:{dis}")
#         print(f"Vat-13%:{vat}")
#         print(f"Grand-Total:{tot}")
#
# elif Laptop==3:
#         a = 60000
#         b = int(input("Enter the Quantity:"))
#         c = a * b
#         dis = c * 5 / 100
#         vat = c * 13 / 100
#         tot = c - dis + vat
#         print(f"total:{c}")
#         print(f"Discount-10%:{dis}")
#         print(f"Vat-13%:{vat}")
#         print(f"Grand-Total:{tot}")
#
# elif Laptop==4:
#         a = 28000
#         b = int(input("Enter the Quantity:"))
#         c = a * b
#         dis = c * 20 / 100
#         vat = c * 13 / 100
#         tot = c - dis + vat
#         print(f"total:{c}")
#         print(f"Discount-10%:{dis}")
#         print(f"Vat-13%:{vat}")
#         print(f"Grand-Total:{tot}")
# elif Laptop>4:
#     print("Invalid option!")
#
# print("Thank-You-For-Visit-on-our-website!!!")
########################################################################################################################
# Ncell-Talktime offers
# print("*******Ncell-Talk-Time-Offers*******\n")
# print("Voice_Call_Offers\n")
# print("1.5min@RS.5-Normal")
# print("2.25min@Rs.10-1Day")
# print("3.35min@Rs.15-2Days")
# print("4.45min@Rs.20-3Days")
# print("5.60min@Rs.25-5Days")
# a = int(input("*Choose the option:"))
#
# if a == 1:
#     print("Your 5minutes Talk-time has been succesfully activated and we deducted Rs.5 from your Mobile balance. ")
# elif a == 2:
#     print("Your 25minutes Talk-time has been succesfully activated and we deducted Rs.10 from your Mobile balance. ")
# elif a == 3:
#     print("Your 35minutes Talk-time has been succesfully activated and we deducted Rs.15 from your Mobile balance. ")
# elif a == 4:
#     print("Your 45minutes Talk-time has been succesfully activated and we deducted Rs.20 from your Mobile balance. ")
# elif a==5:
#     print("Your 60minutes Talk-time has been succesfully activated and we deducted Rs.25 from your Mobile balance. ")
# else:
#     print("Invalid!")
########################################################################################################################
#Bus-stop-27km- every stop at 5km one stop-Rs.15 / for child and old age -20% /whole trip-50:
# print("*******Bus-Fare-Kathmandu*******")
# print("1.First-stop-Kalanki")
# print("2.Second-Stop-soyambhu")
# print("3.Third-stop-chabel")
# print("4.Fourth-Stop-gaushala")
# print("5.Fifth-Stop-Airport")
# print("6.Last-Stop-Bus_Stand")
# print("*For old-man and Student-20%discount")
# a=int(input(f"Choose your Bus-stop:"))
# b=input("if,you are student or old-man press(Yes/No):")
# student=0
# old_man=0
# passenger=0
# Bus_fare=0
# dis_tot=0
# if a==1:
######################################################################

#LOOPS-[For,While,Nestede]-loops
# data=['Ram','sita','hari','rita',]
# for a in data:
#     if a=="Ram" and a=="sita":
#####################################################################

# data = [['Ram', 'Hari', 'Shyam', 'Mohan'],
# ['Sita', 'Gita', 'Rita', 'Lalita'],
# ['Zyan', 'Arjit', 'Anmol', 'Sohan']
# ]
# for b in data:
#     for user in b:
#         if user=='Arjit'or user=='Anmol':
#             print(user)

########################################################################
# data = ['ram', 'shyam']
# for a in data:
#         print(a)
##########################################################################
# x=0
# while x<10:
#     print(x)
#     x+=1
# Name should be printed:
#total =odd, even:
#no.of student:5times-marks input-Result:
############################################################
#Enter the name:
# i=0
# while i<5:
#     a=input("Enter the students-Name:")
#     i+=1
################################################
#Function:
# def test():
#     print("Hello")
#
#
# test()
# test()

#########################################
# def test():
#     return "Hello"
#
# print(test)

############################################
# def user(name,age):
#     print(name)
#     print(age)
#
# user('Ram',20)
# user('Sita',18)
# user('Hari',15)
############################################
# def add_sub(x,y):
#
#     add=x+y
#     sub=x-y
#     return [add,sub]
#
# a=add_sub(10,20)
# print(a[0])-add
# print(a[1])-sub

#############################################
# def addsub(x,y):
#     add=x+y
#     sub=0
#     if x>y:
#         sub=x-y
#     else:
#         sub=y-x
#     return [add,sub]
# a=addsub(10,20)
# print(a[0])
# print(a[1])
################################################
# def user(name,age=0):
#     print(name)
#     print(age)
#
# user()
#####################################################################
#p*t*r/100 by function:
# def take_input():
#     p = int(input("Enter the printcipal:"))
#     t = int(input("Enter the time:"))
#     r = int(input("Enter the Rate:"))
#     return [p, t, r]
#
#
# def calculate():
#     data = take_input()
#     p = data[0]
#     t = data[1]
#     r = data[2]
#     return p * t * r / 100
#
#
# def result():
#     return calculate()

########################################################################
# print(result())
#ask for p,t,r from user by using function:
# def takevalue():
#     p = int(input("Enter the p:"))
#     t = int(input("Enter the t:"))
#     r = int(input("Enter the r:"))
#     return [p, t, r]
#
##################################################################
# def calculate():
#     data = takevalue()
#     x = data[0]
#     y = data[1]
#     z = data[2]
#     return x * y * z / 100
#
#
# def display():
#     print(calculate())
#
# display()
###################################################################
#Ask user for data and time repeatation:
# def my_rep():
#     times=int(input ("Enter the time:"))
#     data=input("Enter the data:")
#     x=0
#     while x<times:
#         print(data)
#         x+=1
# my_rep()
####################################################################
#*arraay argument
#**keyword argument
#hw
# def dell():
# pass
# def toshiva():
# pass
# def mac():
# pass
#
# if__name__=='__main__':
#     dell()

#####################################################################
# def data():
#     x = 1
#     y = 2
#     return [x,y]
# print(data()[0])
# print(data()[1])
######################################################################
# x=0
# while x<11:
#     print(x)
#     x+=1
#####################################################################
# x = 10
#
#
# def test():
#     global x
#     print(x)##for same variables##
#     x = x + 3
#     print(x)
#
#
# test()
###########################################################################
#types of function
#inbuilt -function
#users- fuction
#function return value
# def test():
#     x=[1,2,3,4,5]
#     return x
# a=test()
# print(a[0:2])
###############################################################################
# def test():
#     def get():
#         return "hello"
#
#     return get()
# print(test())
###############################################################################
# def test():
#     def get():
#         return "hello get"
#
#     return get
#
# print(test()())
#############Ask number  for student  and print name :
# def get_name():
#     num_of_student = int(input("Enter the number of student:"))
#     student = []
#     x = 0
#     while x < num_of_student:
#         name = input("Enter Name:")
#         student.append(name)
#         x += 1
#
#     return student
#
#
# def display():
#     for name in get_name():
#         print(name)
#
#
# display()
#########################################################################################
#display resdult by function:
#while loops practice:
# x=int(input("Enter the no.:"))
# while x<=10:
#     if x==3:
#         x+=1
#         break
#     else:
#         print(x)
#     x+=1

# i = 0
# j = 5
#
# while i < 5:
#     while j >=0:
#             print(i, j)
#             i += 1
#             j -= 1

# def my_function():
#     a="hello"
#     b="hi"
#     return  [a,b]
#
# def clever():
#     c=my_function()
#     print(c[0])
#
# clever()


