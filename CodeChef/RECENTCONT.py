# cook your dish here
while True:
    try:
       for _ in range(int(input())):
           n=int(input())
           a = list(map(str, input().strip().split()))[:n]
           x="START38"
           y="LTIME108"
           x_count=0
           y_count=0
           for i in range(len(a)):
               if a[i]==x:
                   x_count+=1
               elif a[i] == y:
                   y_count += 1
           print(x_count,y_count)
    except:
        break