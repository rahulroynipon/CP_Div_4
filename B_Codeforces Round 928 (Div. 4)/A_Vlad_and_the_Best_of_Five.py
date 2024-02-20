t = int(input())

for _ in range(t):
    x = input()
    ac= 0
    bc = 0
    for i in x:
        if i=='A':
            ac+=1
        else:
            bc+=1
    
    if bc>ac:
        print('B')
    else:
        print('A')