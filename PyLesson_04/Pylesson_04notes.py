print("{:_<10}{:_<10}".format("test", "new test")) 

print("{:_>10} \t {:_>10}".format("test", "new test"))

print("{:_^10}{:_^10}".format("test", "new test")) 

print("{:*^10}{:*^10}".format("test", "new test"))

print("{:2.2f}\t{:2.5f}".format( 2.23, .00001 ))

 
def printf(word, number):
    print("{:<6}\t{:10.2f}".format(word, number))
  
word = "blah!"

number = 88888.99

printf(word, number)

word = "oh boy!"

number = 88777.99

printf(word, number)
