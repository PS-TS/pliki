#include <iostream>
using namespace std;

void funkcja(int a, int b, int c);

int main()
{
    int a, b, c;
    cout << "Podaj kolejno 3 liczby calkowite: " << endl;
    cin >> a;
    cin >> b;
    cin >> c;

    funkcja(a, b, c);

    return 0;
}

void funkcja(int a, int b, int c)
{
    int srednia = (b + c) / 2;
    if (a > srednia)
    {
        cout << "Liczba a jest wieksza niz srednia z liczb b i c." << endl;
    }
    else
    {
        cout << "Liczba a jest NIE wieksza niz srednia z liczb b i c." << endl;
    }
}
