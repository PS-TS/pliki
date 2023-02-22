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

int * wnajw(int tabl[], int p) {
    
	int max = 0, maxi=0;
    
	for (int i = 0; i <= p; i++){
		for (int j = i; j < 20; j++){
            		if (tabl[j] > max){	//znajduje najwiekszy pole w tym przejściu tablicy
                		max = tabl[j];
                		maxi = j;
			}               
		}
		tabl[maxi] = tabl[i];   //zamiana
        	tabl[i] = max;
        	maxi = i+1;           //reset zmiennych
        	max = tabl[i+1];
    	}
    return tabl;		//wydanie konkretnego elementu
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
    
    wnajw(tab,n);
    for (int i = 0; i < n; i++)
    cout<<tab[i]<<endl;
}
