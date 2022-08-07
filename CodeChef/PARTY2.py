# cook your dish here
while True:
    try:
        for _ in range(int(input())):
            n, x, k = map(int, input().split())
            cost = n * x
            if cost <= k:
                print("YES")
            else:
                print("NO")
    except:
        break
