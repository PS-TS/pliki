#include <stdio.h>
#include <stdlib.h>
void przepisz(char* text1, char* text2)
{
    int i=0;
    while(text1[i]!='\0')
    {
        text2[i]=text1[i];
        i++;
    }
    text2[i]='\0';
}
int main()
{
    char a[]="Ala";
    char b[20];
    przepisz(a,b);
    printf("%s",b);

    return 0;
}
