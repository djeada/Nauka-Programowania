#include <iostream>
#include <cassert>

using namespace std;

//Napisz funkcje, ktora przy pomocy petli obliczy silnie
//z otrzymanej liczby.

int silnia(int a) {

	int wynik = 1;

	while (a > 0) {
		wynik *= a;
		a--;	
	}

	return wynik;
}

int main () {

	int a = 4;
	int wynik = 24;
	assert(silnia(a) == wynik);

	return 0;
}
