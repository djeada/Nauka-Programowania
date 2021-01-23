#include <cassert>
#include <vector>
#include <math.h>
using namespace std;

//Policz z ilu zer i jedynek sklada sie otrzymana liczba.

int policzUstawioneBity(int liczba) {
    int suma = 0;
    while (liczba > 0) {
        if (liczba & 1)
            suma++;
        liczba >>= 1;
	}

    return suma;
}

void przygotujTablice(vector<int>& tablica) {

	tablica.clear();

	for (int i = 0; i < 256; i++)
		tablica.push_back(policzUstawioneBity(i));
}

int liczbaBitow(int liczba) {
	return (int)log2(liczba) + 1; 
}

int zera(int liczba, vector<int>& tablica) {
	return liczbaBitow(liczba) - tablica[liczba & 0xff] + tablica[(liczba >> 8) & 0xff] + tablica[(liczba >> 16) & 0xff] + tablica[(liczba >> 24) & 0xff];
}

int jedynki(int liczba, vector<int>& tablica) {
	return tablica[liczba & 0xff] + tablica[(liczba >> 8) & 0xff] + tablica[(liczba >> 16) & 0xff] + tablica[(liczba >> 24) & 0xff];
}

void test1(vector<int>& tablica) {
	int liczba = 10;
	int wynik = 2;

	assert(jedynki(liczba, tablica) == wynik);
}

void test2(vector<int>& tablica) {
	int liczba = 7;
	int wynik = 3;

	assert(jedynki(liczba, tablica) == wynik);
}

void test3(vector<int>& tablica) {
	int liczba = 10;
	int wynik = 2;

	assert(zera(liczba, tablica) == wynik);
}

void test4(vector<int>& tablica) {
	int liczba = 7;
	int wynik = 0;

	assert(zera(liczba, tablica) == wynik);
}

int main() {

	vector<int> tablica;
	przygotujTablice(tablica);
	
	test1(tablica);
	test2(tablica);
	test3(tablica);
	test4(tablica);

	return 0;
}

