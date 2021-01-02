#include <vector>
#include <cassert>
#include <algorithm>
#include <numeric>

using namespace std;

//Dla otrzymanej listy skladajacej sie z nieparzystej 
//liczby elementow znajdz element bez pary. Przez pary 
//elementow rozumiemy tutaj elementy o rownej wartosci. 

//Zlozonosc czasowa O(n)
//Zlozonosc pamieciowa O(n)
int elementBezParyV1(vector<int>& lista) {
	vector<int> pom;

	for (auto liczba : lista) {
		auto i = find(pom.begin(), pom.end(), liczba);
		if (i != pom.end())
			pom.erase(i);
		else
			pom.push_back(liczba);
	}

	return pom.front();
}

//Zlozonosc czasowa O(n)
//Zlozonosc pamieciowa O(n)
int elementBezParyV2(vector<int>& lista) {
	int wynik = 0;

	for (auto liczba : lista)
		wynik ^= liczba;

	return wynik;
}

int main() {
    	vector<int> lista({1, 3, 1,  7, 3, 1, 1});
	int wynik = 7;
	assert(elementBezParyV1(lista) == wynik);
	assert(elementBezParyV2(lista) == wynik);

	return 0;
}
