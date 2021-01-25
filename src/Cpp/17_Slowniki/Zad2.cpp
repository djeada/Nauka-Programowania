#include <cassert>
#include <unordered_map>
#include <vector>

using namespace std;

//Otrzymujesz dwie listy. Zbuduj slownik skladajacy się z kluczy będacych 
//elementami pierwszej listy i wartosciami będacymi elementami drugiej listy. 
//Jesli listy sa roznej dlugosci zwroc pusty slownik.
unordered_map<int, int> budujSlownik(vector<int>& listaA, vector<int>& listaB) {
	unordered_map<int, int> slownik;

	if (listaA.size() != listaB.size())
		return slownik;

	for (int i = 0; i < listaA.size(); i++)
		slownik[listaA[i]] = listaB[i];

	return slownik;
}

void test1() {
	vector<int> listaA {3, 5, 8};
	vector<int> listaB {1, 2, -1};
	unordered_map<int, int> wynik {{3, 1}, {5, 2}, {8, -1}};

	assert(budujSlownik(listaA, listaB) == wynik);
}

void test2() {
	vector<int> listaA {0, 1};
	vector<int> listaB {1, 0};
	unordered_map<int, int> wynik {{0, 1}, {1, 0}};

	assert(budujSlownik(listaA, listaB) == wynik);
}

int main() {

	test1();
	test2();

	return 0;
}

