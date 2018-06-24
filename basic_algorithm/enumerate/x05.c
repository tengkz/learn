#include<stdio.h>
#include<math.h>
void main(){
    int a,b,c,d,e,f,g;
    int s;
    int t;
    for(a=2;a<=9;a++)
        for(b=2;b<=9;b++){
            if(a==b)    continue;
            for(c=2;c<=9;c++){
                if(c==a||c==b)  continue;
                for(d=2;d<=9;d++){
                    if(d==a||d==b||d==c)    continue;
                    for(e=2;e<=9;e++){
                        if(e==a||e==b||e==c||e==d)  continue;
                        for(f=2;f<=9;f++){
                            if(f==a||f==b||f==c||f==d||f==e)    continue;
                            for(g=2;g<=9;g++){
                                if(g==a||g==b||g==c||g==d||g==e||g==f)  continue;
                                s=1e6*a+1e5*b+1e4*c+1e3*d+1e2*e+1e1*f+g;
                                t=(int)sqrt(s);
                                if(t*t==s)
                                    printf("%d\n",s);
                            }
                        }
                    }
                }
            }
        }
}
