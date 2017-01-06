startnumber = int(input("Please enter a starting number:"))
sequencesize = int(input("Please enter a sequence size:"))

seq = [0] * sequencesize

for i in range(0,len(seq)):
    if i == 0 or i == 1:
        seq[i] = startnumber
    else:
        seq[i] = seq[i-2] + seq[i-1]
print(seq)


