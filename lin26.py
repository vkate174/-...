import random
A=random.randint(-4,4)
print("A=" + str(A))
x=A
if x <= 0:
    print("x <= 0")
    f=0
    print("f(A)=" + str(f))
  elif 0 < x and x < 1:
      print(" 0 < x < 1")
      f=x
      print("f(A)=" + str(f))
  elif not x <= 0 or not (0 < x and x < 1):
      print("other case")
      f=x**4
      print("f(A)=" + str(f))
      
