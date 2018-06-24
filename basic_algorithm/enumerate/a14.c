#include<stdio.h>
int solve(int x){
    if(x<36)
        return 0;
    int a[9]={0};
    int b,c;
    int d1,d2,d3;
    int e1,e2,e3;
    int s1;
    int ret=0;
    for(a[4]=1;a[4]<=x-28;a[4]++){
        for(a[6]=a[4]+1;a[6]<=x-a[4]-1-21;a[6]++){
            for(a[1]=1;a[1]<=x-28;a[1]++){
                if(a[1]==a[4]||a[1]==a[6])  continue;
                b=(x+a[4]+a[1]+a[6]);
                if(b%3!=0)  continue;
                s1=b/3;
                e1=s1-a[1]-a[4];
                for(a[2]=1;a[2]<=e1/2;a[2]++){
                    if(a[2]==a[1]||a[2]==a[4]||a[2]==a[6])  continue;
                    a[3]=e1-a[2];
                    if(a[3]==a[2]||a[3]==a[1]||a[3]==a[4]||a[3]==a[6])  continue;
                    e2=s1-a[1]-a[6];
                    for(a[7]=1;a[7]<=e2/2;a[7]++){
                        if(a[7]==a[1]||a[7]==a[2]||a[7]==a[3]||a[7]==a[4]||a[7]==a[6])  continue;
                        a[8]=e2-a[7];
                        if(a[7]==a[8]||a[8]==a[1]||a[8]==a[2]||a[8]==a[3]||a[8]==a[4]||a[8]==a[6])  continue;
                        a[5]=s1-a[4]-a[6];
                        if(a[5]==a[1]||a[5]==a[2]||a[5]==a[3]||a[5]==a[4]||a[5]==a[6]||a[5]==a[7]||a[5]==a[8])  continue;
                        d1=a[1]*a[2]*a[3]*a[4];
                        d2=a[1]*a[7]*a[8]*a[6];
                        d3=a[4]*a[5]*a[6];
                        if(d1==d2&&d2==d3){
                            printf("%d,%d,%d,%d,%d,%d,%d,%d\n",a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]);
                            ret++;
                        }
                    }
                }
            }
        }
    }
    return ret;
}
void main(){
    int n;
    int ret=solve(89);
    printf("Number of answers is %d\n",ret);
}
