values = []
values.append([1,2,3,4])
values.append([5,6,7,8])
values.append([9,10,11,12])
values.append([13,14,15,16])

#print(values) 
#print(values[2][3]) 


for i in range(0,len(values)): #outerloop: loops through list(columns)
    output = "" 
    for j in range(0, len(values[i])): #innerloop: loops through list at position i(rows)
        output += str(values[i][j]) + "\t"
    print(output, "\n")

    
        
for value in values:
    output = ""
    for num in value:
        output += str(num) + "\t"
    print(output) 
