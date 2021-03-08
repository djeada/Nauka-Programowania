#include <cassert>
#include <string>
#include <algorithm>

//Otrzymujesz napis. Zamien litery a na znaki zapytania.
void zamienV1(std::string& napis) {

	for (auto& znak : napis) {
		if (znak == 'a')
			znak = '?';
	}
}

void zamienV2(std::string& napis) {
	replace(napis.begin(), napis.end(), 'a', '?');
}

void test1() {
	std::string napis = "pacZka!";
	std::string wynik = "p?cZk?!";
	
	zamienV1(napis);
	assert(napis == wynik);
}

void test2() {
	std::string napis = "pacZka!";
	std::string wynik = "p?cZk?!";
	
	zamienV2(napis);
	assert(napis == wynik);
}

int main() {
	test1();
	test2();
	return 0;
}
