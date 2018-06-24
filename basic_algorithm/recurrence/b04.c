#include<stdio.h>
void main(){
    int i,m,u,p;
    double n,h,f[1000],q[100];
    printf("Please input n:");
    scanf("%lf",&n);
    printf("Please input m:");
    scanf("%d",&m);
    u=1;f[1]=1.0;
    p=0;q[0]=1.0;
    while(1){
        if(q[p]<=f[u]){
            q[p+1]=q[p]*3;
            p++;
        }
        h=q[p];
        for(i=0;i<p;i++){
            if(q[i]<=f[u])   q[i]*=2;
            if(h>q[i])  h=q[i];
        }
        if(h>n) break;
        f[++u]=h;
    }
    printf("%d\n%lf\n",u,f[m]);
}
