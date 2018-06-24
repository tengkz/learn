#include<stdio.h>
int maxCommon(int a,int b)
{
    int t;
    if(a<b)
    {
        t=a;
        a=b;
        b=t;
    }
    t=a%b;
    while(t)
    {
        a=b;
        b=t;
        t=a%b;
    }
    return b;
}
void main()
{
    int i,j;
    int m,n;
    printf("Please input m and n:");
    scanf("%d,%d",&m,&n);
    int c=0;
    double s=0.0;
    for(i=m;i<=n;i++)
    {
        for(j=1;j<=i-1;j++)
        {
            if(maxCommon(i,j)==1)
            {
                c++;
                s+=j*1.0/i;
            }
        }
    }
    printf("%d,%lf\n",c,s);
}
