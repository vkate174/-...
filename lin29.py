import random
a=random.randint(5,2019)
print("year: ' + str(a))
      if a % 4 == 0:
      print(str(a) + " year a leap")
    elif not a % 4 == 0:
        print(str(a) + "year a not leap")
V = a//100 + 1
print(str(a) + "year, " + str(V) + "century")
