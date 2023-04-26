#include <stdio.h>
#include <stdlib.h>
void wytnij(char* text, int n, int m)
{
    int a=0;
    while(text[a]!=0)
    {
        a++;
    }
    int i,j;
    for(i=n,j=m+1;j<=a;++j,++i)
    {
        text[i]=text[j];
    }
    text[i]='\0';
}
int main()
{
    char a[]="Jestem Koxem 123";
    wytnij(a,4,7);
    printf("%s\n",a);
    return 0;
}
