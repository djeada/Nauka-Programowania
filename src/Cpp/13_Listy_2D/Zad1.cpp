#include <cassert>
#include <vector>

using namespace std;

//Otrzymjesz dwie liczby, a oraz b. Stwórz macierz a 
//identycznych wierszy składających się z liczb od 0 do b.

vector<vector<int>> macierz(int a, int b) {

	vector<vector<int>> macierz;
	vector<int> wiersz;

	for (int i = 0; i <= b; i++)
		wiersz.push_back(i);

	for (int i = 0; i < a; i++)
		macierz.push_back(wiersz);

	return macierz;
}

void test1() {
	vector<vector<int>> wynik { {0, 1, 2, 3, 4, 5}, 
				{0, 1, 2, 3, 4, 5}, 
				{ 0, 1, 2, 3, 4, 5} };
	int a = 3;
	int b = 5;
	assert(macierz(a, b) == wynik);

}

void test2() {
	vector<vector<int>> wynik { {0, 1, 2}, 
				{0, 1, 2} };
	int a = 2;
	int b = 2;
	assert(macierz(a, b) == wynik);

}

int main() {
	test1();
	test2();
	return 0;	 	
}
