
def interest(R,P,N,T):
    return P*((1+(R/N))**(N*T))

n = float(input( " number of times loan is compounded per year: "))
r = float(input( " interest rate: "))
t = float(input( " life of the loan: "))
p = float(input( " principal: "))

print("Cost of loan is:", interest(r,p,n,t)/(t*12))


      


