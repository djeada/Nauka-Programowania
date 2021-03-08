#include <cassert>
#include <string>
#include <algorithm>

//Odwroc napis.

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void odwrocNapisV1(std::string& slowo) {

	int j = slowo.length() - 1;

	for (int i = 0; i <= j; i++, j--) {
		char c = slowo[i];
		slowo[i] = slowo[j];
		slowo[j] = c;	
	}
}

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void odwrocNapisV2(std::string& slowo) {
    reverse(slowo.begin(), slowo.end());
}

void test1() {
	std::string napis = "adam";
	std::string wynik = "mada";

	odwrocNapisV1(napis);
	assert(napis == wynik);
}

void test2() {
	std::string napis = "adam";
	std::string wynik = "mada";

	odwrocNapisV2(napis);
	assert(napis == wynik);
}

int main() {
	test1();	
	test2();
	return 0;
}

