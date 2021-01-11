#include <vector>
#include <cassert>

using namespace std;

//Otrzymujesz liste n wspolczynnikow wielomianu postaci 
//a_nx^n + a_(n-1)x^(n-1) + ... + a_0 oraz liczbe k. 
//Oblicz wartosc wspolczynnikow wielomianu bedacego k-ta 
//pochodna otrzymanego wielomianu.
vector<int> pochodna(vector<int>& lista, int k) {

	vector<int> wynik;
	vector<int> kopia(lista);	
	
	for (int j = 0; j < k; j++) {
		wynik.clear();
		int n = kopia.size();
		for (int i = 0; i < n - 1; i++)
			wynik.push_back(kopia[i]*(n-i-1));
		kopia = wynik;
	}

	return wynik;
}

void test1() {
	vector<int> lista {4, -3, 2};
	int k = 1;
	vector<int> wynik {8, -3};
	assert(pochodna(lista, k) == wynik);
}

void test2() {
	vector<int> lista {13, -6, 0, -1, -1};
	int k = 2;
	vector<int> wynik {156, -36, 0};
	assert(pochodna(lista, k) == wynik);
}

int main() {

    	test1();
    	test2(); 	
	return 0;
}

