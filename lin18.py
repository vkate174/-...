import random
import math
A= random.randint (1,5)
V = A**3
print ("Kyb capacity",V)
p= math.pi
H = random.randint (1,5)
R= random.randint (1,3)
W = (P*R**2)*H
print ("cylinder capacity", W)
vg = random.randint (1,50)
print ("volume of fluid",vg)
if vg > V:
    print ("can fill cube")
  else:
      print("can not fill cube")
if vg > W:
    print ("can fill celinder")
  else:
      print("can not fill celinder")
if vg > V+W :
    print("can fill both")
  else:
      print ("can not fill both")
