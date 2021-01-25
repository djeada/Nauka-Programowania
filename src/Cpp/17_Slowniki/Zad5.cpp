#include <cassert>
#include <unordered_map>
#include <utility>
#include <vector>
#include <string>

using namespace std;

//Otrzymujesz liste par. Pierwszym elementem pary jest napis reprezentujacy imie i nazwikso 
//pracownika, drugim zysk z transakcji jaka dany pracownik przeprowadzil. Znajdz pracownika, 
//ktory przyniosl firmie najwiecej zysku.

void wypelnijSlownik(const vector<pair<string, int>>& lista, unordered_map<string, int>& slownik) {

	for (const auto& rekord : lista)
		slownik[rekord.first] += rekord.second;
}

string znajdzMaxZysk(unordered_map<string, int>& slownik) {
	string najlepszyPracownik;
	int maxZysk = -1;

	for (auto it = slownik.begin(); it != slownik.end(); it++) {
		if (it->second > maxZysk) {
			najlepszyPracownik = it->first;
			maxZysk = it->second;
		}
	}

	return najlepszyPracownik;
}

string pracownik(vector<pair<string, int>>& lista) {

	if (lista.empty())
		return "";

	unordered_map<string, int> slownik;
	wypelnijSlownik(lista, slownik);

	return znajdzMaxZysk(slownik);
}

void test1() {

	vector<pair<string, int>> lista {{"Barnaba Barabash", 120}, {"Jon Snow", 100}, {"Kira Summer", 300}, 
					{"Barnaba Barabash", 200}, {"Bob Marley", 110}};

	string wynik = "Barnaba Barabash";

	assert(pracownik(lista) == wynik);
}

void test2() {
	vector<pair<string, int>> lista;
	string wynik;

	assert(pracownik(lista) == wynik);
}

int main() {

	test1();
	test2();

	return 0;
}

