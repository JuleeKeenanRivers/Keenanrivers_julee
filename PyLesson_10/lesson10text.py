lettersList = []
lettersList.append(["a", "b", "c", "d"])
lettersList.append(["e", "f", "g", "h"])
lettersList.append(["i", "j", "k", "l"])
lettersList.append(["m", "n", "o", "p"])

print("here is a list with letters...")

for letters in lettersList:
    output = ""
    for letter in letters:
        output += letter + "\t"
    print(output)

    
    
print("\nHere is a list of words using split()")
wordsList = []

go = "father mother eagle house car office coffee make create life photo"
spList = go.split(" ")

spot = 0

for i in range(0,3):
    output = ""
    wordsList.append([])
    for j in range(0,4):
        wordsList[i].append(spList[spot])
        output += wordsList[i][j] + "\t\t"
        spot += 1
    print(output) 
