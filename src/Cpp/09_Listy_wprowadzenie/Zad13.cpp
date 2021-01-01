#include <vector>
#include <cassert>
#include <algorithm>
#include <numeric>

using namespace std;

//Dla otrzymanej listy, skladajacej się z nieuporzadkowanych 
//kolejnych (za wyjatkiem jednego) wyrazow ciagu arytmetycznego, 
//znajdz brakujacy element.

int sumaCiaguArt(vector<int>& lista) {
	int min = *min_element(lista.begin(), lista.end());
	int maks = *max_element(lista.begin(), lista.end());
	return (lista.size() + 1)*(min + maks)/2;
}

int znajdzBrakujacyElement(vector<int>& lista) {

	int sumaListy = accumulate(lista.begin(), lista.end(), 0);
	int sumaPrzedzialu = sumaCiaguArt(lista);

	return sumaPrzedzialu - sumaListy;
}

int main() {
    	vector<int> lista({6, 8, 4, 10, 14, 2});
	int wynik = 12;
	assert(znajdzBrakujacyElement(lista) == wynik);

	lista = {1, 2, 4, 5, 6};
	wynik = 3;
	assert(znajdzBrakujacyElement(lista) == wynik);

	return 0;
}
