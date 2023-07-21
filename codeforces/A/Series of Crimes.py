import random
while True:
    try:
       n,m=map(int,input().split())
       district_map=[['.' for i in range(m)] for j in range(n)]
       x_val=[]
       y_val=[]
       while True:
           if len(x_val)>=3:
               break
           x = random.randint(0, n-1)
           y = random.randint(0, m-1)
           print("value of position",x,y)
           if district_map[x][y] != '*':
               if len(x_val)<2:
                   district_map[x][y] = '*'
                   x_val.append(x)
                   y_val.append(y)
               else:
                   if x in x_val and y in y_val:
                       district_map[x][y]="*"
                       x_val.append(x)
                       y_val.append(y)
       for i in range(len(x_val)):
           count=x_val.count(x_val[i])
           if count%2!=0:
               v_x=x_val[i]
               v_y=y_val[i]
               break
       print(v_x,v_y)
    except:
        break