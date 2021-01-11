#include <vector>
#include <cassert>
#include <cmath>

using namespace std;

//Otrzymujesz liste n wspolczynnikow wielomianu postaci 
//a_nx^n + a_(n-1)x^(n-1) + ... + a_0 oraz liczbe x. 
//Oblicz wartosc wspolczynnikow wielomianu po 
//przemnozeniu przez liczbe x.
vector<int> iloczyn(vector<int>& lista, int x) {

	vector<int> wynik;

	for (auto& liczba : lista)
		wynik.push_back(liczba*x);

	return wynik;
}

void test1() {
	vector<int> lista {3, 2, 1};
	int x = 2;
	vector<int> wynik {6, 4, 2};
	assert(iloczyn(lista,x) == wynik);
}

int main() {

    	test1();
    	    	
	return 0;
}

