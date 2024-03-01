def push(myDict,arr):
    for i in arr:
        if i in myDict:
            myDict[i]+=1
        else:
            myDict[i] = 1


def count(arr,myDict):
    total = 0
    for i in arr:
        if myDict[i]==1:
            total+=3
        elif myDict[i]==2:
            total+=1
    
    return total




def decoder(n,arrA,arrB,arrC):
    myDict = {}
    
    push(myDict,arrA)
    push(myDict,arrB)
    push(myDict,arrC)
    
    
    return [count(arrA,myDict),count(arrB,myDict),count(arrC,myDict)]
    

    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arrA = list(input().split())
        arrB = list(input().split())
        arrC = list(input().split())
        print(*decoder(n,arrA,arrB,arrC))