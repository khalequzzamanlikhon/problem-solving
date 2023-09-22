def cal_points(arr):
   points=0
   for i in range(len(arr)):
       for j in range(len(arr)):
           if arr[i][j]=="X":
               if i<=4:
                  if j<=4:
                   points+=min(i+1,j+1)
                  else:
                   points+=min(i+1,(9-j+1))
               elif i>=4:
                  if j<=4:
                     points+=min((9-i+1),j+1)
                  else:
                     points+=min((9-i+1),(9-j+1))
   return points


while True:
    try:
        t=int(input())
        while(t):
            arr = [input() for _ in range(10)]
            tp=cal_points(arr)
            print(tp)
            t-=1
    except:
        break