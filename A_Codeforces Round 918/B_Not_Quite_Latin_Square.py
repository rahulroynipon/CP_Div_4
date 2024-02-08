t = int(input())
 
 
for _ in range(t):
    mydict = {
        'A': 0,
        'B': 0,
        'C': 0
    }
    for _ in range(3):
        x = input()
        for i in x:
            if i in mydict:
                mydict[i] += 1
 
    for key, value in mydict.items():
        if value==2:
            print(key)
            break