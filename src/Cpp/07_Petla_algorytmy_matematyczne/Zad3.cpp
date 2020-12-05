#include <iostream>
#include <cassert>

using namespace std;

//Napisz funkcje, ktora dla otrzymanych dwoch liczb, 
//przy pomocy dodawania badz odejmowania oraz petli zrealizuje:

//a) mnozenie;
int mnozenie(int a, int b) {
	int wynik = 0;
	for (int i = 0; i < b; i++)
		wynik += a;

	return wynik;
}

//b) dzielenie
int dzielenie(int a, int b) {
	int wynik = 0;
	while (a >= b) {
		a -= b;
		wynik++;
	}

	return wynik;
}


int main () {

	int a = 2;
	int b = 3;

	int wynik = 6;
	assert(mnozenie(a, b) == wynik);

	a = 30;
	b = 6;

	wynik = 5;
	assert(dzielenie(a, b) == wynik);

	return 0;
}
