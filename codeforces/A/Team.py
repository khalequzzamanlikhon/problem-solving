while True:
    try:
        n = int(input())
        count = 0
        for i in range(n):
            x = list(map(int, input().split()))
            if sum(x) >= 2:
                count += 1
        print(count)
    except:
        break