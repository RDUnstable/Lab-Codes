import math as m

f = float(input("Enter the frequency in GHz: "))
er = float(input("Enter the relative permitivitty: "))

c = 3e11

#This section is only valid for TE10 dominant mode

a = (c/2*f*1e9)
ad = a/(m.sqrt(er))

d = float(input("Enter the diameter if vias in mm: "))
p = float(input("Enter the distance between the vias in mm: "))

a_s = ad - (d*d/0.95*p)

print("Distance between the via rows: ", a_s)




