#include<stdio.h>
void main(){
    int a[5000]={0};
    int n,i,f;
    printf("Please input n:");
    scanf("%d",&n);
    a[1]=1;
    f=1;
    for(i=2;i<=n;i++){
        if(i%2==1)
            a[i]=a[i/2]+a[i/2+1];
        else
            a[i]=a[i/2]+1;
        if(a[i]>f)
            f=a[i];
    }
    for(i=2;i<=n;i++){
        if(a[i]==f)
            printf("a[%d]=",i);
    }
    printf("%d\n",f);
}
