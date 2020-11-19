#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

/*
Znajdz wszystkie permutacje slowa.
*/

void permutacja (string& slowoWej, string& slowoWyj, vector<string>& wynik) {
	if (slowoWej.empty()) {
		wynik.push_back(slowoWyj);
		return;
	}

	for (int i = 0; i < slowoWej.length(); ++i) {
		string noweSlowoWej = slowoWej;
		string noweSlowoWyj = slowoWyj;
		noweSlowoWej .erase(i,1);
		noweSlowoWyj += slowoWej.at(i);
		permutacja (noweSlowoWej, noweSlowoWyj, wynik);
	}
}

vector<string> permutacje(string& slowoWej) {
	
	vector<string> wynik;

	string slowoWyj;  
	permutacja(slowoWej, slowoWyj, wynik);
	
	return wynik;
}

int main() {
    string slowo = "Dora";

    vector<string> listaPermutacji = permutacje(slowo);
	
	vector<string> wynik {"Droa", "Daor", "aDor", "aroD", "aDro", "aorD", "raDo", "roDa", "rDoa", "raoD", "aoDr", "arDo", 
    			"oraD", "oaDr", "orDa", "rDao", "oDar", "roaD", "oarD", "oDra", "Dora", "Daro", "Doar", "Drao"};

	sort(listaPermutacji.begin(), listaPermutacji.end());
	sort(wynik.begin(), wynik.end());
	assert(listaPermutacji == wynik); 

    return 0;
}

