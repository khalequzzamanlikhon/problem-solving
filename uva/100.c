#include<stdio.h>
int main()
{
    int a,b,c,max,min,i,count,k,x;
    while(scanf("%d%d",&a,&b)!=EOF)
    {
        int max_cycle=0;
        if(a>b)
        {
            max=a;
            min=b;
        }
        else
        {
            max=b;
            min=a;
        }
        x=min;
        while(x<=max)
        {
            min=x;
            count=1;
            while(min!=1)
            {

                if(min%2==0)
                {
                    count++;
                    min/=2;
                }
                else
                {
                    count++;
                    min=(3*min)+1;
                }
            }
            if(count>max_cycle)
                max_cycle=count;
            x++;
        }
        printf("%d %d %d\n",a,b,max_cycle);
    }
    return 0;
}
