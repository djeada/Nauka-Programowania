#include <cassert>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

//Otrzymujesz napis reprezuntajacy zdanie. 
//Znajdz najdluzsze oraz najkrotsze slowo w zdaniu. 
//Jesli wiecej niz jedno slowo ma ekstremalna dlugosc, 
//zwroc te, ktore wystepuje w zdaniu jako pierwsze. 
//Znaki interpunkcyjne nie sa liczone jako slowa. 

void wyczysc(string& napis){
	auto it = napis.begin();

	while (it != napis.end()) {
		if (ispunct(*it))
			napis.erase(it);
		else
			it++;
	}
}

string najdluzsze(string& napis) {
	string wynik;
	int dlugosc = 0;
	int pocz = 0; 
	int konc = 0;
	while ((konc = napis.find(' ', pocz)) != string::npos) {
		if (konc != pocz) {
			auto slowo = napis.substr(pocz, konc - pocz);
			wyczysc(slowo);

			if (slowo.size() > dlugosc) {
				wynik = slowo;
				dlugosc = slowo.size();

			}
		}
		pocz = konc + 1;
	}
	if (konc != pocz) {
		auto slowo = napis.substr(pocz);
		wyczysc(slowo);
		if (slowo.size() > dlugosc) {
			wynik = slowo;
			dlugosc = slowo.size();		
		}
	}

	return wynik;
}

string najkrotsze(string& napis) {
	string wynik;
	int dlugosc = napis.size();
	int pocz = 0; 
	int konc = 0;
	while ((konc = napis.find(' ', pocz)) != string::npos) {
		if (konc != pocz) {
			auto slowo = napis.substr(pocz, konc - pocz);
			wyczysc(slowo);

			if (slowo.size() < dlugosc) {
				wynik = slowo;
				dlugosc = slowo.size();

			}
		}
		pocz = konc + 1;
	}
	if (konc != pocz) {
		auto slowo = napis.substr(pocz);
		wyczysc(slowo);
		if (slowo.size() < dlugosc) {
			wynik = slowo;
			dlugosc = slowo.size();		
		}
	}

	return wynik;
}

void test1() {
	string napis = "Kaczka lubi wiosne.";
	string wynik = "Kaczka";
	assert(najdluzsze(napis) == wynik);
}

void test2() {
	string napis = "Kaczka lubi wiosne.";
	string wynik = "lubi";
	assert(najkrotsze(napis) == wynik);
}


int main() {
	test1();
	test2();
	return 0;
}


