# cook your dish here
def odd_even(x):
    if x%2!=0:
        return 1
    elif x%2==0:
        return 0

while True:
    try:
        for _ in range(int(input())):
            a, b, p, q = map(int, input().split())
            if a==p and a+b==p+q:
                print(0)
            else:
                s1 = odd_even(a + b)
                s2 = odd_even(p + q)
                if s1 == s2:
                    print(2)
                else:
                    print(1)
    except:
        break
