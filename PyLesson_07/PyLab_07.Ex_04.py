sentence = input("Please enter a sentence:")

def Replace(sen):
    while sen.count("a") > 0:
        sen = sen[0 : sen.index("a")] + "@" + sen[sen.index("a")+1 : len(sen)]
    return sen

print(Replace(sentence))

        
    
        






