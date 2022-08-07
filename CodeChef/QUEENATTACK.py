while True:
    try:
        for _ in range(int(input())):
            n,x,y=map(int,input().split())
            board=[]
            count = 0
            up = x - 1
            down = n - x
            right = n - y
            left = y - 1
            count += up + down + right + left
            #principal diagonal
            #upper part
            count+=min(x-1,y-1)
            #down part
            count+=min(n-x,n-y)
            #extra diagonal
            #down part
            count+=min(y-1,n-x)
            #upper part
            count+=min(n-y,x-1)
            print(count)
    except:
        break
