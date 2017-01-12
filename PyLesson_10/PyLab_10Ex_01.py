numslist = []

for i in range(0,4):
    numslist.append([])
    for j in range(0,4):
        i += numslist[i]

for nums in numslist:
    output = ""
    for num in nums:
        num += output + " "
    print(output) 
    
    
