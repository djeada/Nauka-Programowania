#include <iostream>
using namespace std;

int main() {

	//Dla pobranej liczby, powinna zostac wyswietlona suma 
	//wszystkich liczb naturalnych mniejszych od pobranej liczby.
	
	cout << "Podaj liczbe: " << endl;
	int n;
	cin >> n;

	int suma = 0;
	
	for (int i = 1; i < n; i++)
		suma += i;

	cout << suma << endl;

	return 0;
}
