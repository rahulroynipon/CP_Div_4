def decoder(n, arr):
    vowel = ['a', 'e', 'i', 'o', 'u']
    s = ''

    i = 0
    while i < n:
        if arr[i] not in vowel:
            s += arr[i]
        else:
            s += arr[i]
            if i + 2 < n and arr[i + 2] not in vowel:
                s += arr[i+1]
                i += 1
            
            if i+2>=n:
                pass
            else:
                s+='.'
        i += 1

    return s


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input()
        print(decoder(n, arr))
