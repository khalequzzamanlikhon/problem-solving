# cook your dish here
while True:
    try:
        for _ in range(int(input())):
            a,b,c = map(int, input().split())
            if a>b+c or b>a+c or c>a+b:
                print("YES")
            else:
                print("NO")

    except:
        break
