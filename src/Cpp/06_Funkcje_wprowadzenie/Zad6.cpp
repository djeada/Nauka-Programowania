#include <cmath>
#include <cassert>

//Napisz funkcje, ktora dla otrzymanej liczby zwroci sume cyfr tej liczby.

int sumaCyfr(int a) {
 	int suma = 0;
	
	while (a > 0) {
		suma += (a % 10);
		a /= 10;
	} 

	return suma;
}

void test1() {
	int a = 312423;
	int wynik = 15;
	
	assert(sumaCyfr(a) == wynik);
}

void test2() {
	int a = 5;
	int wynik = 5;
	
	assert(sumaCyfr(a) == wynik);
}

int main() {
	test1();
	test2();

	return 0;
}
