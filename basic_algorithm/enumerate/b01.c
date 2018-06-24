#include<stdio.h>
void main()
{
    int c,j,m,n,f[10];
    long d,k,g1,g2,s1,s2,t;
    printf("Please input m and n:");
    scanf("%d,%d",&m,&n);
    t=1;
    for(k=1;k<=n-1;k++)
        t*=10;
    g1=0;s1=0;
    g2=0;s2=0;
    for(k=t;k<=10*t-1;k++)
    {
        d=k;
        for(j=0;j<=9;j++)   f[j]=0;
        for(j=1;j<=n;j++)
        {
            c=d%10;f[c]+=1;
            d/=10;
        }
        if(f[m]>0&&k%m>0)
        {
            g1++;
            s1+=k;
        }
        if(f[m]==2&&k%m>0)
        {
            g2++;
            s2+=k;
        }
    }
    printf("g1=%d,g2=%d\n",g1,g2);
    printf("s1=%d,s2=%d\n",s1,s2);
}
