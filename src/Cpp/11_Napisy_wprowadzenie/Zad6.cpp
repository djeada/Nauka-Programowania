#include <cassert>
#include <string>
#include <algorithm>

using namespace std;

//Otrzymujesz napis. Zamien litery a na znaki zapytania.
void zamienV1(string& napis) {

	for (auto& znak : napis) {
		if (znak == 'a')
			znak = '?';
	}
}

void zamienV2(string& napis) {
	replace(napis.begin(), napis.end(), 'a', '?');
}

void test1() {
	string napis = "pacZka!";
	string wynik = "p?cZk?!";
	
	zamienV1(napis);
	assert(napis == wynik);
}

void test2() {
	string napis = "pacZka!";
	string wynik = "p?cZk?!";
	
	zamienV2(napis);
	assert(napis == wynik);
}

int main() {
	test1();
	test2();
	return 0;
}
