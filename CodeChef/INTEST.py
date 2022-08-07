while True:
    try:
        n,k=input().split()
        n=int(n)
        k=int(k)
        count=0
        for i in range(n):
            x=int(input())
            if x%k==0:
                count+=1
        print(count)
    except:
        break
