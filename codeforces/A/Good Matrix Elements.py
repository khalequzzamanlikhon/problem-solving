while True:
    try:
       n=int(input())
       grid=[]
       for i in range(n):
           t=input().split()
           for j in range(n):
               t[j]=int(t[j])
           grid.append(t)
       sum=0
       v_x=int((n-1)/2)
       v_y=int((n-1)/2)
       sum+=grid[v_x][v_y]
       init_sum=sum
       for i in range(8):
           if i==0:
               while v_x>=0:
                   sum+=grid[v_x][v_y]
                   v_x-=1
           elif i==1:
               v_x = int((n - 1) / 2)
               while v_x<n:
                   sum += grid[v_x][v_y]
                   v_x += 1
           elif i==2:
               v_x = int((n - 1) / 2)
               while v_y<n:
                   sum += grid[v_x][v_y]
                   v_y+= 1
           elif i == 3:
               v_y = int((n - 1) / 2)
               while v_y >=0:
                   sum += grid[v_x][v_y]
                   v_y -= 1
           elif i == 4:
               v_y = int((n - 1) / 2)
               while v_y >=0 and v_x>=0:
                   sum += grid[v_x][v_y]
                   v_y -= 1
                   v_x-=1
           elif i == 5:
               v_x = int((n - 1) / 2)
               v_y = int((n - 1) / 2)
               while v_y<n and v_x<n:
                   sum += grid[v_x][v_y]
                   v_y += 1
                   v_x+=1
           elif i == 6:
               v_x = int((n - 1) / 2)
               v_y = int((n - 1) / 2)
               while v_y<n and v_x>=0:
                   sum += grid[v_x][v_y]
                   v_y += 1
                   v_x-=1
 
           elif i == 7:
               v_x = int((n - 1) / 2)
               v_y = int((n - 1) / 2)
               while v_y>=0 and v_x<n:
                   sum += grid[v_x][v_y]
                   v_y -= 1
                   v_x+=1
       print(sum-8*init_sum)
 
    except:
        break