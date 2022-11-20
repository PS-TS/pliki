#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;

void fun1(int tab1[], int tab2[], int tab3[]){
	for(int i=0;i<20;i++){
		cout<<tab1[i]<<" "<<tab2[i]<<" "<<tab3[i]<<endl;
		if(tab1[i]==tab2[i]||tab3[i]==tab2[i]||tab1[i]==tab3[i])
		cout<<"Indeks "<<i<<" zawiera przynajmniej 2 identyczne wartosci"<<endl;
	}
	
}
void fun2(int tab1[], int tab2[], int tab3[]){
	for(int i=0;i<20;i++){
		if(tab1[i]==tab2[i]&&tab1[i]==tab3[i])
		cout<<"Indeks "<<i<<" zawiera 3 identyczne wartosci"<<endl;
	}
	
}
void fun3(int tab1[], int tab2[], int tab3[]){
	for(int i=0;i<20;i++){
		if(tab1[i]!=tab2[i]&&tab2[i]!=tab3[i]&&tab1[i]!=tab3[i])
		cout<<"Indeks "<<i<<" zawiera 3 rozne wartosci"<<endl;
	}
	
}

int main(){
	srand(time(NULL));
	int tab1[20], tab2[20], tab3[20];
	for(int i=0;i<20;i++){
		tab1[i] = rand()%4;
		tab2[i] = rand()%4;
		tab3[i] = rand()%4;
	}
	fun1(tab1,tab2,tab3);
	cout<<endl;
	fun2(tab1,tab2,tab3);
	cout<<endl;
	fun3(tab1,tab2,tab3);
}
