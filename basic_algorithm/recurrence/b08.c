#include<stdio.h>
void main(){
    int a[6]={0};
    int i,flag=0;
    a[0]=-1;
    while(1){
        a[0]+=4;
        for(i=1;i<=5;i++){
            if( (5*a[i-1]+1)%4==0 ){
                a[i]=(5*a[i-1]+1)/4;
                if(i==5)    flag=1;
            }
            else{
                break;
            }
        }
        if(flag==1){
            break;
        }
    }
    for(i=0;i<6;i++){
        printf("%d ",a[i]);
    }
}
