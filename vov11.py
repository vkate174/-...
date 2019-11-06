A=5
B=6
C=7
M=35
K=20
if (A<M and B<K) or (A<K and B<M):
    print("Проходит в дверь")
elif (B<M and C<K) or (B<K and C<M):
    print("Проходит в дверь")
 elif (A<M and C<K) or (A<K and C<M):
     print("Проходит в дверь")
else:
    print("Не проходит в дверь")
    
