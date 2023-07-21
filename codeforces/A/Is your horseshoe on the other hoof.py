while True:
    try:
        n=list(map(int,input().split()))
        count=[]
        for i in range(len(n)):
            if n[i] not in count:
                count.append(n[i])
        print(len(n)-len(count))
    except:
        break