while True:
    try:
        for _ in range(int(input())):
            n,k,v=map(int,input().split())
            a=list(map(int,input().split()))
            sum2=v*(n+k)-sum(a)
            if sum2<=0:
                print(-1)
            else:
                avg = sum2 / k

                if int(avg) * k == int(sum2):

                    print(int(avg))
                else:

                    print(-1)



    except:
        break
