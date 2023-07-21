def good_element_sum(matrix):
     n=len(matrix)
     middle=n//2
     d1_sum=sum(matrix[i][i] for i in range(n))
     d2_sum=sum(matrix[i][n-i-1] for i in range(n))
     mr_sum=sum(matrix[middle][j] for j in range(n))
     mc_sum=sum(matrix[j][middle] for j in range(n))
     minus_term=matrix[middle][middle]
     return d1_sum+d2_sum+mr_sum+mc_sum -minus_term*3
     
while True:
    try:
         n=int(input())
         matrix=[]
         for _ in range(n):
              row=list(map(int,input().split()))
              matrix.append(row)
         sum=good_element_sum(matrix)
         print(sum)
    except:
         break