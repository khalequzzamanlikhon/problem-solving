while True:
    try:
        s = input()[:10]
        max=s[0]
        count=1
        for i in range(1,len(s)):
            if s[i]>max:
                max=s[i]
                count=1
            elif s[i]==max:
                count+=1
        for i in range(count):
            print(max,end='')
        print("\n")
    except:
        break