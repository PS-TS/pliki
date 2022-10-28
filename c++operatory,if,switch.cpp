#include <iostream>
#include <conio.h>
using namespace std;
int main()
{
    // unsigned int - dodatnie
    // int, long, long long - całkowite; float, double, long double - zmiennoprzecinkowe; char, string - znakowe;
    // >, <, >=, <=, ==, !=, &&, ||
    /*
    int i = 0;
    double o = 0;
    cout << "Wpisz rozmiar w cm: ";
    cin >> i;
    if (i > 0)
        o = i / 2.54;
    else
        cout << "Rozmiar musi byc wiekszy niz 0" << endl;
    cout << "Wynik "<<i<<"cm to: " << o <<" cali" << endl;
    */
    // porownywanie stringow t.compare("c")
    /*
    char t;
    double stopnie, w;
    cout << "f - farenheit, c - celsius: ";
    cin >> t;
    cout << "Podaj wartosc temperatury w stopniach "<<t<<": ";
    cin >> stopnie;
        if (t == 'f'){
            w = (stopnie - 32) * (5.0 / 9.0);
            cout << "Wynik: " << w << " stopni " << endl;}
        else if (t == 'c'){
            w = (stopnie * (9.0 / 5.0)) + 32;
            cout << "Wynik: " << w << " stopni " << endl;}
        else
            cout << "Blad" << endl;
    */
    ////////////////V1
    /*
    char l;
    cout << "Podaj wartosc: ";
    while (true) {
        l = _getch(); //pobieranie znaku bez konieczności wciskania ENTER, biblioteka <conio.h>
        switch (l) {
        case '1':                     //to jest znak typu char, a nie liczba typu int (pojedyncze apostrofy)
            cout << l << " - Jeden";
            break;
        case '2':
            cout << l << " - Dwa";
            break;
        case '3':
            cout << l << " - Trzy";
            break;
        case '4':
            cout << l << " - Cztery";
            break;
        case '5':
            cout << l << " - Piec";
            break;
        case '6':
            cout << l << " - Szesc";
            break;
        case '7':
            cout << l << " - Siedem";
            break;
        case '8':
            cout << l << " - Osiem";
            break;
        case '9':
            cout << l << " - Dziewiec";
            break;
        default:                      //wartość w przypadku niespełnienia żadnego powyższego warunku
            cout << "Poza zakresem";
            break;
        }
        cout << endl << "Podaj wartosc: " ;
    }*/
    ////////////////////V2
    string tab[9] = { "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec" };
    int a = 0;
    cout << "Podaj: ";
    cin >> a;
    if (a > 0 && a <= 9) //jeśli a>0 i a<=9
        cout << "Wynik: " << tab[a - 1] << endl; //tablica 10 elementowa ma numery 0-9 czyli pierwszy element to tab[0] a ostatni tab[9]
    else
        cout << "Poza zakresem"<<endl;
}
