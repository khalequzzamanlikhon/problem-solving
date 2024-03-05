while True:
    try:
        n=int(input())
        d_i=list(map(int,input().split()))
        a,b=map(int,input().split())
        y=0
        for i in range(a-1,b-1):
            y+=d_i[i]
        print(y)
    except:
        break