#include<stdio.h>
void main(){
    int a=1,b=0;
    int a1,b1;
    int t=10,i;
    for(i=1;i<=t;i++){
        a1=b;
        b1=3*a+2*b;
        a=a1;
        b=b1;
    }
    printf("%d %d\n",a,b);
}
