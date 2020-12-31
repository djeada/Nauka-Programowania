#include <vector>
#include <iostream>

using namespace std;

//Dla liczby N, wczytaj N liczb do listy, a nastepnie:
void wczytaj(vector<int>& lista, int n) {
	for (int i = 0; i < n; i++) {
		int liczba;
		cin >> liczba;
		lista.push_back(liczba);
	}
}

//a)dodaj do kazdego elementu 1;
void zwieksz(vector<int>& lista) {
	for (auto& liczba : lista)
		liczba += 1;
}

//b)pomnoz kazdy element przez jego indeks;
void pomnoz(vector<int>& lista) {
	for (int i = 0; i < lista.size(); i++)
		lista[i] *= i;
}

//c)zastap wszystkie elementy wartoscia pierwszego elementu listy.
void zastap(vector<int>& lista) {
	if (lista.empty())
		return;

	for (auto& liczba : lista)
		liczba = lista[0];
}

//Dla każdego podpunktu wypisz zmodyfikowaną listę. Elementy listy powinny 
//być oddzielone przecinkami i wypisane w jednym wierszu.
void wypiszOdKonca(vector<int>& lista) {
	for (auto liczba : lista)
		cout << liczba << ", ";
	cout << endl;
}

int main() {

	vector<int> lista;
	int n;
	
	cout << "podaj liczbe n: ";
	cin >> n;
	wczytaj(lista, n);	

	vector<int> kopia(lista);
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

