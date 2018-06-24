#include<stdio.h>
#include<math.h>
void main(){
    double a3[100]={-1};
    double x[200]={0};
    double y;
    int i=4,j,index=0;
    long m,n;
    double flag;
    double tmp;
    for(j=0;j<100;j++)
        a3[j]=-1;
    x[1]=1;x[2]=2;x[3]=3;
    a3[0]=1;a3[1]=0;
    printf("Please input n:");
    scanf("%ld",&n);
    printf("Please input m:");
    scanf("%ld",&m);
    do{
        flag=1e10;
        for(j=0;j<100;j++){
            tmp=pow(3,j)*pow(2,a3[j]+1);
            if(tmp<flag){
                flag=tmp;
                index=j;
            }
        }
        a3[index]++;
        x[i++]=flag;
        printf("x[%d]=%lf\n",i-1,x[i-1]);
    }while(x[i-1]<n);
    printf("%d\n%lf\n",i-2,x[m]);
}
