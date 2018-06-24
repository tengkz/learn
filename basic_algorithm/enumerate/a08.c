#include<stdio.h>
#include<math.h>
void main()
{
    int n;
    int a[99999]={0};
    printf("Please input n:");
    scanf("%d",&n);
    int i,j;
    for(i=1;i<=n;i++)
    {
        for(j=2*i;j<=n;j+=i)
        {
            a[j]+=i;
        }
    }
    int flag=0;
    float mr=0.0;
    for(i=2;i<=n;i++)
    {
        if(a[i]*1.0/i>mr)
        {
            mr=a[i]*1.0/i;
            flag=i;
        }
    }
    printf("max ratio = %f, at index %d\n",mr,flag);
}
