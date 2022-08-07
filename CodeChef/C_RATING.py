# cook your dish here
while True:
    try:
       for _ in range(int(input())):
           x,y=map(int,input().split())
           count=0
           while x<y:
               x+=8
               count+=1
           print(count)
    except:
        break