from itertools import count
while True:
    try:
        for _ in range(int(input())):
            x=int(input())
            lst=input().split()
            for i in range(x):
                lst[i]=int(lst[i])
            st=set(lst)
            lst1=list(st)
            ls=[]
            for i in range(len(lst1)):
                p=lst.count(lst1[i])
                ls.append(p)
            print(len(lst)-max(ls))

    except:
        break

