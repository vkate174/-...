import random
A = [ random.randint (0,1000) for _ in range(20)]
print A
for i in range (0, len(A), -1):
    for k in range(len(A) - 1):
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                x = A[i]
                A[i] = A[i+1]
                A[i+1] = x

print A
