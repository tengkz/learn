#include<stdio.h>
void main()
{
    int d,e,f,g;
    for(d=1;d<=9;d++)
        for(e=1;e<=9;e++)
            for(f=1;f<=9;f++)
                for(g=1;g<=9;g++){
                    if(d==e||d==f||d==g||e==f||e==g||f==g)
                        continue;
                    else{
                        if(((10*d+e)*(10*f+g))==((10*e+d)*(10*g+f)))
                            printf("%d%d * %d%d = %d%d * %d%d\n",d,e,f,g,e,d,g,f);
                    }
                }
}
