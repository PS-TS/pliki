#include <iostream>
#include <windows.h>
#include <ctime>
using namespace std;

int najw(int tabl[]) {
    int wynik = 0;
    for (int i = 0; i < 20; i++){
        if(tabl[i]>wynik)
        wynik = tabl[i];
    }
    return wynik;
}

int wnajw(int tabl[], int x, int p) {
    
	int max = 0, maxi=0, zmiana;
    
	for (int i = 0; i < x; i++){
        
		for (int j = i; j < 20; j++)
            if (tabl[j] > max){
                max = tabl[j];
                maxi = j;
			}               	//najwiekszy pole w tym przejœciu tablicy
        
		tabl[maxi] = tabl[i];   //zamiana
        tabl[i] = max;
        maxi = i+1;           //reset zmiennych
        max = tabl[i+1];
    }
    return tabl[p];		//wydanie konkretnego elementu
}

int main()
{
    int tab[20];
    int n = 0;
    srand(time(NULL));
    for (int i = 0; i < 20; i++){
        tab[i] = rand() % 101;
    }
    cout << "Podaj liczbe do wydania: ";
    cin >> n;
    cout<<"a) \nNajwieksza: " << najw(tab) << endl << "b) "<< endl;
    
    //funkcja wykonuje sie tyle razy ile potrzeba najwiekszych liczb
    
    for (int i = 0; i < n; i++)
    cout<<wnajw(tab, n, i)<<endl;
}
