while True:
    try:
         n = int(input())
         c = 0
         m = 0
         for _ in range(n):
                a, b = map(int, input().split())
                c -= a
                c += b
                if c > m:
                    m = c
         print(m)
    except:
        break