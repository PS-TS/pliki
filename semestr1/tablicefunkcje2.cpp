#include <iostream>
using namespace std;

int parz(int tabl[]) {
    int wynik = 0;
    for (int i = 0; i < 20; i++){
        if(tabl[i]%2==0)
        wynik ++;
    }
    return wynik;
}

int main()
{
    int tab[20];
    srand(time(NULL));
    for (int i = 0; i < 20; i++){
        tab[i] = rand() % 101;
    }
    cout<<parz(tab);
}

