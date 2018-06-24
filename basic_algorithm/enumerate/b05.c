#include<stdio.h>
#include<math.h>
void main()
{
    long m1,m2,i=1,d1,d2;
    double s=0;
    printf("Please input the two limits:");
    scanf("%ld,%ld",&m1,&m2);
    while(s<=m1)
    {
        s+=sqrt(i*1.0)/(i+1);
        i++;
    }
    d1=i;
    while(s<m2)
    {
        s+=sqrt(i*1.0)/(i+1);
        i++;
    }
    d2=i-1;
    printf("%ld,%ld\n",d1,d2);
}
