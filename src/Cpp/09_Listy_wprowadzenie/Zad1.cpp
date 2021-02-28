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

//a) wypisz liste od poczatku do konca. Elementy listy powinny 
//znajdowac sie w osobnych wierszach.
void wypiszOdPoczatku(std::vector<int>& lista) {
	for (auto liczba : lista)
		std::cout << liczba << std::endl;
}

//b) wypisz liste od konca. Elementy listy powinny byc oddzielone 
//przecinkami i wypisane w jednym wierszu.
void wypiszOdKonca(std::vector<int>& lista) {
	auto it = cend(lista);
    	while (it != cbegin(lista))
        		std::cout << *(--it) << ", ";

	std::cout << std::endl;
}

int main() {

	std::vector<int> lista;
	int n;
	
	std::cout << "podaj liczbe n: ";
	std::cin >> n;
	wczytaj(lista, n);	
	wypiszOdPoczatku(lista);
	wypiszOdKonca(lista);

	return 0;
}

