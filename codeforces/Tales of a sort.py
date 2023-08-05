while True:
    try:
        t=int(input())
        for j in range(t):
            n=int(input())
            arr=list(map(int,input().split()))
            ans=0
            for i in range(len(arr)-1):
                if arr[i]>arr[i+1]:
                    ans=max(ans,arr[i])
            print(ans)  
            j+=1

    except:
        break