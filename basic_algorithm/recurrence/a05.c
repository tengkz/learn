#include<stdio.h>
void main(){
    long a[100]={0};
    int n,i,t,j,x;
    printf("Please input n:");
    scanf("%d",&n);
    a[0]=1;
    printf("1\n");
    for(i=1;i<n;i++){
        t=1;
        for(j=1;j<=i;j++){
            x=a[j];
            a[j]+=t;
            t=x;
        }
        for(j=0;j<=i;j++)
            printf("%d ",a[j]);
        printf("\n");
    }
}
