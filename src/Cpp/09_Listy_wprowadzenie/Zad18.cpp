#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

//Dla otrzymanej listy znajdz indeks najmniejszego elementu. 
//Lista jest posortowana rosnaco, ale zostala przesunieta.
//Przykladowo przez przesuniecie w prawo o 1 rozumiemy, ze 
//ostatni element trafi na miejsce pierwszego, pierwszy drugiego, itd.

int indeksMin(vector<int>& lista) {
	int n = lista.size();

	for (int i = 0; i < n - 1; i++) {
        		if (lista[i] > lista[i + 1])
			return i + 1;
    	}

	return 0;
}

int main() {
    	vector<int> lista({7, 8, -1, 4, 5});
	int wynik = 2;
	assert(indeksMin(lista) == wynik);
	
	lista = {2, 3, 4, 5, 6};
	wynik = 0;
	assert(indeksMin(lista) == wynik);

	lista = {8, 9, 10, 11, 1};
	wynik = 4;
	assert(indeksMin(lista) == wynik);

	return 0;
}
