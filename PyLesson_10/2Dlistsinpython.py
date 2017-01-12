print("using range...") 
for i in range(0, len(values[i])):
    output = ""
    for j in range(0, len(values[i])):
        output += str(values[i][j]) + "\t"
    print(output + "\n")
    
print("using enhanced loop...")
for value in values:
    output = ""
    for num in value:
        output += str(num) + "\t"
    print(output + "\n") 
