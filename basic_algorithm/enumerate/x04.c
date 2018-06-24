#include<stdio.h>
#include<math.h>
int su(int x){
    if(x<=1)    return 0;
    if(x==2)    return 1;
    int s=(int)sqrt(x);
    int i;
    for(i=2;i<=s;i++)
        if(x%i==0)
            return 0;
    return 1;
}
void main(){
    long s;
    int i;
    long m1=1e10,m2=0;
    for(i=1;i<=2011;i++){
        if(su(2*i-1)+su(2*i+1))
            s+=(2*i-1)*(2*i+1);
        else
            s-=(2*i-1)*(2*i+1);
        if(s>m2)
            m2=s;
        if(s<m1)
            m1=s;
    }
    printf("s(2011)=%d,max(s)=%d,min(s)=%d\n",s,m2,m1);
}
