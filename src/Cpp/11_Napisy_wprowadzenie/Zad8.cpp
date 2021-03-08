#include <cassert>
#include <algorithm>
#include <vector>
#include <iostream>

//Otrzymujesz napis reprezuntajacy zdanie.
//Podziel zdanie na slowa skladowe. 
//Znaki interpunkcyjne nie sa liczone jako slowa.

void wyczysc(std::string& napis){
	auto it = napis.begin();

	while (it != napis.end()) {
		if (ispunct(*it))
			napis.erase(it);
		else
			it++;
	}
}

void slowaV1(std::string& napis) {
	unsigned int pocz = 0; 
	unsigned int konc = 0;
	while ((konc = napis.find(' ', pocz)) != std::string::npos) {
		if (konc != pocz) {
			auto slowo = napis.substr(pocz, konc - pocz);
			wyczysc(slowo);
			if (!slowo.empty())
				std::cout << slowo << std::endl;
		}
		pocz = konc + 1;
	}
	if (konc != pocz) {
		auto slowo = napis.substr(pocz);
		wyczysc(slowo);
		if (!slowo.empty())
			std::cout << slowo << std::endl;

	}
}

int main() {
	std::string napis = "We think in generalities, but we live in details";
	slowaV1(napis);
	return 0;
}

