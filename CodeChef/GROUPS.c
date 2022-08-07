#include<stdio.h>
#include<string.h>
int main()
{
    int n,i,j,k;
    scanf("%d",&n);
    for(i=0; i<n; i++)
    {
        char str[100000];
        scanf("%s",str);
        int length=strlen(str);
        j=0;
        int count=0;
        while(j<length)
        {
            if(str[j]=='1')
            {
                count++;
                k=j+1;
                while(k<length)
                {
                    if(str[k]=='0')
                    {
                        break;
                    }
                    k++;
                }
                j=k;
            }
            j++;
        }
        printf("%d\n",count);
    }
    return 0;
}
