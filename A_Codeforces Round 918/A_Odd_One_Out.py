t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
 
    x = arr[0]
    if arr.count(x)==1:
        print(x)
    else:
        arr.remove(x)
        arr.remove(x)
        print(arr[0])