while True:
    try:
        n,k=map(int,input().split())
        score=input().split()
        for i in range(n):
            score[i]=int(score[i])
        count = 0
        for i in range(len(score)):
            if score[i]>=score[k-1] and score[i]>0:
                count+=1
        print(count)
    except:
        break