#include<stdio.h>
void main(){
    int a[31]={0};
    a[1]=1;a[2]=1;a[3]=2;
    int i;
    for(i=4;i<=30;i++){
        a[i]=a[i-1]+a[i-3];
    }
    printf("%d\n",a[30]);
}
