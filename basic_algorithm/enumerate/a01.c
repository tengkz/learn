#include<stdio.h>
int main(void){
    int m=0,n=0,mNum=0,nNum=0;
    int i;
    for(i=10000;i<=99999;i++){
        if(i%7==0)
            continue;
        int t = i,flag = 0;
        while(t){
            if(t%10==7){
                flag++;
            }
            t/=10;
        }
        if(flag==1){
            m+=i;
            mNum++;
        }
        if(flag==2){
            m+=i;
            mNum++;
            n+=i;
            nNum++;
        }
    }
    printf("m=%d,n=%d\n",m,n);
    printf("mNum=%d,nNum=%d\n",mNum,nNum);
    return 0;
}
