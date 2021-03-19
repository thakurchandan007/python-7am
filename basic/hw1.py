print("********computer-Market*********")
print("1.Dell-NRS20000")
print("2.Hp-NRS30000")
print("3.Mac-NRS80000")
print("4.Acer-NRS15000")
print("For home delivery -NRS1000/For out of KTM valley  delivery -NRS2500")
print("self pickup -free\n")

print("********GREAT-OFFER************")
print("40% off on Dell")
print("35% off on Hp")
print("20% off on Mac")
print("50% off on Acer")

print("-13% vat tax will be added\n")

print(".....FOR-Dell.....")

x = int(input('Enter the Quantity number:'))
dell = 20000

total = x * dell
a = total - total * 40 / 100 + total * 13 / 100
print(f"Grand-Total={a}\n")


print(".....FOR-HP.....")
y = int(input('Enter the Quantity number:'))
hp = 30000

total = x * hp
b = total - total * 35 / 100 + total * 13 / 100
print(f"Grand-Total={b}\n")


print(".....FOR-Mac.....")
z = int(input('Enter the Quantity  number:'))
mac = 80000

total = z * mac
c = total - total * 20 / 100 + total * 13 / 100
print(f"Grand-Total={c}\n")


print(".....FOR-Acer.....")
r = int(input('Enter the Quantity number:'))
acer = 15000

total = r * acer
d = total - total * 50 / 100 + total * 13 / 100
print(f"Grand-Tota={d}\n")


print("Thank you !!!")