#include<stdio.h>
void input(int start,int n,int i,int j,int a[100][100])
{
    if(n==1)
    {
        a[i][j] = start;
        return;
    }
    for(int k=0;k<n;k++)
    {
        a[i][j+k] = start++;
    }
    for(int k=1;k<n;k++)
    {
        a[i+k][j+n-1] = start++;
    }
    for(int k=1;k<n;k++)
    {
        a[i+n-1][j+n-k-1] = start++;
    }
    for(int k=1;k<n-1;k++)
    {
        a[i+n-k-1][j] = start++;
    }
    input(start,n-2,i+1,j+1,a);
}

int main()
{
    int a[100][100] = {0};
    int n;
    printf("Please input n(n<10):");
    scanf("%d",&n);
    input(1,n,0,0,a);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            printf("%3d\t",a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
