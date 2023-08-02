while True:
    try:
        n=int(input())
        count=0
        while n!=0:
            x=n%10
            n//=10
            if x==4 or x==7:
                count+=1
        if count==4 or count==7:
            print("YES")
        else:
            print("NO")
    except:
        break