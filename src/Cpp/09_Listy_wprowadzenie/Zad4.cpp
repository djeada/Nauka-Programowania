#include <vector>
#include <cassert>
#include <limits>
#include <algorithm>

using namespace std;

//Otrzymujesz liste. Znajdz najwiekszy 
//i najmniejszy element tej listy.
int maksV1(vector<int>& lista) {

	if (lista.empty())
		return numeric_limits<int>::min();
	
	int maks = lista.front();

	for (auto liczba : lista) {
		if (liczba > maks)
			maks = liczba;
	}

	return maks;
}

int minV1(vector<int>& lista) {

	if (lista.empty())
		return numeric_limits<int>::max();
	
	int min = lista.front();

	for (auto liczba : lista) {
		if (liczba < min)
			min = liczba;
	}

	return min;
}


int main() {

    	vector<int> lista({3, 5, -7, 4, 9, -11, 2});
 	
    	assert(maksV1(lista) == *max_element(lista.begin(), lista.end()));
    	assert(minV1(lista) == *min_element(lista.begin(), lista.end()));
    	
	lista = {3, -2, 4, 29, -3, -40, 8, 5, -7, -1};

  	assert(maksV1(lista) == *max_element(lista.begin(), lista.end()));
    	assert(minV1(lista) == *min_element(lista.begin(), lista.end()));
    	    	
	return 0;
}

