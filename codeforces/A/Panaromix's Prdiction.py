def prime_number(x):
    flag=1
    for i in range(2,(x//2)+1):
        if x%i==0:
            flag=0
            break
    if flag==1:
        return True
    else:
        return False
    
def next_prime(x):
    x+=1
    while prime_number(x)!=True:
        x+=1
    return x

while True:
    try:
        n,m=map(int,input().split())
        r=prime_number(m)
        if r==True:
            next=next_prime(n)
            if next==m:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    except:
        break