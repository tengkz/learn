#include<stdio.h>
void main(){
    int a[10]={0};
    a[0]=-1;
    while(1){
        a[0]+=4;
        if( (5*a[0]+1)%4==0 ){
            a[1]=(5*a[0]+1)/4*5+1;
            if( a[1]%4==0 ){
                a[2]=a[1]/4*5+1;
                if( a[2]%4==0 ){
                    a[3]=a[2]/4*5+1;
                    if( a[3]%4==0 ){
                        a[4]=a[3]/4*5+1;
                        if( a[4]%4==0 ){
                            a[5]=a[4]/4*5+1;
                            printf("%d %d %d %d %d %d\n",a[0],a[1],a[2],a[3],a[4],a[5]);
                            break;
                        }
                    }
                }
            }
        }
    }
}
