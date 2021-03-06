#include<stdio.h>
void quicksort(int a[],int l,int r)
{
    if(l<r)
    {
        int x = a[l];
        int i=l,j=r;
        while(i<j)
        {
            while(i<j && a[j]>=x)
                j--;
            if(i<j)
                a[i++] = a[j];
            while(i<j && a[i]<x)
                i++;
            if(i<j)
                a[j--] = a[i];
        }
        a[i] = x;
        quicksort(a,l,i-1);
        quicksort(a,i+1,r);
    }
}
int main()
{
    int a[100]={3,2,8,5,4,6,9,1,7,0};
    quicksort(a,0,9);
    int i;
    for(i=0;i<10;i++)
    {
        printf("%d ",a[i]);
    }
    return 0;
}
