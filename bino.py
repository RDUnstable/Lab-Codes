import math

def fact(n):
    if n == 0:
        return 1;
    elif n == 1:
        return n;
    else:
        return n*fact(n-1)
    
def C(n,r):
    
    return (fact(n))/(fact(r)*fact(n-r))

z0 = int(input("Z0: "))
zl = int(input("Zl: "))
n = int(input("Order: "))
gm = float(input("Gamma m: "))

a = (pow(2,-n))*((zl-z0)/(zl+z0))

z = [z0,0,0,0,0,0]
i = 0
while i < n:
    
    z[i+1] = pow(math.e,(math.log(z[i]) + pow(2,-n)*C(n,i)*math.log(zl/z0)))
    i += 1
    
print(z)

          
     
    
