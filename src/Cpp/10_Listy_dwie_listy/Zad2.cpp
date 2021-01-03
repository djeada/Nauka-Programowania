#include <vector>
#include <cassert>

using namespace std;

//Dla otrzymanych dwoch list zwroc liste powstala poprzez:
//a) dostawienie drugiej listy na koniec pierwszej listy;
vector<int> dostaw(vector<int>& listaA, vector<int>& listaB) {

	vector<int> wynik(listaA);
	
	for (auto liczba : listaB)
		wynik.push_back(liczba);

	return wynik;
}

//wstawienie elemntów o indeksach parzystych z drugiej 
//listy na odpowiadające im indeksy pierwszej listy.
vector<int> podmien(vector<int>& listaA, vector<int>& listaB) {
	vector<int> wynik(listaA);
	
	for (int i = 0; i < wynik.size(); i+=2 )
		wynik[i] = listaB[i];

	return wynik;
}

int main() {

	vector<int> listaA({-2, 8, 3, 6});
	vector<int> listaB({7, 5, 0});

	vector<int> wynik({-2, 8, 3, 6, 7, 5, 0});
	assert(dostaw(listaA, listaB) == wynik);
	
	wynik = {7, 8, 0, 6};
	assert(podmien(listaA, listaB) == wynik);

	return 0;
}

