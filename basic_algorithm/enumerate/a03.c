#include<stdio.h>
#include<math.h>
void main()
{
    long y=1,x;
    double x2;
    while(1)
    {
        x2 = y*y*73+1;
        x = (long)floor(sqrt(x2));
        if(x*x==(long)x2)
            break;
        y++;
    }
    printf("y=%d,x=%ld\n",y,x);
}
