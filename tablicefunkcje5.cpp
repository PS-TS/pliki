#include <iostream>
#include <cstdlib>
#include <time.h>
#include <string>
using namespace std;

int fun1(string str){
	int x = 0;
	for(int i = 0; i<str.length();i++)
		if(str[i] >= 'a' && str[i] <= 'z')
			x++;
	return x;
}
int fun2(string str){
	int x = 0;
	for(int i = 0; i<str.length();i++)
		if(!(str[i] >= 'a' && str[i] <= 'z') && !(str[i] >='A' && str[i] <='Z'))
			x++;
	return x;;
}

int main(){
	string tekst;
	cout<<"Napisz cos: ";
	getline(cin, tekst);
	cout<<"Male litery: "<<fun1(tekst)<<endl;
	cout<<"Inne znaki (spacje tez liczy): "<<fun2(tekst)<<endl;
}
