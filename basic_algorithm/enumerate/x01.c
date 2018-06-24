#include<stdio.h>
#include<math.h>
void main(){
    double i=1,s=0,e=0;
    int i1,i2;
    while(1){
        e+=1.0/i;
        s+=1.0/e;
        if(s>2010){
            i1=(int)i;
            break;
        }
        i++;
    }
    if(s>=2011){
        i2=0;
    }
    else{
        while(1){
            e+=1.0/i;
            s+=1.0/e;
            if(s>=2011){
                i2=(int)i;
                break;
            }
            i++;
        }
    }
    printf("%d,%d\n",i1,i2-1);
}
