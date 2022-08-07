# cook your dish here
while True:
    try:
        for _ in range(int(input())):
            n,d=map(int,input().split())
            p=input().split()
            p_risk=[]
            p_not_risk=[]
            for i in range(n):
                p[i]=int(p[i])
                if p[i]<=9 or p[i]>=80:
                    p_risk.append(p[i])
                else:
                    p_not_risk.append(p[i])
            day_count=0
            if len(p_risk)%d==0:
                day_count+=len(p_risk)//d
            else:
                day_count += (len(p_risk) // d)+1
            if len(p_not_risk) % d == 0:
                day_count += len(p_not_risk) // d
            else:
                day_count += (len(p_not_risk) //d) + 1
            print(day_count)
    except:
        break
