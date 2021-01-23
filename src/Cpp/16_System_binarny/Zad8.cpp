#include <cassert>

using namespace std;

//Znajdz potege dwojki wieksza badz rowna otrzymanej liczbie. 
//Inaczej: zaaokraglij liczbe do nastepnej potegi dwojki. 
//Dla otrzymanej liczby ujemnej zwroc 0.

int nastepnaPotegaDwojkiV1(int liczba) {
	if (liczba <= 0)
		return 0;
		
	if (liczba == 1)
		return 2;

	liczba--;

	while (liczba & liczba - 1)
		liczba &= liczba - 1;
		
	return liczba << 1;
}

int nastepnaPotegaDwojkiV2(int liczba) {
	if (liczba <= 0)
		return 0;
		
	int potega = 2;
	
	while (liczba > 2) {
		liczba >>= 1;
		potega <<= 1;
	}

	return potega;
}

void test1() {
	int liczba = 111;
	int wynik = 128;

	assert(nastepnaPotegaDwojkiV1(liczba) == wynik);
}

void test2() {
	int liczba = -30;
	int wynik = 0;

	assert(nastepnaPotegaDwojkiV1(liczba) == wynik);
}

void test3() {
	int liczba = 1;
	int wynik = 2;

	assert(nastepnaPotegaDwojkiV1(liczba) == wynik);
}

void test4() {
	int liczba = 111;
	int wynik = 128;

	assert(nastepnaPotegaDwojkiV2(liczba) == wynik);
}

void test5() {
	int liczba = -30;
	int wynik = 0;

	assert(nastepnaPotegaDwojkiV2(liczba) == wynik);
}

void test6() {
	int liczba = 1;
	int wynik = 2;

	assert(nastepnaPotegaDwojkiV2(liczba) == wynik);
}

int main() {

	test1();
	test2();
	test3();
	test4();
	test5();
	test6();

	return 0;
}

