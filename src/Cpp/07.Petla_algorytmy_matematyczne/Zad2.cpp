#include <iostream>
#include <cassert>

using namespace std;

int potega(int a, int b) {
	int wynik = 1;
	for (int i = 0; i < b; i++)
		wynik *= a;

	return wynik;
}

int main () {

	int a = 2;
	int b = 3;
	int wynik = 8;

	assert (potega(a, b) == wynik);

	return 0;
}
