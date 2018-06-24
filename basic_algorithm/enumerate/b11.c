#include<stdio.h>
void main(){
    int a,b,d,e,f,g;
    for(a=10;a<99;a++)
        for(b=a+1;b<99;b++){
            d=a/10;
            e=a%10;
            f=b/10;
            g=b%10;
            if(d==e || d==f || d==g || e==f || e==g || f==g)
                continue;
            if(d>e || d>f || d>g)
                continue;
            if((10*d+e)*(10*f+g)==(10*e+d)*(10*g+f))
                printf("%d%d x %d%d = %d%d x %d%d\n",d,e,f,g,e,d,g,f);
        }
}
