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

void test1() {
	string zdanie = "lezy jezy na wierzy";
	string wynik = "lezyjezynawierzy";

	usunSpacjeV1(zdanie);	
	assert(zdanie == wynik);
}

void test2() {
	string zdanie = "lezy jezy na wierzy";
	string wynik = "lezyjezynawierzy";

	usunSpacjeV2(zdanie);
	assert(zdanie == wynik);
}

int main() {
	test1();
	test2();

	return 0;
}

