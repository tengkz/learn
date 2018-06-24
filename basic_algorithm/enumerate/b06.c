#include<stdio.h>
#include<math.h>
void main()
{
    double s=0;
    long i=1,j,n;
    printf("Please input n:");
    scanf("%ld",&n);
    while(s<=n)
    {
        if(i%3==0)
            s-=1.0/i;
        else
            s+=1.0/i;
        i++;
    }
    printf("%ld\n",i-1);
    for(j=0;j<3;j++)
    {
        if(i%3==0)
            s-=1.0/i;
        else
            s+=1.0/i;
        if(s>n)
            printf("%ld\n",i);
        i++;
    }
}
