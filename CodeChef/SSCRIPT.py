while True:
    try:
        T=int(input())
        while T:
            N,K=map(int,input().split())
            character = '*'
            string=input()[:N]
            for i in range(len(string)):
                if string[i]!=character:
                    string[i].lower()
            f=0
            for i in range(len(string)):
                if string[i]==character:
                    if K==1:
                        f=1
                        break
                    elif K>1 and K<=N:
                        if i+K>=N:
                            break
                        elif i+K<N:
                            flag = 0
                            for j in range(i + 1, i + K):
                                if string[j] != character:
                                    flag = 1
                                    break
                            if flag == 0:
                                f = 1
                                break
            if f==1:
                print("YES")
            elif f==0:
                print("NO")

    except:
        break