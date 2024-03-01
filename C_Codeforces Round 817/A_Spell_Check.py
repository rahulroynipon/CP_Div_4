def decoder(n,x):
    y = 'Timru'
    if n!=5:
        return 'NO'
    
    arr = list(y)
    x = sorted(list(x))
    if x==arr:
        return 'YES'
    
    return 'NO'
 
 
 
 
 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = input()
        print(decoder(n,x))