#include <stdio.h>
#include <stdlib.h>
void przepisz(char* text1, char* text2, char* text3)
{
    int i=0,j=0;
    while(text1[i]!='\0')
    {
        text3[i]=text1[i];
        i++;
    }
    while(text2[j]!='\0')
    {
        text3[i]=text2[j];
        i++;
        j++;
    }

    text3[i]='\0';
}
int main()
{
    char a[]="Ala m";
    char b[]="a kota";
    char c[20];
    przepisz(a,b,c);
    printf("%s",c);

    return 0;
}
