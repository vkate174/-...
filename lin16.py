s= 2500
a=0
ost=0
if s % 500 ==0:
    print(str(s//500) + " - po 500")
 else:
     a = str(s//500)
     ost = s % 500
     a = (a + " - 500")
     print (a)
if ost%100 ==0:
    S = ost/100
    print(S)
 else:
     S = str(ost//100)
     ost = ost%100
     S = S + " - po 100")
     print (S)
if ost%10 ==0:
    print(str(ost/10) + " - po10")
  else:
      D = str(ost//10)
      ost = ost%10
      D = (D+ " - po10")
      print (D)
if ost%2 ==0:
    print(str(ost/2) + " - po2")
 else:
     DV = str(ost//2)
     print(DV + " - po2")
