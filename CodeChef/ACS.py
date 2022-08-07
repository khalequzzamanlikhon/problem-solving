while True:
    try:
        for _ in range(int(input())):
            x=int(input())
            q=x//100
            r=x%100
            if q+r<=10:
                print(q+r)
            else:
                print(-1)

    except:
        break