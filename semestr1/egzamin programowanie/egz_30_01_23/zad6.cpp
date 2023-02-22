#include <iostream>
using namespace std;

int funkcja(int n);

int main()
{
    cout << funkcja(4)<< endl;
    cout << funkcja(5);
}

int funkcja(int n)
{
    if (n == 0)
    {
        return 1;
    }
    if (n == 1)
    {
        return 2;
    }
    if (n % 2 == 0)
    {
        return funkcja(n/2) + 2;
    }
    return 2 * funkcja(n - 2);
}
