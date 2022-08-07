while True:
    try:
        t=int(input())
        while t:
            h,p=map(int,input().split())
            while p>0:
                h-=p
                p//=2
            if h>0:
                print(0)
            else:
                print(1)
    except:
        break