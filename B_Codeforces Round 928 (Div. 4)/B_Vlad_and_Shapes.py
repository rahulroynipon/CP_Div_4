def decoder(n,arr):
    for i in range(n):
        countOne = arr[i].count(1)
        if countOne!=0:
            countTwo = arr[i+1].count(1)
            if countOne==countTwo:
                return 'SQUARE'
            return 'TRIANGLE'
                
                



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for _ in range(n):
            x = input()
            x = list(map(int,x))
            arr.append(x)
        
        print(decoder(n,arr))
        
