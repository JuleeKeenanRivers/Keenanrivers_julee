startnumber = int(input("Please enter a starting number:"))
sequencesize = int(input("Please enter a sequence size:"))

seq = len(str(sequencesize))

for i in range(0,seq):
    if i is 0 or 1:
        seq[i] = 0
    else:
        seq[i] = seq%20
print(seq)

