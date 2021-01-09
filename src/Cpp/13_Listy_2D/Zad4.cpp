#include <cassert>
#include <vector>

using namespace std;

//Otrzymujesz dwie macierze o tych samych wymiarach, zwroc macierz bedaca:

//a) wynikiem dodawania otrzymanych macierzy;
bool wymiaryRowne(vector<vector<int>> macierzA, vector<vector<int>> macierzB) {

	if (macierzA.size() != macierzB.size())
		return false;

	
	for (int i = 0; i < macierzA.size(); i++) {
		if (macierzA[i].size() != macierzB[i].size())
			return false;
	}

	return true;
}

vector<vector<int>> dodaj(vector<vector<int>> macierzA, vector<vector<int>> macierzB) {

	vector<vector<int>> wynik;

	if (!wymiaryRowne(macierzA, macierzB))
		return wynik;


	for(int i = 0; i < macierzA.size(); ++i) {
		vector<int> wiersz;
        		for(int j = 0; j < macierzA[i].size(); ++j)
            		wiersz.push_back(macierzA[i][j] + macierzB[i][j]);
		wynik.push_back(wiersz);
	}

	return wynik;
}

//b) odejmowania pierwszej macierzy od drugiej.
vector<vector<int>> odejmij(vector<vector<int>> macierzA, vector<vector<int>> macierzB) {


	vector<vector<int>> wynik;

	if (!wymiaryRowne(macierzA, macierzB))
		return wynik;


	for(int i = 0; i < macierzA.size(); ++i) {
		vector<int> wiersz;
        		for(int j = 0; j < macierzA[i].size(); ++j)
            		wiersz.push_back(macierzA[i][j] - macierzB[i][j]);
		wynik.push_back(wiersz);
	}
	
	return wynik;
}

void test1() {
	vector<vector<int>> macierzA { {1, 2}, {-2, 0} };
	vector<vector<int>> macierzB { {5, -3}, {1, 7} };
	vector<vector<int>> wynik { {6, -1}, {-1, 7} };
	assert(dodaj(macierzA, macierzB) == wynik);
}

void test2() {
	vector<vector<int>> macierzA { {1, 2}, {-2, 0} };
	vector<vector<int>> macierzB { {5, -3}, {1, 7} };
	vector<vector<int>> wynik { {-4, 5}, {-3, -7} };
	assert(odejmij(macierzA, macierzB) == wynik);
}

int main() {
	test1();
	test2();
	return 0;	 	
}
