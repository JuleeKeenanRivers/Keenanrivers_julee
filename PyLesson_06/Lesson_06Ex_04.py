num = int(input("Please enter an integer:"))
size = int(input("Please enter the size of the table:"))

for i in range(1, size):
    print("{:10} | {:10}".format(i, i*num))



