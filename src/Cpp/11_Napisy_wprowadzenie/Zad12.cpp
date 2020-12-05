#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

/*
Usun spacje ze zdania.
*/

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(n)
void usunSpacjeV1(string& slowo) {
	string pom;

	for (const auto& znak : slowo) {
		if (znak != ' ')
			pom += znak;
	}
	
	slowo = pom;
}

//Zlozonosc Czasowa O(n)
void usunSpacjeV2(string& slowo) {
	slowo.erase(remove(slowo.begin(), slowo.end(), ' '), slowo.end());
}

int main() {
    string zdanie = "lezy jezy na wierzy";
    string wynik = "lezyjezynawierzy";

	usunSpacjeV1(zdanie);	
	assert(zdanie == wynik);
	
	zdanie = "lezy jezy na wierzy";
	
	usunSpacjeV2(zdanie);
	assert(zdanie == wynik);
    
	return 0;
}

