import random
import math
X=random.randint(2.0,8.0)
if X <= 0:
    f=0
    print("f(" + str(X)+")=" + str (f))
if 0 < X < 1:
    f=X**2-X
    print ("f("+str(X)+")="+ str (f))
 else:
     f=X**2-math.sin(math.pi**2)
     print ("f(+str(X)+")="+str (f))
     
