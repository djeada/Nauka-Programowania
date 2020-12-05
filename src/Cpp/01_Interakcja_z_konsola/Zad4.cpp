#include <iostream>
#include <cmath>

using namespace std;

/*
Wypisz wynik podstawowych operacji arytmetycznych 
dla dwoch liczb pobranych od uzytkownika.
*/

int main(){

	int x, y;
	cout << "Podaj dwie liczby: " << endl;
	cin >> x >> y;
	
	cout << "Suma " << x << " oraz " << y << " wynosi " << x + y << endl;
	cout << "Roznica " << x << " i " << y << " wynosi " << x - y << endl;
	cout << "Iloczyn " << x << " i " << y << " wynosi " << x * y << endl;
	cout << "Iloraz " << x << " przez " << y << " wynosi " << x / y << endl;
	cout << "Reszta z dzielenia " << x << " przez " << y << " wynosi " << x % y << endl;
	cout << x << " podniesione do " << y << " wynosi " << pow(x, y) << endl;

	return 0;
}
