#include<stdio.h>
#include<math.h>
void main()
{
    int a,b;
    scanf("%d,%d",&a,&b);
    int x,s,f=0,q;
    float t=0.0;
    int i,k;
    for(i=a;i<=b;i++)
    {
        s=1;
        q=(int)sqrt(i);
        for(k=2;k<=q;k++)
        {
            if(i%k==0)
                s+=(k+i/k);
        }
        if(q*q==b)
            s-=q;
        if(s*1.0/i>t)
        {
            t=s*1.0/i;
            f=i;
        }
    }
    printf("max ratio is %f, at index %d\n",t,f);
}
