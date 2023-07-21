while True:
    try:
        n=int(input())
        if n%2!=0:
            print(-1)
        else:
            list=[]
            for i in range(n):
                list.append(i+1)
            for i in range(0,n,2):
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
            print(*list)
    except:
        break