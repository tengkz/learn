#include<stdio.h>
#include<math.h>
void main()
{
    double i=1,s=0;
    while(1)
    {
        s+=sqrt(i)/(i+1);
        if(s>2010&&s<2011)
            break;
        i++;
    }
    printf("%lf\n",i);
}
