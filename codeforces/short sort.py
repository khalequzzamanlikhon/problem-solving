def pos_check(s):
    my_str="abc"
    count=0
    for i in range(len(s)):
        if s[i]!=my_str[i]:
            count+=1
    if count<=2:
        return True
    else:
        return False

while True:
    try:
        t=int(input())
        while(t):
            s=input()
            result=pos_check(s)
            if result==True:
                print("yes")
            else:
                print("no")
            t-=1

    except:
        break