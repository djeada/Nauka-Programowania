#include <iostream>

using namespace std;

int main() {

	//Dla pobranej liczby, wyswietl liczbe Pi tyle razy 
	//ile wynosi pobrana liczba, z dokladnoscia do tylu 
	//miejsc po przecinku ile wynosi pobrana liczba.
	
	cout << "Podaj liczbe" << endl;
	int a;
	cin >> a;
	
	int suma = 0;

	while (a > 0) {
		suma += (a % 10);
		a = a / 10; 
	}

	cout << "Suma cyfr podanej liczby wynosi " << suma << endl;

	return 0;
}
