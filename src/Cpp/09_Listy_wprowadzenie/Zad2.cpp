#include <vector>
#include <iostream>

//Dla liczby N, wczytaj N liczb do listy, a nastepnie:
void wczytaj(std::vector<int>& lista, int n) {
	for (int i = 0; i < n; i++) {
		int liczba;
		std::cin >> liczba;
		lista.push_back(liczba);
	}
}

//a)dodaj do kazdego elementu 1;
void zwieksz(std::vector<int>& lista) {
	for (auto& liczba : lista)
		liczba += 1;
}

//b)pomnoz kazdy element przez jego indeks;
void pomnoz(std::vector<int>& lista) {
	for (unsigned int i = 0; i < lista.size(); i++)
		lista[i] *= i;
}

//c)zastap wszystkie elementy wartoscia pierwszego elementu listy.
void zastap(std::vector<int>& lista) {
	if (lista.empty())
		return;

	for (auto& liczba : lista)
		liczba = lista[0];
}

//Dla każdego podpunktu wypisz zmodyfikowaną listę. Elementy listy powinny 
//być oddzielone przecinkami i wypisane w jednym wierszu.
void wypiszOdKonca(std::vector<int>& lista) {
	for (auto liczba : lista)
		std::cout << liczba << ", ";
	std::cout << std::endl;
}

int main() {

	std::vector<int> lista;
	int n;
	
	std::cout << "podaj liczbe n: ";
	std::cin >> n;
	wczytaj(lista, n);	

	std::vector<int> kopia(lista);
	zwieksz(kopia);
	wypiszOdKonca(kopia);	

	kopia = lista;
	pomnoz(kopia);
	wypiszOdKonca(kopia);	

	kopia = lista;
	zastap(kopia);
	wypiszOdKonca(kopia);	

	return 0;
}

