#include<stdio.h>
void main()
{
    int a[3000]={1,2,0};
    int h,t,k,n;
    int i,j;
    t=1,k=2;
    printf("Please input n:\n");
    scanf("%d",&n);
    while(t<n){
        h=0;
        for(i=0;i<=t;i++){
            for(j=0;j<i;j++){
                if(k==2*a[i]+3*a[j]||k==2*a[j]+3*a[i]){
                    a[++t]=k;
                    h=1;
                    break;
                }
            }
            if(h==1)
                break;
        }
        k++;
    }
    printf("(%d)=%d\n",n,a[n-1]);
}
