word1 = input("Please enter word 1:")
word2 = input("Please enter word 2:")
word3 = input("Please enter word 3:")

def makeCenter(word):
    if(len(word) >= 20):
        return word
    else:
        return makeCenter( " " + word + " ")

print(makeCenter(word1))
print(makeCenter(word2))
print(makeCenter(word3))


        
    
