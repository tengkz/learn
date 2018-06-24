#include<stdio.h>
void main(){
    int i=1,x;
    do{
        x=11*i+10;
        i+=5;
    }while(!(x%5==1&&x%6==5&&x%7==4));
    printf("%d\n",x);
}
