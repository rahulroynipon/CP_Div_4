def decoder(n,arrA,arrB):
    for i in range(n):
        if (arrA[i]=='R'and arrB[i]!='R') or (arrB[i]=='R'and arrA[i]!='R'):
            return 'NO'
    
    return 'YES'


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arrA = input()
        arrB = input()
        print(decoder(n,arrA,arrB))