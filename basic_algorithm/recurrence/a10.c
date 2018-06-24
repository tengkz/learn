#include<stdio.h>
void main(){
    int b[21]={0};
    int s=0;
    b[1]=1;b[2]=2;
    int i;
    for(i=3;i<=20;i++){
        b[i]=3*b[i-1]-b[i-2];
        s+=b[i];
    }
    printf("%d %d\n",b[20],s);
}
