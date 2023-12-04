import math

c = float(input("Coupling factor: "))
z0 = 50

z0e = (4*c - 3 + math.sqrt(9-8*c*c))/(2*c*math.sqrt((1-c)/(1+c)))*z0
z0o = (4*c + 3 - math.sqrt(9-8*c*c))/(2*c*math.sqrt((1+c)/(1-c)))*z0

ze4 = ((z0o+z0e)/(3*z0o+z0e))*z0e
zo4 = ((z0o+z0e)/(3*z0e+z0o))*z0o

print(ze4)
print(zo4)
