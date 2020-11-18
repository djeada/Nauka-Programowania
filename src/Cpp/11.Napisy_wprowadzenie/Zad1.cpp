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
void odwrocNapisV1(string& slowo) {

	int j = slowo.length() - 1;

	for (int i = 0; i <= j; i++, j--) {
		char c = slowo[i];
		slowo[i] = slowo[j];
		slowo[j] = c;	
	}
}

int main() {
    string napis = "adam";
    string wynik = "mada";

	odwrocNapisV1(napis);	
	assert(napis == wynik);
    
	return 0;
}

