while True:
    try:
        n,m=map(int,input().split())
        s=(n*(n+1))/2
        m%=s
        for i in range(1,n+1):
            if m<i:
                break
            m-=i
        print(int(m))
    except:
        break