
def gcd(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m
while True:
    try:
       a, b, n = map(int, input().split())
       while True:
            n -= gcd(a, n)
            if n == 0:
                print(0)
                break
            n -= gcd(b, n)
            if n == 0:
                print(1)
                break
    except:
        break
 
