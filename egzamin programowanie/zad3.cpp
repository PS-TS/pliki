#include <iostream>
using namespace std;

int funkcja(int n);

int main()
{
    cout << funkcja(5);
}

int funkcja(int n)
{
    int liczba = 0;
    for (int i = 0; i < n; i++)
    {
        if (liczba >= 0)
        {
            liczba += 3;
            liczba *= -1;
        }
        else
        {
            liczba -= 3;
            liczba *= -1;
        }
    }
    return liczba;
}