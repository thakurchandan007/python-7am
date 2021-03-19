dell=30000
mac=50000
hp=25000
total=0
delivery_price=0
bag=0
plastic=0
gift_box=0
tax_amount=0

print("************Computer-Bazar************")
print("1.Dell-(Rs.30000) 2.Mac-(Rs.50000) 3.Hp-(Rs.25000)")
ch=int(input("Enter Any Option:"))

if ch==1:
    qt=int(input("Enter the quantity:"))
    total=qt*dell

if ch==2:
    qt=int(input("Enter the quantity:"))
    total=qt*mac

if ch==3:
    qt=int(input("Enter the quantity:"))
    total=qt*hp

print("******1.Home-(Rs.1000) 2.Pickup-(Free)******")
delivery_option=int(input("Choose a option:"))
if delivery_option==1:
    delivery_price=1000

print("********1.Bag-(Rs.1000) 2.Plastic-(Rs.500) 3.Gift-Box-(Rs.5000)  4.None ********")
choose_option=int(input("Choose the option:"))
if choose_option==1:
    bag=1000
if choose_option==2:
    plastic=500
if choose_option==3:
    gift_box=5000

print("********1.Kathmandu-(13%vat) 2.Lalitpur-(free) 3.Bhaktapur-(Free)********")
choose_location=int(input("Enter your option:"))
if choose_location==1:
    tax_amount=total*13/100

Grand_total=total+tax_amount+plastic+bag+gift_box+delivery_price

print("**********Total-Bills**********")
print(f"Total:{total}")
print(f"Tax-Amount:{tax_amount}")
print(f"Delivery-Charge:{delivery_price}")
print(f"Grand-Total:{Grand_total}")
