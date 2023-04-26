#include <stdio.h>
#include <stdlib.h>
int dlugosc(char* text)
{
    int a=0;
    while(text[a]!=0)
    {
        a++;
    }
    return a;
}
int main()
{
    printf("%d\n",dlugosc("wasrswe"));
    return 0;
}
