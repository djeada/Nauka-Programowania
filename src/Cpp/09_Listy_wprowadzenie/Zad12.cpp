#include <vector>
#include <cassert>
#include <string>

using namespace std;

//Otrzymujesz liste liczb, kierunek przesuniec (1 odpowiada przesunieciu 
//w prawo, a 0 w lewo) oraz liczbę miejsc o jaka maja zostac przesuniete 
//elementy. Przykladowo dla przesuwania w prawo pierwszy element trafia 
//na miejsce drugiego, drugi trzeciego, a ostatni na miejsce pierwszego. 
//Przesun elementy listy w danym kierunku.

//Zlozonosc czasowa O(n)
//Zlozonosc pamieciowa O(n)
void rotacjaV1(vector<int>& lista, const string& kierunek, int liczba) {

	if (kierunek == "prawo") {
		for (int i = 0; i < liczba; i++) {
			lista.insert(lista.begin(), lista.back());
			lista.erase(std::prev(lista.end()));
		}
	}

	else {
		for (int i = 0; i < liczba; i++) {
			lista.push_back(lista.front());
			lista.erase(lista.begin());
		}
	}
}

int main() {
    	vector<int> lista({5, 27, 6, 2, 1, 10, 8});
    	vector<int> wynik({6, 2, 1, 10, 8, 5, 27});
	string kierunek = "lewo";
	int liczba = 2;

	rotacjaV1(lista, kierunek, liczba);
	assert(lista == wynik);


	lista = {9, 9, 42, 47, 5, 6, 19, 7};
    	wynik = {6, 19, 7, 9, 9, 42, 47, 5};
	kierunek = "prawo";
	liczba = 3;

	rotacjaV1(lista, kierunek, liczba);
	assert(lista == wynik);

	return 0;
}
