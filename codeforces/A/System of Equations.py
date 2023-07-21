import math
while True:
    try:
        n,m=map(int,input().split())
        count=0
        a_max=math.sqrt(n)
        for i in range(0,int(a_max)+1):
            b = n - i ** 2
            if i + b ** 2 == m:
                count+=1
        print(count)
    except:
        break