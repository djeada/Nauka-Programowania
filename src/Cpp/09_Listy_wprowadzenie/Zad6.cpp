#include <vector>
#include <cassert>

using namespace std;

//Otrzymujesz liste liczb. Sprwadz czy srednia elementow 
//znajduje się w liscie. Dla sredniej nie bedacej liczba
//calkowita, zaokraglij wynik w dol.

int policzSrednia(vector<int>& lista) {
	
	int suma = 0;
	
	for (auto liczba : lista)
		suma += liczba;

	return suma/lista.size();
}

bool czySredniaWLiscie(vector<int>& lista) {

	int srednia = policzSrednia(lista);
	
	for (auto liczba : lista) {
		if (liczba == srednia)
			return true;
	}

	return false;
}

int main() {

    	vector<int> lista({3, 5, -7, 4, 9, -11, 2});    	
    	assert(!czySredniaWLiscie(lista));
    	
    	lista = {1, 2, 3};
        	assert(czySredniaWLiscie(lista));
    	
	return 0;
}

