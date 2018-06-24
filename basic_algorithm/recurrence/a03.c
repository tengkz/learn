#include<stdio.h>
#include<math.h>
void main(){
    double a,b,x,y,s,m;
    int n;
    a=2.0;b=3.0;m=3.0;s=6.0;
    printf("Please input n:");
    scanf("%d",&n);
    int i;
    for(i=4;i<=n;i++){
        if(a*2<b*3){
            a*=2;
            m=a;
        }
        else{
            b*=3;
            m=b;
        }
        s+=m;
    }
    printf("%.0lf,%.0lf\n",m,s);
}
