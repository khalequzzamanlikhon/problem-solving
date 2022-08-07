while True:
    try:
        t=int(input())
        while t:
            n,k=map(int,input().split())
            output=""
            x=input().split()
            for i in range(n):
                x[i]=int(x[i])
                if x[i]%k==0:
                    output+=str(1)
                else:
                    output+=str(0)
            print(output)
    except:
        break

