#include <cassert>
#include <string>
#include <algorithm>

//Otrzymujesz napis. Zamien wszystkie znaki napisu
//na odpowiadajace im numery w tablicy ASCII. Podmien 
//otrzymany napis na uzyskane numery oddzielone przecinkami.

void zamienV1(std::string& napis) {

	if (napis.empty())
		return;

	std::string wynik = "";

	for (int numer : napis)
		wynik += std::to_string(numer) + ", ";

	napis = wynik.substr(0, wynik.size() - 2);
}

void test1() {
	std::string napis = "pacZka!";
	std::string wynik = "112, 97, 99, 90, 107, 97, 33";
	
	zamienV1(napis);
	assert(napis == wynik);
}

void test2() {
	std::string napis = "";
	std::string wynik = "";
	
	zamienV1(napis);
	assert(napis == wynik);
}


int main() {
	test1();
	test2();
	return 0;
}


