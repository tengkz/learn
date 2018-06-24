#include<stdio.h>
void main(){
    int a[10000]={0};
    double x[2012]={0};
    x[1]=1.0/2;
    int c=3,m,i;
    double f=0.5;
    a[1]=1;
    a[2]=1;
    for(i=2;i<=2011;i++){
        while(a[c]==1){
            c++;
        }
        a[c]=1;
        a[c+i]=1;
        x[i]=c*1.0/(c+i);
        if(x[i]>f)
            f=x[i];
    }
    printf("%lf,%lf\n",x[2011],f);
}

