def formatr(item, price):
    print("{:.<15} {:8.2f}".format(item, price))

item1 = input("please enter item1: ")
price1 = float(input("please enter the price: "))

item2 = input("please enter item2:")
price2 = float(input("please enter the price: "))

item3 = input("please enter item3:")
price3 = float(input("please enter the price: "))

item4 = input("please enter item4:")
price4 = float(input("please enter the price: "))

print("Subtotal: ..... ", (price1 + price2 + price3 + price4))
subtotal = (price1+price2+price3+price4) 

print("<<<<<<<Receipt>>>>>>")
formatr(item1, price1)
formatr(item2, price2)
formatr(item3, price3)
formatr(item4, price4)


discount = 0;

if subtotal>2000:
    discount = 0.15 * subtotal 

if subtotal<2000:
    discount = 0

#print("Discount: .....", discount)

formatr("Discount",discount)
    
#print("tax:.....", (subtotal*.0872))

tax = (subtotal*.0872)
formatr("tax",tax)

total = (subtotal - discount + tax)
#print("total:.....",total)

formatr("total",total)


print("*Thank you for your support*")



    

