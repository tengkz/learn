#include<stdio.h>
void main()
{
    int n;
    printf("Please input the number of digits:");
    scanf("%d",&n);
    int g[10],f[10];
    long long s[10];
    int i;
    for(i=0;i<10;i++)
    {
        g[i]=0;
        s[i]=0;
    }
    int d,c,j,t=1;
    for(i=1;i<n;i++)
        t*=10;
    for(i=t;i<=t*10-1;i++)
    {
        d=i;
        for(j=0;j<10;j++)
            f[j]=0;
        for(j=1;j<=n;j++)
        {
            c=d%10;
            f[c]+=1;
            d/=10;
        }
        for(j=0;j<10;j++)
        {
            if(f[j]>0)
            {
                g[j]++;
                s[j]+=i;
            }
        }
    }
    int p,q;
    printf("Please input p and q:");
    scanf("%d,%d",&p,&q);
    printf("Number of p is %d,number of q is %d\n",g[p],g[q]);
    printf("Sum of p is %d,sum of q is %d\n",s[p],s[q]);
}
