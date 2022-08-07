while True:
    try:
        t=int(input())
        while t:
            n=int(input())
            x=input().split()
            for i in range(n):
                x[i]=int(x[i])
            flag=0
            for z in x:
                if z%2==0:
                    flag=1
                    break
            if flag==1:
                print("NO")
            elif flag==0:
                print("YES")
    except:
        break