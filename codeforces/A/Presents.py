while True:
    try:
        n=int(input())
        gift_list=list(map(int,input().split()))
        result=[0]*n
        for i in range(n):
            result[gift_list[i]-1]=i+1  
        #print the array
        print(*result)
    except:
        break


#4
#2 3 4 1