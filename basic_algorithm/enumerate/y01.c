#include<stdio.h>
#include<math.h>
void main(){
    double i=1,s=0,e=0;
    do{
        e+=1.0/i;
        s+=1.0/e;
        i++;
    }while(s<=2010);
    printf("%d,",(int)(i-1));
    do{
        e+=1.0/i;
        s+=1.0/e;
        i++;
    }while(s<2011);
    printf("%d\n",(int)(i-2));
}
