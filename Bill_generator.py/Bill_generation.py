from datetime import datetime
name=input("Enter your name: ")
lists='''
Rice           Rs 20/kg
Sugar          Rs 30/kg
Salt           Rs 20/kg
Maggi          Rs 50/pac
Boost          Rs 100/pac
colgate        Rs 85/each
Dairymilk      Rs 10/each
kitkat         Rs 35/each
snickers       Rs 50/each
chocolate      Rs 350/each 
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
plist=[]
qlist=[]
# rates of items dec
items={'rice':20,
       'sugar':30,
       'salt':20,
       'maggi':50,'boost':100,'colgate':85,'dairymilk':10,'kitkat':35,'snickers':50,'dark chocolate':350}
option=int(input("for lists of items enter the option: "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
    if item in items.keys():
          price=quantity*(items[item])
          pricelist.append((item,quantity,items,price))
          totalprice+=price
          ilist.append(item)
          qlist.append(quantity)
          plist.append(price)
          gst=(totalprice*5)/100
          finalamount=gst+totalprice
    else:
         print("sorry you entered item is unavailable")
else:
     print("you entered wrong number")  
inp=input("can i bill the items yes or no:")
if inp=='yes':
     pass
if finalamount!=0:
     print(25*"=","V supermarket",25*"=")
     print(28*" ","khammam")
     print("Name:",name,30*" ","Date:",datetime.now())
     print(75*"=")
     print(f"{"sno":<5}{'items':<20}{'Quantity':<10}{'price':<10}")
     print(75*"=")
     for i in range(len(pricelist)):
          print(f"{i+1:<5}{ilist[i]:<20}{qlist[i]:<10}{plist[i]:<10}") 
print(75*"-")  
print(50*" ",'TotalAmount:','Rs',totalprice)  
print("gst amount",50*" " ,'Rs',gst)
print(75*"-")
print(50*" ",'final amount:','Rs',finalamount)
print(75*"-")
print(50*" ","Thanks for visiting")
print(75*"-")