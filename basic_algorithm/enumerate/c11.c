#include<stdio.h>
void main(){
    int c[6];
    int t,a,b;
    int i,j;
    for(a=100;a<999;a++){
        for(b=a+1;b<999;b++){
            t=0;
            c[0]=a/100;
            c[1]=(a-c[0]*100)/10;
            c[2]=a%10;
            c[3]=b/100;
            c[4]=(b-c[3]*100)/10;
            c[5]=b%10;
            for(i=0;i<6;i++){
                for(j=i+1;j<6;j++){
                    if(c[i]==c[j]){
                        t=1;
                        break;
                    }
                }
                if(t==1)
                    break;
            }
            if(t==1)
                continue;
            for(i=1;i<6;i++){
                if(c[i]<c[0]){
                    t=1;
                    break;
                }
            }
            if(t==1)
                continue;
            if((100*c[0]+10*c[1]+c[2])*(100*c[3]+10*c[4]+c[5])==(100*c[2]+10*c[1]+c[0])*(100*c[5]+10*c[4]+c[3]))
                printf("%d%d%dX%d%d%d=%d%d%dX%d%d%d\n",c[0],c[1],c[2],c[3],c[4],c[5],c[2],c[1],c[0],c[5],c[4],c[3]);
        }
    }
}
