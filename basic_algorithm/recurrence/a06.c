#include<stdio.h>
void main(){
    int a[100][100]={0};
    int i,j,n;
    printf("Please input n:");
    scanf("%d",&n);
    a[1][1]=1;
    for(i=2;i<=n;i++){
        a[1][i]=(i-1)*(i-1)+1;
        for(j=2;j<=i;j++){
            a[j][i]=a[j-1][i]+1;
        }
        for(j=i-1;j>=1;j--){
            a[i][j]=a[i][j+1]+1;
        }
    }
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            printf("%6d",a[i][j]);
        }
        printf("\n");
    }
}
