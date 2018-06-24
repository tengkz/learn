#include<stdio.h>
void main(){
    int a[2012]={0};
    a[1]=1;
    int s=1;
    int i,j,k;
    j=1;k=1;
    for(i=2;i<=2011;i++){
        if(2*a[j]<3*a[k]){
            a[i]=2*a[j++]+1;
        }
        else{
            a[i]=3*a[k++]+1;
        }
        s+=a[i];
    }
    printf("a[2011]=%d,sum=%d\n",a[2011],s);
}
