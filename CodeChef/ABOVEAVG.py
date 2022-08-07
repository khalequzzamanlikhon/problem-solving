# cook your dish here
while True:
    try:
        for _ in range(int(input())):
            n,m,x=map(int,input().split())
            if m==x:
                print(0)
            else:
                t=x*n
                print(t//(x+1))
    except:
        break
