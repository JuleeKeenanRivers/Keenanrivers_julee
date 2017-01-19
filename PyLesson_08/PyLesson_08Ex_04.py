word = input("please enter a word:")
stop = len(word)
start = 0

def tree(word,start,stop):
    if (start <= stop): 
        print("{:>10}".format(word[0:start])) 
        return tree( word, start + 1, stop )

tree(word,start,stop)





