#include <iostream>
#include<vector>
using namespace std;

int main()
{
    vector<int>wektor;
    int liczba;
    cout << "Podaj kolejno 5 liczb calkowitych: " << endl;

    for (int i = 0; i < 5; i++)
    {
        cin >> liczba;
        wektor.push_back(liczba);
    }

    vector<int>wektor2;
    for (int i = wektor.size(); i > 0; i--)
    {
        wektor2.push_back(wektor[i-1]);
    }
    return 0;
}
