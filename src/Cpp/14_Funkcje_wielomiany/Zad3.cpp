#include <vector>
#include <cassert>
#include <cmath>

using namespace std;

//Otrzymujesz dwie listy n wspolczynnikow wielomianu postaci 
//a_nx^n + a_(n-1)x^(n-1) + ... + a_. Oblicz wartosc wspolczynnikow 
//wielomianu bedacego suma otrzymanych wielomianow.
vector<int> suma(vector<int>& listaA, vector<int>& listaB) {

	assert(listaA.size() == listaB.size());
	vector<int> wynik;

	for (int i = 0; i < listaA.size(); i++)
		wynik.push_back(listaA[i] + listaB[i]);

	return wynik;
}

void test1() {
	vector<int> listaA {3, 2, 1};
	vector<int> listaB {8, 9, 2};
	vector<int> wynik {11, 11, 3};
	assert(suma(listaA,listaB) == wynik);
}

int main() {

    	test1();
    	    	
	return 0;
}

