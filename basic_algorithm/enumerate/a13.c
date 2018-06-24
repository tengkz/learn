#include<stdio.h>
#include<math.h>
int isSu(int x){
    if(x==1) return 0;
    if(x==2) return 1;
    if(x%2==0) return 0;
    int a=(int)sqrt(1.0*x);
    int i;
    for(i=2;i<=a;i++)
        if(x%i==0)
            return 0;
    return 1;
}
void main(){
    int t,x,d;
    int m[1000],n[1000];
    int i,j,k,l,c;
    int ret=0;
    printf("Please input t:");
    scanf("%d",&t);
    if(t%3==0&&isSu(t/3)){
        c=0;
        x=t/3;
        for(i=2;i<x;i+=2){
            if(isSu(x-i)&&isSu(x+i)){
                m[c]=x-i;
                n[c++]=x+i;
            }
        }
        for(i=0;i<c;i++){
            d=x-m[i];
            for(j=0;j<c;j++){
                for(k=j+1;k<c;k++){
                    if(m[j]-m[k]==d){
                        for(l=k+1;l<c;l++){
                            if(m[k]-m[l]==d){
                                printf("%d\t%d\t%d\n%d\t%d\t%d\n%d\t%d\t%d\n",m[l],m[k],m[j],m[i],x,n[i],n[j],n[k],n[l]);
                                printf("====================================\n");
                                ret++;
                            }
                        }
                    }
                }
            }
        }
        printf("There are %d answers totally!\n",ret);
    }
    else{
        printf("The number %d can not be solved!\n",t);
    }
}

