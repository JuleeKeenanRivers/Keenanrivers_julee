import random 
xAndO = []
for i in range(0,4):
    xAndO.append([])
    for j in range(0,4):
        switch = random.randint(0,1)
        if switch == 1:
            xAndO[i].append("x")
        else:
            xAndO[i].append("o")
        
for values in xAndO:
    output = ""
    for value in values:
        output += value + "\t"
    print(output) 
  

