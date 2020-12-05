#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

/*
Odwroc napis.
*/

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void odwrocNapis(string& slowo, int pocz, int koniec) {

	int j = koniec;

	for (int i = pocz; i <= j; i++, j--) {
		char c = slowo[i];
		slowo[i] = slowo[j];
		slowo[j] = c;	
	}
}

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void odwrocNapisy(string& zdanie) {

	int N = zdanie.length():
	int pocz = 0;
	int koniec;

	for (int i = 0; i < N; i++) {
		if (zdanie[i] == ' ' || zdanie[i] == '\0') {
			koniec = i - 1 ;
			odwrocNapis(zdanie, pocz, koniec);
			pocz = i + 1;
		}
	}
}

int main() {
    string napis = "Cameron Diaz";
    string wynik = "noremaC zaiD";

	odwrocNapisV1(napis);	
	assert(napis == wynik);
    
	return 0;
}

