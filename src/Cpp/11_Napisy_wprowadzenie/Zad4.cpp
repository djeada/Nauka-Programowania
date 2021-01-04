#include <cassert>
#include <string>
#include <algorithm>

using namespace std;

/*
Otrzymujesz napis. Zamien wszystkie 
male litery na wielkie.
*/

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void naWielkieV1(string& slowo) {

	for (auto& znak : slowo) {
		if (znak >= 97 && znak <= 122)
			znak -= 32;
	}
}

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void naWielkieV2(string& slowo) {

	for (auto& znak : slowo) {
		if (islower(znak))
			znak = toupper(znak);
	}
}

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
void naWielkieV3(string& slowo) {
    transform(slowo.begin(), slowo.end(), slowo.begin(), ::toupper); 
}

void test1() {
	string napis = "pacZka!";
	string wynik = "PACZKA!";
	
	naWielkieV1(napis);
	assert(napis == wynik);
}

void test2() {
	string napis = "pacZka!";
	string wynik = "PACZKA!";
	
	naWielkieV2(napis);
	assert(napis == wynik);
}

void test3() {
	string napis = "pacZka!";
	string wynik = "PACZKA!";
	
	naWielkieV3(napis);
	assert(napis == wynik);
}

int main() {
	test1();
	test2();
	test3();
	return 0;
}


