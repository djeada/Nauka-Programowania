#include <vector>
#include <cassert>
#include <cmath>

using namespace std;

//Otrzymujesz dwie listy n wspolczynnikow wielomianu postaci 
//a_nx^n + a_(n-1)x^(n-1) + ... + a_. Oblicz wartosc wspolczynnikow 
//wielomianu bedacego iloczynem otrzymanych wielomianow.
vector<int> iloczyn(vector<int>& listaA, vector<int>& listaB, int n = -1) {

	vector<int> wynik(listaA.size() + listaB.size() - 1, 0);

	for (int i=0; i< listaA.size(); i++) { 
		for (int j=0; j<listaB.size(); j++) 
			wynik[i+j] += listaA[i]*listaB[j]; 
	}

	return wynik;
}

void test1() {
	vector<int> listaA {5, 0, 10, 6};
	vector<int> listaB {1, 2, 4};
	vector<int> wynik {5, 10, 30, 26, 52, 24};
	assert(iloczyn(listaA,listaB) == wynik);
}

int main() {
    	test1();
	return 0;
}

