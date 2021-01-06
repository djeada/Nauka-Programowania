#include <cassert>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

//Otrzymujesz liste liczb. 
//Zamien liste na napis.

string liczby(const vector<int>& lista) {
	string wynik = "";
	
	for (auto liczba : lista)
		wynik += to_string(liczba);

	return wynik;
}

void test1() {
	vector<int> lista({2, 4, 7});
	string wynik = "247";
	assert(liczby(lista) == wynik);
}

void test2() {
	vector<int> lista;
	string wynik = "";
	assert(liczby(lista) == wynik);
}

int main() {
	test1();
	test2();
	return 0;
}


