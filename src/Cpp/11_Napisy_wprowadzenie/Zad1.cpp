#include <cassert>
#include <string>
#include <algorithm>

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

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void odwrocNapisV2(string& slowo) {
    reverse(slowo.begin(), slowo.end());
}

void test1() {
	string napis = "adam";
	string wynik = "mada";

	odwrocNapisV1(napis);
	assert(napis == wynik);
}

void test2() {
	string napis = "adam";
	string wynik = "mada";

	odwrocNapisV2(napis);
	assert(napis == wynik);
}

int main() {
	test1();	
	test2();
	return 0;
}

