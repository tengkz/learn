#include<stdio.h>
void main(){
    int a[1600][25];
    int s,i,j,k,t,u;
    int n;
    printf("Please input n:");
    scanf("%d",&n);
    a[1][1]=1;a[1][2]=1;
    a[2][1]=2;
    u=2;
    for(s=3;s<=n;s++){
        for(i=1;i<=u;i++){
            for(j=s;j>=1;j--){
                a[i][j]=a[i][j-1];
            }
            a[i][1]=1;
        }
        k=u;
        for(i=1;i<=u;i++){
            if(a[i][2]<a[i][3]){
                k++;
                for(j=2;j<=s;j++){
                    a[k][j-1]=a[i][j];
                }
                a[k][1]++;
            }
        }
        u=k;
        u++;
        a[u][1]=s;
    }
    for(i=1;i<=u;i++){
        j=1;
        while(a[i][j]>0){
            printf("%d ",a[i][j++]);
        }
        printf("\n");
    }
    printf("%d\n",u);
}
