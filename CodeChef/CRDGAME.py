while True:
    try:
        t=int(input())
        while(t):
            c_count = 0
            m_count = 0
            r=int(input())
            for i in range(r):
                sum_a = 0
                sum_b=0
                a,b=map(int,input().split())
                while(a>0):
                    sum_a+=a%10
                    a//=10
                while(b>0):
                    sum_b += b % 10
                    b //= 10
                if sum_a!=sum_b:
                    if sum_a>sum_b:
                        c_count+=1
                    else:
                        m_count+=1
                else:
                    m_count+=1
                    c_count+=1
            if c_count > m_count:
                print(0, c_count)
            elif m_count > c_count:
                print(1, m_count)
            else:
                print(2, c_count)
    except:
        break