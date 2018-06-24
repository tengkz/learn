#include<stdio.h>
void main(){
    int a[100]={0};
    int n,k;
    printf("Please input n:");
    scanf("%d",&n);
    n--;
    a[0]=1;
    for(k=1;k<=n;k++){
        a[k]=a[k-1]*(n-k+1)/k;
    }
    for(k=0;k<=n;k++){
        printf("%d ",a[k]);
    }
}
