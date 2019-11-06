import random
a=random.randint (0,999)
print(a)
if a % 2 ==0:
    if a % 10 ==0:
        print("Число чётное и кратно 10")
    else:
        print("Число чётное")
else:
    print("Число нечётное")
    
