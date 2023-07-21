while True:
    try:
        for _ in range(int(input())):
            n=int(input())
            value=input().split()
            for i in range(n):
                value[i]=int(value[i])
            value.sort()
            flag=0
            for i in range(len(value)-1):
                if abs(value[i]-value[i+1])>1:
                    flag=1
                    break
            if flag==0:
                print("YES")
            else:
                print("NO")
    except:
        break