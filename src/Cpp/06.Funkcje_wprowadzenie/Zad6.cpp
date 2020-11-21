#include <cmath>
#include <iostream>

using namespace std;

//Napisz funkcje, ktora dla otrzymanej liczby zwroci sume cyfr tej liczby.

int sumaCyfr(int a) {
 	int suma = 0;
	
	while (a > 0) {
		suma += (a % 10);
		a /= 10;
	} 

	return suma;
}

int main() {
	cout << "Podaj liczbe: " << endl;
	int a;
	cin >> a;
	
	cout << "Suma cyfr liczby to: " << sumaCyfr(a) << endl;

	return 0;
}
