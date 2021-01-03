#include <vector>
#include <cassert>
#include <algorithm>
#include <unordered_set>

using namespace std;

//Otrzymujesz dwie listy. Znajdz elementy wystepujace 
//zarowno w pierwszej jak i w drugiej liscie.

//Zlozonosc obliczeniowa O(n^2)
//Zlozonosc pamieciowa O(n)
vector<int> czescWspolnaV1(vector<int>& listaA, vector<int>& listaB) {

	vector<int> wynik;

	for (auto liczba : listaA) {
		if (find(listaB.begin(), listaB.end(), liczba) != listaB.end())
			wynik.push_back(liczba);
	}

	return wynik;
}

//Zlozonosc obliczeniowa O(nlogn)
//Zlozonosc pamieciowa O(n)
vector<int> czescWspolnaV2(vector<int>& listaA, vector<int>& listaB) {

	vector<int> wynik;
    	sort(listaA.begin(), listaA.end());
    	sort(listaB.begin(), listaB.end());
	set_intersection(listaA.begin(), listaA.end(), listaB.begin(), listaB.end(), inserter(wynik, wynik.begin()));

	return wynik;
}

bool wektoryRowne(vector<int> v1, vector<int> v2) {
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    return v1 == v2;
}

int main() {

	vector<int> listaA({3, 6, 2, 7, 9});
	vector<int> listaB({4, 2, 3, 5, 6});
	vector<int> wynik({3, 6, 2});
	assert(wektoryRowne(czescWspolnaV1(listaA, listaB), wynik));
	assert(wektoryRowne(czescWspolnaV2(listaA, listaB), wynik));

	return 0;
}

