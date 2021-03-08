#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

//Znajdz wszystkie permutacje slowa.

void permutacja (std::string& slowoWej, std::string& slowoWyj, std::vector<std::string>& wynik) {
	if (slowoWej.empty()) {
		wynik.push_back(slowoWyj);
		return;
	}

	for (unsigned int i = 0; i < slowoWej.length(); ++i) {
		std::string noweSlowoWej = slowoWej;
		std::string noweSlowoWyj = slowoWyj;
		noweSlowoWej .erase(i,1);
		noweSlowoWyj += slowoWej.at(i);
		permutacja (noweSlowoWej, noweSlowoWyj, wynik);
	}
}

std::vector<std::string> permutacje(std::string& slowoWej) {
	
	std::vector<std::string> wynik;

	std::string slowoWyj;  
	permutacja(slowoWej, slowoWyj, wynik);
	
	return wynik;
}

void test1() {
	std::string slowo = "Dora";

	std::vector<std::string> listaPermutacji = permutacje(slowo);

	std::vector<std::string> wynik {"Droa", "Daor", "aDor", "aroD", "aDro", "aorD", "raDo", "roDa", "rDoa", "raoD", "aoDr", "arDo", 
	"oraD", "oaDr", "orDa", "rDao", "oDar", "roaD", "oarD", "oDra", "Dora", "Daro", "Doar", "Drao"};

	sort(listaPermutacji.begin(), listaPermutacji.end());
	sort(wynik.begin(), wynik.end());
	assert(listaPermutacji == wynik); 
}


int main() {

	test1();

	return 0;
}

