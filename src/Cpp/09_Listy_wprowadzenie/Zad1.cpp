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

//a) wypisz liste od poczatku do konca. Elementy listy powinny 
//znajdowac sie w osobnych wierszach.
void wypiszOdPoczatku(vector<int>& lista) {
	for (auto liczba : lista)
		cout << liczba << endl;
}

//b) wypisz liste od konca. Elementy listy powinny byc oddzielone 
//przecinkami i wypisane w jednym wierszu.
void wypiszOdKonca(vector<int>& lista) {
	auto it = cend(lista);
    	while (it != cbegin(lista))
        		cout << *(--it) << ", ";

	cout << endl;
}

int main() {

	vector<int> lista;
	int n;
	
	cout << "podaj liczbe n: ";
	cin >> n;
	wczytaj(lista, n);	
	wypiszOdPoczatku(lista);
	wypiszOdKonca(lista);

	return 0;
}

