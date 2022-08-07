#include<stdio.h>
#include<string.h>
int count_movement(char a[],int arr[])
{
    int i,sum=0,g[3],b[3],c[3],cn;
    for(i=0; i<9; i++)
    {
        sum+=arr[i];
    }
    b[0]=arr[0];
    b[1]=arr[3];
    b[2]=arr[6];
    g[0]=arr[1];
    g[1]=arr[4];
    g[2]=arr[7];
    c[0]=arr[2];
    c[1]=arr[5];
    c[2]=arr[8];
    if(strcmp(a,"BCG")==0)
        cn=sum-(g[2]+b[0]+c[1]);
    else if(strcmp(a,"BGC")==0)
        cn=sum-(g[1]+b[0]+c[2]);
    else if(strcmp(a,"CBG")==0)
        cn=sum-(g[2]+b[1]+c[0]);
    else if(strcmp(a,"CGB")==0)
        cn=sum-(g[1]+b[2]+c[0]);
    else if(strcmp(a,"GBC")==0)
        cn=sum-(g[0]+b[1]+c[2]);
    else if(strcmp(a,"GCB")==0)
        cn=sum-(g[0]+b[2]+c[1]);
    return cn;
}
int main()
{
    int bottles[9],i,count[6],min=2147483647;
    char combination[6][6] = {"BCG", "BGC", "CBG", "CGB", "GBC", "GCB"};
    char output[10];
    while(scanf("%d",&bottles[0])!=EOF)
    {

        for(i=1; i<9; i++)
        {
            scanf("%d",&bottles[i]);
        }
        for(i=0; i<6; i++)
        {
            count[i]=count_movement(combination[i],bottles);
            if(count[i]<min)
            {
                min=count[i];
                strcpy(output,combination[i]);
            }
        }
        printf("%s %d\n",output,min);
        min=2147483647;
    }

    return 0;
}
