#include <vector>
#include <cassert>

using namespace std;

//Dla otrzymanych dwoch list, zwroc liste, ktorej 
//elemnty sa suma odpowiadajacych sobie elementow 
//otrzymanych list.

vector<int> suma(vector<int>& listaA, vector<int>& listaB) {

	vector<int> wynik(listaA);

	int n = wynik.size() < listaB.size() ? wynik.size() : listaB.size();

	for (int i = 0; i < n; i++)
		wynik[i] += listaB[i];
	
	for (int i = n; i < listaB.size(); i++)
		wynik.push_back(listaB[i]);

	return wynik;
}

int main() {

	vector<int> listaA({3, 1, 2, 5});
	vector<int> listaB({2, 8, 6, 5});

	vector<int> wynik({5, 9, 8, 10});
	assert(suma(listaA, listaB) == wynik);

	return 0;
}

