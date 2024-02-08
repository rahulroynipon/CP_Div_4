from math import sqrt
 
t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int,input().split()))
 
    total = sum(x)
 
    print('YES' if sqrt(total)==int(sqrt(total)) else 'NO')