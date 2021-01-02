#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

//Dla otrzymanej listy oraz liczby X, znajdz indeksy pierwszej 
//pary elementów listy, ktorych suma jest rowna liczbie X. 
//Jesli w liscie nie ma takiej pary, zwroc pare (-1, -1)

pair<int, int> sumaDwochV1(vector<int>& lista, int liczba) {
	int n = lista.size();

	for (int i = 0; i < n; i++) {
        		for (int j = i + 1; j < n; j++) {
		  	if (lista[j] + lista[i] == liczba)
				return pair<int, int>(i, j);
            	}
    	}

	return pair<int, int>(-1, -1);
}

int main() {
    	vector<int> lista({1, 3, 4, 5, 2});
	int liczba = 5;
	pair<int, int> wynik(0, 2);
	assert(sumaDwochV1(lista, liczba) == wynik);
	
	lista = {2, -6, 10, 21, 8};
	int liczba = 7;
	wynik = (-1, -1);
	assert(sumaDwochV1(lista, liczba) == wynik);

	return 0;
}
