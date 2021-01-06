#include <cassert>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

//Otrzymujesz napis reprezuntajacy zdanie.
//Podziel zdanie na slowa skladowe. 
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

void slowaV1(string& napis) {
	int pocz = 0; 
	int konc = 0;
	while ((konc = napis.find(' ', pocz)) != string::npos) {
		if (konc != pocz) {
			auto slowo = napis.substr(pocz, konc - pocz);
			wyczysc(slowo);
			if (!slowo.empty())
				cout << slowo << endl;
		}
		pocz = konc + 1;
	}
	if (konc != pocz) {
		auto slowo = napis.substr(pocz);
		wyczysc(slowo);
		if (!slowo.empty())
			cout << slowo << endl;

	}
}

int main() {
	string napis = "We think in generalities, but we live in details";
	slowaV1(napis);
	return 0;
}

