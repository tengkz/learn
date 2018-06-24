#include<stdio.h>
void main(){
    int a[2012]={0};
    int q=3;
    a[0]=1;
    int s=1;
    int i;
    for(i=1;i<=10;i++){
        a[i]=2*a[i-1]+q;
        q*=3;
        s+=a[i];
    }
    printf("%d %d\n",a[10],s);
}
