#include<stdio.h>
#include<math.h>
double f(double x)
{
    return fabs( 2*pow(x,2)*pow(sin(x),7) + 3*pow(x,0.5)*cos(x) - exp(x)/5 );
}
void main()
{
    double c=0.1,m=2.5;
    double p=1e10,g=m,t;
    int i,j;
    double k;
    for(i=0;i<10;i++)
    {
        printf("a=%lf,b=%lf\n",m-5*c,m+5*c);
        for(k=m-5*c;k<=m+5*c;k+=c)
        {
            t = f(k);
            printf("%lf,",t);
            if(t<p)
            {
                p = t;
                g = k;
            }
        }
        printf("\n");
        m=g;
        c/=10;
    }
    printf("%.8lf\n",m);
}
