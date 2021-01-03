#include <vector>
#include <cassert>
#include <algorithm>
#include <unordered_set>

using namespace std;

//Otrzymujesz dwie listy. Znajdz elementy
//ktore nie sa czescia wspolna obu list.

//Zlozonosc obliczeniowa O(n^2)
//Zlozonosc pamieciowa O(n)
vector<int> roznicaV1(vector<int>& listaA, vector<int>& listaB) {

	vector<int> wynik;

	for (auto liczba : listaA) {
		if (find(listaB.begin(), listaB.end(), liczba) == listaB.end())
			wynik.push_back(liczba);
	}

	for (auto liczba : listaB) {
		if (find(listaA.begin(), listaA.end(), liczba) == listaA.end())
			wynik.push_back(liczba);
	}

	return wynik;
}

//Zlozonosc obliczeniowa O(nlogn)
//Zlozonosc pamieciowa O(n)
vector<int> roznicaV2(vector<int>& listaA, vector<int>& listaB) {

	vector<int> wynik;
    	sort(listaA.begin(), listaA.end());
    	sort(listaB.begin(), listaB.end());
	set_difference(listaA.begin(), listaA.end(), listaB.begin(), listaB.end(), inserter(wynik, wynik.begin()));
	set_difference(listaB.begin(), listaB.end(), listaA.begin(), listaA.end(), inserter(wynik, wynik.begin()));

	return wynik;
}

bool wektoryRowne(vector<int> v1, vector<int> v2) {
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    return v1 == v2;
}

int main() {

	vector<int> listaA({9, 2, 5, 4});
	vector<int> listaB({4, 2, 1});
	vector<int> wynik({9, 5, 1});
	assert(wektoryRowne(roznicaV1(listaA, listaB), wynik));
	assert(wektoryRowne(roznicaV2(listaA, listaB), wynik));

	return 0;
}
