#include <iostream>
using namespace std;

int funkcja(int n, int m, int tab[]);

int main()
{
    int tab1[] = { 1, 4, 10, 5, 7, 6, 11 };
    cout << funkcja(7,4,tab1) << endl;

    int tab2[] = { 2, 5, 8, 14, 21, 3 };
    cout << funkcja(6, 2, tab2);
}


int funkcja(int n, int m, int tab[])
{
    int liczba_el = 0;
    for (int i = 0; i < n; i++)
    {
        if (tab[i] <= 2 * m)
        {
            liczba_el++;
        }
    }
    return liczba_el;
}
