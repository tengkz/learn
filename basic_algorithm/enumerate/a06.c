#include<stdio.h>
#include<math.h>
void main()
{
    double i=3.0,s=1.5;
    int sign = -1;
    while(1)
    {
        s+=sign*1.0/i;
        if(s>2)
            break;
        sign*=-1;
        i++;
    }
    printf("%lf\n",i);
}
