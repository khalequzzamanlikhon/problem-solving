while True:
    try:
        A,B,C=map(int,input().split())
        if A==B or A==C or A==C:
            print("YES")
        else:
            print("NO")
    except:
        break
