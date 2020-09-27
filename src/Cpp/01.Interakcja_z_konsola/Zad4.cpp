#include <iostream>
#include <cmath>

using namespace std;

int main(){
	/*
	Wypisz wynik podstawowych operacji arytmetycznych 
	dla dwoch liczb pobranych od uzytkownika.
	*/
	
	int x, y;
	cin >> x >> y;
	
	cout << x+y << endl;
	cout << x-y << endl;
	cout << x*y << endl;
	cout << x/y << endl;
	cout << x%y << endl;
	cout << pow(x, y);

	return 0;
}
