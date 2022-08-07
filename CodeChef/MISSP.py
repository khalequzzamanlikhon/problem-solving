while True:
    try:
        for _ in range(int(input())):
            n=int(input())
            doll=[]
            for i in range(n):
                z=int(input())
                doll.append(z)
            for m in doll:
                if doll.count(m)%2!=0:
                    print(m)
                    break

    except:
        break
