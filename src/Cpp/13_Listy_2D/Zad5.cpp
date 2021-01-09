#include <cassert>
#include <vector>
#include <utility>

using namespace std;

//Otrzymujesz macierz kwadratowa. Sprawdz, czy macierz jest kwadratem magicznym.
//Kwadrat magiczny sklada sie z nie powtarzajacych sie dodatnich liczb naturalnych. 
//Suma elementow w kazdym wierszu, w kazdej kolumnie oraz na kazdej przekatnej 
//jest taka sama.

bool macierzKwadratowa(const vector<vector<int>>& macierz) {

	int n = macierz.size();
	
	for (int i = 0; i < n; i++) {
		if (macierz[i].size() != n)
			return false;
	}

	return true;
}

pair<int, int> przekatne(const vector<vector<int>>& macierz) {
	int sumaPrzekatnej1 = 0;
	int sumaPrzekatnej2 = 0;
	int n = macierz.size();

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (i == j)
				sumaPrzekatnej1 += macierz[i][j];
			if (i + j == (n-1))
				sumaPrzekatnej2 += macierz[i][j];
		}
	}

	return pair<int, int>(sumaPrzekatnej1, sumaPrzekatnej2);
}

vector<int> wiersze(const vector<vector<int>>& macierz) {
	vector<int> wynik;

	for (auto wiersz : macierz) {
		int sumaWiersz = 0;

		for (auto liczba : wiersz)
			sumaWiersz += liczba;
		
		wynik.push_back(sumaWiersz);
	}

	return wynik;
}

vector<int> kolumny(const vector<vector<int>>& macierz) {
	vector<int> wynik;

	for (int i = 0; i < macierz.size(); i++) {
		int sumaKolumna = 0;

		for (int j = 0; j < macierz.size(); j++)
    			sumaKolumna += macierz[j][i];		
		
		wynik.push_back(sumaKolumna);
	}

	return wynik;
}

bool magicznyKwadrat(const vector<vector<int>>& macierz) {

	if (!macierzKwadratowa(macierz))
		return false;

	int n = macierz.size();

	pair<int, int> sumaPrzekatnych = przekatne(macierz);

	if (sumaPrzekatnych.first != sumaPrzekatnych.second)
		return false;

	for (auto sumaWiersz : wiersze(macierz)) {
		if (sumaWiersz != sumaPrzekatnych.first)
			return false;
	}


	for (auto sumaKolumna : kolumny(macierz)) {
		if (sumaKolumna != sumaPrzekatnych.first)
			return false;
	}

	return true;
}

void test1() {
	vector<vector<int>> macierz { {2, 7, 6}, {9, 5, 1}, {4, 3, 8} };
	assert(magicznyKwadrat(macierz));
}

void test2() {
	vector<vector<int>> macierz { {1, 2}, {-2, 0} };
	assert(!magicznyKwadrat(macierz));
}

int main() {
	test1();
	test2();
	return 0;	 	
}
