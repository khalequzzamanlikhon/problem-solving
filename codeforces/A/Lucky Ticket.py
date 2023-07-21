while True:
    try:
        n=int(input())
        number=int(input())
        number_string=[]
        for i in range(n):
            val=number%10
            number=number//10
            number_string.append(val)
        four1=0
        seven1=0
        four2 = 0
        seven2 = 0
        sum1=0
        sum2=0
        for i in range(len(number_string)):
            if i<n//2:
                if number_string[i]==4:
                    four1+=1
                    sum1+=number_string[i]
                elif number_string[i]==7:
                    seven1+=1
                    sum1 += number_string[i]
            else:
                if number_string[i]==4:
                    four2+=1
                    sum2 += number_string[i]
                elif number_string[i]==7:
                    seven2+=1
                    sum2 += number_string[i]
 
        count=four2+four1+seven2+seven1
        if count!=n:
            print("NO")
        else:
            if sum1==sum2:
                print("YES")
            else:
                print("NO")
    except:
        break