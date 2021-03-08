#include <cassert>
#include <string>
#include <algorithm>

//Otrzymujesz napis. Zamien wszystkie 
//male litery na wielkie.

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void naWielkieV1(std::string& slowo) {

	for (auto& znak : slowo) {
		if (znak >= 97 && znak <= 122)
			znak -= 32;
	}
}

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void naWielkieV2(std::string& slowo) {

	for (auto& znak : slowo) {
		if (islower(znak))
			znak = toupper(znak);
	}
}

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void naWielkieV3(std::string& slowo) {
    transform(slowo.begin(), slowo.end(), slowo.begin(), ::toupper); 
}

void test1() {
	std::string napis = "pacZka!";
	std::string wynik = "PACZKA!";
	
	naWielkieV1(napis);
	assert(napis == wynik);
}

void test2() {
	std::string napis = "pacZka!";
	std::string wynik = "PACZKA!";
	
	naWielkieV2(napis);
	assert(napis == wynik);
}

void test3() {
	std::string napis = "pacZka!";
	std::string wynik = "PACZKA!";
	
	naWielkieV3(napis);
	assert(napis == wynik);
}

int main() {
	test1();
	test2();
	test3();
	return 0;
}


