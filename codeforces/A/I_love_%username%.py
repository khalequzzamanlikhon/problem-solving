while True:
    try:
        n=int(input())
        score=input().split()
        for i in range(n):
            score[i]=int(score[i])
        count=0
        # #checking for least
        for i in range(1,len(score)):
            #checking for least
            min=1
            for j in range(i):
                if score[i]>=score[j]:
                    min=0
                    break
            if min==1:
                count+=1
 
        #checking for max
        for i in range(1,len(score)):
            max=1
            for j in range(i):
                if score[i]<=score[j]:
                    max=0
                    break
            if max==1:
                count+=1
        print(count)
    except:
        break