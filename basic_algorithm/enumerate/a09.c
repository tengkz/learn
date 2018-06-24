#include<stdio.h>
#include<math.h>
void main()
{
    int a,b,c,e,d,f,s;
    int flag=0;
    double x,y;
    s=12;
    while(s<=92)
    {
        for(a=1;a<s/3;a++){
            for(b=a+1;b<s/2;b++){
                c=s-a-b;
                if(c<=b)
                    continue;
                for(d=a+1;d<s/3;d++){
                    if(d==b||d==c)
                        continue;
                    for(e=d+1;e<s;e++){
                        if(e==b||e==c)
                            continue;
                        f=s-d-e;
                        if(f==a||f==b||f==c||f<=e)
                            continue;
                        x=s*1.0/a+s*1.0/b+s*1.0/c;
                        y=s*1.0/d+s*1.0/e+s*1.0/f;
                        if(x==y){
                            printf("%d,%d,%d,%d,%d,%d\n%d\n",a,b,c,d,e,f,s);
                        }
                    }
                }
            }
        }
        s+=1;
    }
}
