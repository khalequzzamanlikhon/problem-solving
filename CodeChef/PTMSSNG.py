while True:
    try:
        t = int(input())
        while t:
            n = int(input())
            x = []
            y = []
            for j in range(4 * n - 1):
                a, b = map(int, input().split())
                x.append(a)
                y.append(b)
            missing_X = [mp for mp in x if x.count(mp) == 1][0]
            missing_Y = [mp for mp in y if y.count(mp) == 1][0]
            print(missing_X, missing_Y)
    except:
        break