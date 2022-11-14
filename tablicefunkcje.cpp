#include <iostream>
using namespace std;

int suma(int tabl[]) {
    int wynik = 0;
    for (int i = 0; i < 20; i++){
        wynik += tabl[i];
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
    cout<<suma(tab);
}

