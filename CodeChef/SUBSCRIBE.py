# cook your dish here
while True:
    try:
        for _ in range(int(input())):
            inn=int(input())
            if inn<=30:
                print("NO")
            else:
                print("YES")

    except:
        break
