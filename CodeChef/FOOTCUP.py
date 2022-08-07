while True:
    try:
        T=int(input())
        for i in range(T):
            X,Y=map(int,input().split())
            if X==Y:
                if X==0:
                    print("NO")
                elif X>0:
                    print("YES")
            else:
                print("NO")
    except:
        break
