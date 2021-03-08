#include <cassert>
#include <string>
#include <algorithm>

//Policz z ilu slow sklada sie zdanie. 
//Znaki interpunkcyjne nie sa liczone jako slowa.

//Zlozonosc Czasowa O(n)
//Zlozonosc Pamieciowa O(1)
int policzSlowaV1(std::string& slowo) {

	bool spacja = true;
	int licznik = 0;

	for (auto znak : slowo) {
		if (isspace(znak))
			spacja = true;
		else if (isalpha(znak) && spacja) {
			licznik++;
			spacja = false;
		}
	}

	return licznik;
}

void test1() {
	std::string napis = "Ile to   ma :  slow w swoim zdaniu na   koniec?";
	int wynik = 9;

	assert(policzSlowaV1(napis) == wynik);
}

int main() {
	test1();
	return 0;
}
