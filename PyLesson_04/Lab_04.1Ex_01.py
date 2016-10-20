def formatr (item, price):
    print("{:>20} ........ {:8.2f}".format(item , price))
    
item1 = input("Please enter item1: ")
price1 = float(input("please enter the price: "))
               
item2 = input("please enter item2: ")
price2 = float(input("please enter the price: "))
               
item3 = input("Please enter item3: ")
price3 = float(input("please enter the price: "))

print("Subtotal: ......", (price1 + price2 + price3))
subtotal = (price1+price2+price3)

print("<<<<<<recepit>>>>>>")
formatr(item1, price1)
formatr(item2, price2)
formatr(item3, price3)
formatr("Subtotal:", subtotal)
               
print("tax:.....", (subtotal*.0872))
tax= (subtotal* .0972)

print("total:....", (subtotal+tax))
total= (subtotal+tax)

print("*Thank you for your support*")

