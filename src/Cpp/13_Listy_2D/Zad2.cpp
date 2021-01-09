#include <cassert>
#include <vector>
#include <utility>

using namespace std;

//Dla otrzymanej liczby, stworz macierz kwadratowa skladajaca
//się z liczby kolumn i wierszy rownej otrzymanej liczbie
//ktorej kazdy element jest iloczynem jego wspolrzednych.

vector<vector<int>> macierz(int n) {

	vector<vector<int>> macierz;
	macierz.reserve(n);

	for (int i = 0; i < n; i++) {
		vector<int> wiersz;
		for (int j = 0; j < n; j++)
			wiersz.push_back(i*j);
		macierz.push_back(wiersz);
	}

	return macierz;
}

void test1() {
	int n = 4;
	vector<vector<int>> wynik { {0, 0, 0, 0}, {0, 1, 2, 3}, 
				{0, 2, 4, 6},  {0, 3, 6, 9} };
	assert(macierz(n) == wynik);
}

int main() {
	test1();
	return 0;	 	
}
