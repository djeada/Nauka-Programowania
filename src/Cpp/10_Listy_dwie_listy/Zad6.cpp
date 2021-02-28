#include <vector>
#include <cassert>
#include <algorithm>
#include <unordered_set>

//Otrzymujesz dwie listy. Znajdz elementy wystepujace 
//zarowno w pierwszej jak i w drugiej liscie.

//Zlozonosc obliczeniowa O(n^2)
//Zlozonosc pamieciowa O(n)
std::vector<int> czescWspolnaV1(std::vector<int>& listaA, std::vector<int>& listaB) {

	std::vector<int> wynik;

	for (auto liczba : listaA) {
		if (find(listaB.begin(), listaB.end(), liczba) != listaB.end())
			wynik.push_back(liczba);
	}

	return wynik;
}

//Zlozonosc obliczeniowa O(nlogn)
//Zlozonosc pamieciowa O(n)
std::vector<int> czescWspolnaV2(std::vector<int>& listaA, std::vector<int>& listaB) {

	std::vector<int> wynik;
    	sort(listaA.begin(), listaA.end());
    	sort(listaB.begin(), listaB.end());
	set_intersection(listaA.begin(), listaA.end(), listaB.begin(), listaB.end(), inserter(wynik, wynik.begin()));

	return wynik;
}

bool wektoryRowne(std::vector<int> v1, std::vector<int> v2) {
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	return v1 == v2;
}

void test1() {
	std::vector<int> listaA {3, 6, 2, 7, 9};
	std::vector<int> listaB {4, 2, 3, 5, 6};
	std::vector<int> wynik {3, 6, 2};
	assert(wektoryRowne(czescWspolnaV1(listaA, listaB), wynik));
}

void test2() {
	td::vector<int> listaA {3, 6, 2, 7, 9};
	std::vector<int> listaB {4, 2, 3, 5, 6};
	std::vector<int> wynik {3, 6, 2};
	assert(wektoryRowne(czescWspolnaV2(listaA, listaB), wynik));
}

int main() {

	test1();
	test2();

	return 0;
}
