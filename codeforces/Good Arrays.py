while True:
    try:
        t=int(input())
        while t:
           n=int,input()
           arr=list(map(int,input().split()))
           sum_a=0
           cnt_1=0
           for x in arr:
               sum_a+=x
               if x==1:
                   cnt_1+=1
           p=len(arr)
           if sum_a>=cnt_1+p and p>1:
               print("YES")
           else:
               print("NO")
           t-=1
    except:
        break    