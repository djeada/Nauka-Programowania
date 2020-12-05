#include <iostream>

using namespace std;

//Napisz funkcje, ktora dla otrzymanej liczby n,
//poprosi uzytkownika o podanie n liczb i zwroci
//ich srednia arytmetyczna

float srednia(int n) {
	
	float suma = 0.0;
	int x;

	for (int i = 0; i < n; i++) {
		cout << "Podaj liczbe: " << endl;
		cin >> x;
		suma += x;
	}

	return suma/n;
}

int main () {

	cout << "Podaj liczbe n: " << endl;
	int n;
	cin >> n;
	
	float wynik = srednia(n);

	cout << "Srednia z podanych liczb to " << wynik << endl;

	return 0;
}
