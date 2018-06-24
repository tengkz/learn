#include<stdio.h>
int f(int m,int n){
    if(n==0)
        return 1;
    if(n>m)
        return 0;
    else
        return f(m-1,n)+f(m,n-1);
}
void main(){
    int m,n;
    printf("Please input m and n:");
    scanf("%d,%d",&m,&n);
    printf("Number is %d\n",f(m,n));
}
