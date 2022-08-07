while True:
    try:
        T=int(input())
        for i in range(T):
            X,Y=map(int,input().split())
            QT=X+(X*(7/100))
            if Y<=QT:
                print("YES")
            else:
                print("NO")
    except:
        break
