sentence = input("Please enter a sentence:")
space = " "

def Replace(sentence):
    if " " not in sentence:
        return sentence
    else:
        return sentence[0:sentence.index(" ")] + "_" + Replace(sentence[sentence.index(" ")+1:len(sentence)])

print(Replace(sentence))




