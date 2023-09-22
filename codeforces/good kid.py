def factorial(arr):
    fact=1
    for x in arr:
        fact*=x
    return fact
while True:
    try:
        t=int(input())
        while(t):
            n=int(input())
            arr=list(map(int,input().split()))[:n]
            arr.sort()
            arr[0]+=1
            mul=factorial(arr)
            print(mul)
            t-=1

    except:
        break