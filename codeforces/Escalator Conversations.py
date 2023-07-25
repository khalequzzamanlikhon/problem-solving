while True:
    try:
        t=int(input())
        for _ in range(t):
            n,m,k,H=map(int,input().split())
            h=list(map(int,input().split()))
            l=[i for i in range(1,m+1)]
            arr=[p*k for p in l]
            diff_list=[]
            for i in range(len(arr)-1):
                for j in range(i+1,len(arr)):
                    val=abs(arr[i]-arr[j])
                    diff_list.append(val)
            con=0
            for i in range(len(h)):
                h_diff=abs(H-h[i])
                for x in diff_list:
                    if x==h_diff:
                        con+=1
                        break     
            print(con)
    except:
        break