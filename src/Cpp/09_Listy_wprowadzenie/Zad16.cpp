#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

/*
Znajdz takie pary elementow w liscie, ktorych suma jest rowna liczbie.
Element nie moze byc w parze sam ze soba.
*/

vector<pair<int, int>> znajdzParyV1(vector<int>& lista, int suma) {
	
	vector<pair<int, int>> wynik;
	 
	for (int i = 0; i < lista.size(); i++) {
		for (int j = i + 1; j < lista.size(); j++) {
			if (lista[i] + lista[j] == suma)
				wynik.emplace_back(lista[i], lista[j]);
		}
	}

    return wynik;
}

int main() {
	vector<int> lista {0, 4, 5, 6, 2, 9, 2, 3};
	vector<pair<int, int>> wynik {{0, 5}, {2, 3}, {2, 3}};
	int suma = 5;

	assert( znajdzParyV1(lista, suma) == wynik);

	return 0;
}

