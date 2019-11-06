import random
a=random.randint (0,999)
print (a)
if a % 2 ==0:
    if a % 5 ==0:
        print("Число нечётное и кратно 5")
     else:
         print("Число нечётное")
else:
    print ("Число чётное")
    
