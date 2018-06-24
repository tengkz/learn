#include<stdio.h>
void main(){
    int a[11]={0};
    a[0]=1;
    int i;
    for(i=1;i<=10;i++){
        a[i]=(a[i-1]+1)*2;
    }
    printf("%d\n",a[10]);
}
