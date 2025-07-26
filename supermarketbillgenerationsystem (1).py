
from datetime import datetime
name = input("Enter Your Name:")
#items list
items_list = '''
1.rice           80/kg
2.oil            140/litre
3.sugar          60/kg
4.salt           40/kg
5.toothbrush     60rs
6.colgate        85rs
7.paneer         110/kg
8.moong dal      70/kg
9.poha           60/kg
10.soya chunks   50rs
11.teapowder     100rs
12.soaps         130rs/pack
'''
#declaration
price = 0
totalprice = 0
finalprice = 0
pricelist = []
ilist = []
qlist = []
plist = []
#items in dictionary
items = {
    "rice": 80,
    "oil": 140,
    "sugar": 60,
    "salt": 40,
    "toothbrush": 60,
    "colgate": 85,
    "paneer": 110,
    "moongdal": 70,
    "poha": 60,
    "soyachunks": 50,
    "teapowder": 100,
    "soaps": 130
}
#option for displaying items
option = int(input("Enter Option 1 for list of items:"))
print(items_list)
for i in range(len(items)):
    inp = int(input("Press 1 to Buy the items and 2 for exit:"))
    if inp == 2:
        break
    if inp == 1:
        item = input("enter the item:")
        quantity = int(input("enter the quantity:"))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item, quantity, price, items))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice * 5) / 100
            finalamount = totalprice + gst
        else:
            print("sorry you entered item is not available!")
    else:
        print("please enter the valid option!")

inp1 = input("Can i bill the items yes or no:")
if inp1.lower() == 'yes' and totalprice != 0:
    print("=" * 25, "V.A.R SuperMarket", "=" * 35)
    print(" " * 28, "korutla")
    print("Name:", name, " " * 30, "Datetime:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 75)
    print("{:<5} {:<15} {:<15} {:<10}".format("S.No", "Item", "Quantity", "price"))

    for i in range(len(pricelist)):
        print("{:<5} {:<15} {:<15} {:<10}".format(i + 1, ilist[i], qlist[i], plist[i]))

    print("-" * 75)
    print(" " * 50, 'Totalamount:', 'Rs', totalprice)
    print("gst", " " * 59, 'Rs', gst)
    print("-" * 75)
    print(" " * 50, "Finalamount:", 'Rs', finalamount)
    print("-" * 75)
    print(" " * 25, "Thanks for visiting", " " * 25)
    print("-" * 75)
elif totalprice==0 and inp1=='yes':
    print("No items for billing")
else:
    print("thank you visit Again!")