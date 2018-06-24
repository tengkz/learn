#include<stdio.h>
#include<math.h>
void main()
{
    int A1[1001]={1,2,0};
    int A2[1001]={2,4,0};
    int A3[1001]={3,6,0};
    int B[1001]={0};
    int i=1,j=1,k;
    int index=1,flag=1,pre=-1;
    while(1){
        for(i=0;i<=pre;i++)
            for(j=pre+1;j<=flag;j++){
                if(i==j)
                    continue;
                A1[++index]=A2[i]+A3[j];
                A2[index]=2*A1[index];
                A3[index]=3*A1[index];
            }
        for(j=0;j<=pre;j++)
            for(i=pre+1;i<=flag;i++){
                if(i==j)
                    continue;
                A1[++index]=A2[i]+A3[j];
                A2[index]=2*A1[index];
                A3[index]=3*A1[index];
            }
        for(i=pre+1;i<=flag;i++)
            for(j=pre+1;j<=flag;j++){
                if(i==j)
                    continue;
                A1[++index]=A2[i]+A3[j];
                A2[index]=2*A1[index];
                A3[index]=3*A1[index];
            }
        pre=flag;
        flag=index;
        if(index>100)
            break;
    }
    for(i=index;i>=0;i--)
        for(j=0;j<i;j++){
            if(A1[j]>A1[j+1]){
                k=A1[j];
                A1[j]=A1[j+1];
                A1[j+1]=k;
            }
        }
    B[0]=A1[0];
    for(i=1,j=1;i<=index;i++){
        if(A1[i-1]!=A1[i])
            B[j++]=A1[i];
        else
            continue;
    }
    for(i=0;i<100;i++)
        printf("%d,",B[i]);
    printf("\n");
}
