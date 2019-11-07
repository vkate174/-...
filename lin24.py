import random
a=random.randint(1,99)
print("a = " + str(a))
b=random.randint(1,99)
print ("b = " + str(b))
c=random.randint(1,99)
print ("c = " + str(c))
d=random.randint(1,99)
print("d = " + str(d))
if (a <= c and b <= d) or (a <= d and b <= c):
    print ("a rectangle with sides a,b can fit into a rectangle with sides s,d")
if not (a <= c and b <= d) or not (a <= d and b <= c):
    print("a recrangle with sides a,b can not fit into rectangle with sides c,d")
    
