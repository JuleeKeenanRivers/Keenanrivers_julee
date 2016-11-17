need = int(input("please enter number of cookies you need:"))
batchSize = 25
batch = 1

for cookies in range(need, -1, -batchSize):
    print("cookies needed:", cookies)
    print("Batch #:", batch)
    batch = batch + 1

print("order up")
