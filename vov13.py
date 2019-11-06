import math
D=10
print("(D) Диаметр поперечного сечения = " + str(D))
A=4
print("(A) Квадратный брус = " + str(A))
d=A * math.sqrt( 5)
print("(d) Диагональ бруса = " str(d))
if D>= d:
    print(" Возможно выпилить")
 if D<d:
     print("Невозможно выпилить")
     
