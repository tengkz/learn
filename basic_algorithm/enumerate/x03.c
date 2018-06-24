#include<stdio.h>
#include<math.h>
int su(int x){
    if(x<=1)    return 0;
    if(x==2)    return 1;
    int s=(int)sqrt(x);
    int i;
    for(i=2;i<=s;i++){
        if(x%i==0)
            return 0;
    }
    return 1;
}
void main(){
    int n,i,m;
    printf("Please input n:\n");
    scanf("%d",&n);
    m=n;
    printf("%d=",n);
    for(i=2;i<=n/2;i++){
        if(su(i)){
            while(m%i==0){
                printf("%d",i);
                m/=i;
                if(m>1)
                    printf("X");
            }
        }
    }
    if(m>1){
        printf("%d is su!",n);
    }
    printf("\n");
}
