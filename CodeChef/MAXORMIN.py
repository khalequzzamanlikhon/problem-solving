while True:
    try:
        for _ in range(int(input())):
            inn=int(input())
            arr=input().split()
            arr_1=[]
            arr_0=[]
            for i in range(inn):
                arr[i]=int(arr[i])
                if arr[i]==1:
                    arr_1.append(arr[i])
                else:
                    arr_0.append(arr[i])
            if len(arr_1)>=len(arr_0):
                print(1)
            else:
                print(0)

    except:
        break
