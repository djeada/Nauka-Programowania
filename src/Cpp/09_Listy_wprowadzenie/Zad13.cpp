#include <vector>
#include <cassert>
#include <algorithm>
#include <numeric>

//Dla otrzymanej listy, skladajacej się z nieuporzadkowanych 
//kolejnych (za wyjatkiem jednego) wyrazow ciagu arytmetycznego, 
//znajdz brakujacy element.

int sumaCiaguArt(std::vector<int>& lista) {
	int min = *min_element(lista.begin(), lista.end());
	int maks = *max_element(lista.begin(), lista.end());
	return (lista.size() + 1)*(min + maks)/2;
}

int znajdzBrakujacyElement(std::vector<int>& lista) {

	int sumaListy = accumulate(lista.begin(), lista.end(), 0);
	int sumaPrzedzialu = sumaCiaguArt(lista);

	return sumaPrzedzialu - sumaListy;
}

void test1() {
	std::vector<int> lista {6, 8, 4, 10, 14, 2};
	int wynik = 12;
	assert(znajdzBrakujacyElement(lista) == wynik);
}

void test2() {
	std::vector<int> lista {1, 2, 4, 5, 6};
	int wynik = 3;
	assert(znajdzBrakujacyElement(lista) == wynik);
}

int main() {
    	
	test1();
	test2();

	return 0;
}
