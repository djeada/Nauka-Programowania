#include <cassert>
#include <string>
#include <algorithm>
#include <vector>

//Otrzymujesz liste liczb. 
//Zamien liste na napis.

std::string liczby(const std::vector<int>& lista) {
	std::string wynik = "";
	
	for (auto liczba : lista)
		wynik += std::to_string(liczba);

	return wynik;
}

void test1() {
	std::vector<int> lista({2, 4, 7});
	std::string wynik = "247";
	assert(liczby(lista) == wynik);
}

void test2() {
	std::vector<int> lista;
	std::string wynik = "";
	assert(liczby(lista) == wynik);
}

int main() {
	test1();
	test2();
	return 0;
}


