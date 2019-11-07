import random
x=random.randint(-100,100)
print("x = " + str(x))
a=random.randint(-100,100)
b=random.randint(-100,100)
if b>a:
    print("[a,b]= " + "[" + str(a) + "," + str(b) + "]")
  if a<= x and x<= b:
      print("число принадлежит данному промежутку")
    elif a> x or x > b:
        print("число не принадлежит данному промежутку")
elif a>b:
    print("error")
    
