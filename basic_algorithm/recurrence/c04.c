#include<stdio.h>
void main(){
    double f[1000],q[100],n,h;
    int u,p,m,i;
    printf("Please input n:");
    scanf("%lf",&n);
    printf("Please input m:");
    scanf("%d",&m);
    u=1;f[u]=1.0;
    p=0;q[p]=1.0;
    while(1){
        printf("p=%d,u=%d,f[%d]=%.0lf\n",p,u,f[u]);
        if(q[p]<=f[u]){
            p++;
            q[p]=q[p-1]*3;
        }
        h=q[p];
        for(i=0;i<p;i++){
            if(q[i]<=f[u]){
                q[i]*=2;
            }
            if(h>q[i]){
                h=q[i];
            }
        }
        if(h>n) break;
        u++;
        f[u]=h;
    }
    printf("%d\n%.0lf\n",u,f[m]);
}
