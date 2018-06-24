#include<stdio.h>
void main(){
    int c[10000]={0};
    int d[10000]={0};
    int cmax=1,dmax=100,imax=1;
    int flag=0;
    c[1]=1;d[1]=2;
    c[2]=3;d[2]=5;
    int i,j,k;
    for(i=3;i<=2011;i++){
        for(j=c[i-1]+1;j<=d[i-1];j++){
            flag=0;
            for(k=1;k<=i-1;k++){
                if(d[k]==j){
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                c[i]=j;
                break;
            }
        }
        d[i]=c[i]+i;
        if(c[i]*dmax>cmax*d[i]){
            cmax=c[i];
            dmax=d[i];
            imax=i;
        }
    }
    printf("%d/%d\n",c[2011],d[2011]);
    printf("a[%d]=%d/%d\n",imax,cmax,dmax);
}
