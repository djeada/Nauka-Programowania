#include <cassert>
#include <vector>
#include <utility>

using namespace std;

//Dla otrzymanych dwoch list, stworz dwu-kolumnowa macierz, 
//ktorej pierwsza kolumna sklada się z elementow pierwszej 
//listy, a druga drugiej. Jesli otrzymane listy nie sa rownej 
//dlugosci zwroc pusta macierz.

vector<pair<int, int>> macierz(vector<int> listaA, vector<int> listaB) {

	vector<pair<int, int>> macierz;


	if (listaA.size() != listaB.size())
		return macierz;

	int n = listaA.size();
	macierz.reserve(n);

	for (int i = 0; i < n; i++)
		macierz.push_back(pair<int, int>(listaA[i], listaB[i]));

	return macierz;
}

void test1() {
	vector<pair<int, int>> wynik { {3, 2}, {5, 8}, {2, 1}};
	vector<int> listaA {3, 5, 2};
	vector<int> listaB {2, 8, 1};
	assert(macierz(listaA, listaB) == wynik);
}

int main() {
	test1();
	return 0;	 	
}
