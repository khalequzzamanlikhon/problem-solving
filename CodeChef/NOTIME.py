while True:
    try:
        N,H,x=map(int,input().split())
        T=input().split()
        for i in range(N):
            T[i]=int(T[i])
        flag=0
        for i in range(N):
            if T[i]+x>=H:
                flag=1
                break

        if flag==1:
            print("YES")
        else:
            print("NO")

    except:
        break