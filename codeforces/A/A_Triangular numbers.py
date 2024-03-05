
def is_traingular(n):
      
      if n<0:
            return False
      sum=0
      i=1
      while sum<=n:
               sum+=i
               if sum==n:
                     return True
               i+=1
               
      return False

while True:
     try:
          n=int(input())
          if is_traingular(n)==True:
                print("YES")
          else:
                print("NO")
     except:
          break