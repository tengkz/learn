#include<stdio.h>
#include<math.h>
int isSu(int x)
{
    if(x==1)
        return 1;
    if(x==2)
        return -1;
    int y=(int)sqrt(x*1.0)+1;
    int i=2;
    for(i=2;i<=y;i++)
    {
        if(x%i==0)
            return 1;
    }
    return -1;
}
void main()
{
    int i,j;
    int maxi,mini;
    double s=0,maxs=0,mins=1e10;
    int n;
    printf("Please input n:");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        if(isSu(2*i-1)*isSu(2*i+1)==-1)
            s+=(2.0*i-1)/(2.0*i+1);
        else
            s-=(2.0*i-1)/(2.0*i+1);
        if(s>maxs)
        {
            maxs=s;
            maxi=i;
        }
        if(fabs(s)<mins)
        {
            mins=fabs(s);
            mini=i;
        }
    }
    printf("%.5lf\n",s);
    printf("%d,%lf\n",maxi,maxs);
    printf("%d,%lf\n",mini,mins);
}

