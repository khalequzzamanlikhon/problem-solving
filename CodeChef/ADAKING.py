import random
def distance(x1, y1, x2, y2):
    z = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return z
while True:
    try:
        t = int(input())
        while (t):
            k = int(input())
            x = []
            for i in range(8):
                y = []
                for j in range(8):
                    y.append('*')
                x.append(y)
            king_x = random.randint(0, 7)
            king_y = random.randint(0, 7)
            x[king_x][king_y] = "O"
            k -= 1
            tx = []
            ty = []
            tx.append(king_x)
            ty.append(king_y)
            while (k):
                m = 100
                while (m > 2):
                    p = random.randint(0, 7)
                    q = random.randint(0, 7)
                    xy = random.randint(0, len(tx) - 1)
                    m = distance(tx[xy], ty[xy], p, q)

                if x[p][q] != "O" and x[p][q] != ".":
                    x[p][q] = "."
                    k -= 1
                    tx.append(p)
                    ty.append(q)
            for i in range(8):
                for j in range(8):
                    flag = 0
                    for k in range(len(tx)):
                        if x[i][j] != "O" and x[i][j] != "." and x[i][j] != "X":
                            d = distance(tx[k], ty[k], i, j)
                            if d <= 2:
                                flag = 1
                                break
                    if flag == 1:
                        x[i][j] = "X"
                    elif flag == 0:
                        if x[i][j] != "O" and x[i][j] != ".":
                            x[i][j] = "."
            for i in range(8):
                for j in range(8):
                    print(x[i][j], end='')
                print('')
    except:
        break