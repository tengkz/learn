#include<stdio.h>
void main(){
    int a=1,b=1,c=1;
    int s=1,n,t;
    printf("Please input n:");
    scanf("%d",&n);
    int i;
    for(i=2;i<=n;i++){
        if(a*2<b*3&&a*2<c*5){
            a*=2;
            t=a;
        }
        if(b*3<a*2&&b*3<c*5){
            b*=3;
            t=b;
        }
        if(c*5<a*2&&c*5<b*3){
            c*=5;
            t=c;
        }
        s+=t;
    }
    printf("%d,%d\n",t,s);
}
        
