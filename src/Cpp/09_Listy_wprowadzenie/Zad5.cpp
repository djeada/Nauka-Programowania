#include <vector>
#include <cassert>
#include <cmath>
#include <numeric>

using namespace std;

//Otrzymujesz liste liczb, wykonaj nastepujace polecenia:

//a)Zwieksz o 1 wszystkie elementy stojace na parzystych indeksach.
void zwieksz(vector<int>& lista) {
	
	for (int i = 0; i < lista.size(); i++) {
		if (i % 2 == 0)
			lista[i]++;
	}
}

//b)Wyzeruj wszystkie wielokrotnosci liczby 3.
void wyzeruj(vector<int>& lista) {
	
	for (auto& liczba : lista) {
		if (liczba % 3 == 0)
			liczba = 0;
	}
}

//c)Podnies do kwadratu wszystkie elementy mniejsze niz 10.
void kwadrat(vector<int>& lista) {
	
	for (auto& liczba : lista) {
		if (liczba < 10)
			liczba = pow(liczba, 2);
	}
}

//d)Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami pierwszymi.
int czyPierwsza(int n) {

	if ((!(n % 2) && n != 2) || n < 1)
		return false;
	
	for (int i = 3; i <= sqrt((double)n); i += 2) {
		if (!(n % i))
			return false;
	}
	
	return true;
}

void suma(vector<int>& lista) {
	int suma = accumulate(lista.begin(), lista.end(), 0);
	
	for (int i = 0; i < lista.size(); i++) {
		if (czyPierwsza(i))
			lista[i] = suma;
	}
}

//e)Zamien kazdy element na iloczyn wszystkich elementow list poza nim samym.

void zamien(vector<int>& lista) {

	vector<int> iloczyny;

	for (int i = 0; i < lista.size(); i++) {
		int iloczyn = 1;

		for (int j = 0; j < lista.size(); j++) {
			if (j == i) continue;

			iloczyn *= lista[j];
		}
		
		iloczyny.push_back(iloczyn);
	}

	lista = iloczyny;
}

int main() {

    	vector<int> lista({3, 5, -7, 4, 9, -11, 2});
	vector<int> kopia(lista);
	vector<int> wynik({4, 5, -6, 4, 10, -11, 3}); 
    	zwieksz(kopia);
	assert(kopia == wynik);

	kopia = lista;
	wynik = {0, 5, -7, 4, 0, -11, 2};
	wyzeruj(kopia);
	assert(kopia == wynik);
   	
	kopia = lista;
	wynik = {9, 25, 49, 16, 81, 121, 4}; 
	kwadrat(kopia);
	assert(kopia == wynik);

	kopia = lista;
	wynik = {3, 5, 5, 5, 9, 5, 2};
	suma(kopia);
	assert(kopia == wynik);

	kopia = lista;
	wynik = {27720, 16632, -11880, 20790, 9240, -7560, 41580};
	zamien(kopia);
	assert(kopia == wynik);

	return 0;
}

