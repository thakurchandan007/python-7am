# def test():
#     print("Hello")
#
# test()
# test()

# def myfunction():
#     """I am chandan thakur .I live in ktm.
#        I am learning python."""
#     return "hello"
# print(myfunction())
# print(myfunction.__doc__)
# __doc__-under score

# def test(a,b,c,d):
#     return a+b+c+d
# a=test(1,2,3,4)
# print(a)

# def introduction(name, age=0):
#     print(name, age)
#
#
#  introduction('ram')

# def test(*name, **age):
#     print(name)
#     print(age)
#
#
#
# test('ram', 'sita', b=20, a=35)

#ask for p,t,r and find si
# def takevalue():
#     p = int(input("Enter the principle:"))
#     t = int(input("Enter the Time:"))
#     r = int(input("Enter the Rate:"))
#
#     return [p, t, r]
#
#
# def calculate():
#     data = takevalue()
#     x = data[0]
#     y = data[1]
#     z = data[2]
#     return x * y * z / 100
#
#
# def display():
#     return calculate()
#
#
# print(display())

# def check():
#     username=input("Enter username:")
#     password=input("Enter password:")
#
#     if username =="admin" and password=="admin" or username=="hari" and password=="hari":
#         print("welcome")
#     else:
#         print("username and password is not correct.please try again!")
#
#
# check()

#ask username and password and check .

# def getinput():
#     username = input("Enter username:")
#     password = input("Enter password:")
#     return [username, password]
#
#
# def checklogin():
#     data = getinput()
#
#     if 'admin' == data[0] and 'admin002' == data[1] or 'jemes' == data[0] and 'jemes' == data[1]:
#         print(f"Welcome:{data[0]}")
#     else:
#         print("username&password not match")
#
#
# checklogin()
###################################################################################################################



# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
# def multiply(x, y):
#     return x * y
#
# # This function divides two numbers
# def divide(x, y):
#     return x / y
#
#
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
#
# while True:
#     # Take input from the user
#     choice = input("Enter choice(1/2/3/4): ")
#
#     # Check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#
#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#         break
#     else:
#         print("Invalid Input")
#######################################################################
# def Bazar():
#     print("1.Dell-RS.30000")
#     print("2.Mac-Rs.50000")
# def take_input():
#     dell = 30000
#     mac = 50000
#     total = 0
#     delivery_price = 0
#     bag = 0
#     plastic = 0
#     gift_box = 0
#     tax_amount = 0
#     choose=int(input("Enter the option(1/2):"))
#     if choose==1:
#         qty=int(input("Enter the Quantity:"))
#         total:qty*dell
#
#     if choose==2:
#         qty=int(input("Enter the Quantity:"))
#         total=qty*mac
#         print("******1.Home-(Rs.1000) 2.Pickup-(Free)******")
#         delivery_option = int(input("Choose a option:"))
#         if delivery_option == 1:
#             delivery_price = 1000
#
#         print("********1.Bag-(Rs.1000) 2.Plastic-(Rs.500) 3.Gift-Box-(Rs.5000)  4.None ********")
#         choose_option = int(input("Choose the option:"))
#         if choose_option == 1:
#             bag = 1000
#         if choose_option == 2:
#             plastic = 500
#         if choose_option == 3:
#             gift_box = 5000
#
#         print("********1.Kathmandu-(13%vat) 2.Lalitpur-(free) 3.Bhaktapur-(Free)********")
#         choose_location = int(input("Enter your option:"))
#         if choose_location == 1:
#             tax_amount = total * 13 / 100
#
#         Grand_total = total + tax_amount + plastic + bag + gift_box + delivery_price
#     def Bill():
#         print("**********Total-Bills**********")
#         print(f"Total:{total}")
#         print(f"Tax-Amount:{tax_amount}")
#         print(f"Delivery-Charge:{delivery_price}")
#         print(f"Grand-Total:{Grand_total}")
# def Grand_total():
#     print(Bazar())
#     print(take_input())
#
# Grand_total()
#######################################################################################################################
def function(x,y):
    a=x+y
    b=x-y
    return [a,b]
function(15,5)
function()


