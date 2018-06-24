#include<stdio.h>
#include<math.h>
double f(double x)
{
    return 2*pow(x,2)*pow(sin(x),7) + 3*pow(x,0.5)*cos(x) - exp(x)/5;
}
void main()
{
    double c=0.1,m=2.5;
    double a,b;
    double p=1e10,g=m;
    int i,j;
    double k,t;
    printf("Please input the two boundaries:");
    scanf("%lf,%lf",&a,&b);
    c=(b-a)/10;
    k=0;
    for(t=a;t<=b;t+=c){
        if(f(t)*f(b)<0){
            k=1.0;
            break;
        }
    }
    if(k==0){
        printf("There is no solution!\n");
        return;
    }
    c=(b-a)/10;m=(a+b)/2;
    for(i=0;i<8;i++){
        for(k=m-5*c;k<=m+5*c;k+=c){
            t=fabs(f(k));
            if(t<p){
                p=t;
                g=k;
            }
        }
        m=g;
        c/=10;
    }
    printf("%.10lf\n",m);
}
