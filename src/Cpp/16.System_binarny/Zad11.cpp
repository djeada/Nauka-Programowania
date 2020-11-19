#include <iostream>
#include <cassert>
#include <bitset>

using namespace std;

/*
Konwersja miedzy dowolnymi systemami liczbowymi.
*/

const int liczbaBitow = 8;

bool czyPalindromV1(int liczba) {
  
	bitset<liczbaBitow> bity = liczba;
	for (int i = 0; i < liczbaBitow/2 - 1; i++) { 
		if (bity[i] ^ bity[liczbaBitow-1-i]) 
			return false;
	}
	return true;
}

int main() {
	int liczba = 231;
	
	assert(czyPalindromV1(liczba));
	
	liczba = 17;
	
	assert(!czyPalindromV1(liczba));
	
    return 0;
}

