import random
import math
a = random.randint(1,10)
Kyb=A**3
print("V Kyb = " + str(Kyb))
H=random.randint(1,10)
R=random.randint(1,10)
pi=math.pi
cylinder=pi*R**2*H
print("V cylinder = " + str(cylinder))
M=random.randint(1,100)
print("V voda = " + str(M))
if Kyb >= M:
    print ("voda наполнит Kyb,")
 elif Kyb < M:
     print("voda не наполнит Kyb,")

if cylinder >= M:
    print(" voda наполнит cylinder,")
 elif cylinder < M:
     print("voda не наполнит cylinder,")

if Kyb >=M:
    if cylinder >=M:
        print("voda наполнит и Kyb и cylinder.")
elif cylinder < M:
    if Kyb < M:
        print("voda не наполнит Kyb и cylinder.")
        
