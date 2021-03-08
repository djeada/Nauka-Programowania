#include <cassert>
#include <string>
#include <algorithm>
#include <vector>

//Otrzymujesz napis reprezentajacy zdanie. 
//Zwroc liste skladajaca sie ze slow zdania. 
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

std::vector<std::string> slowaV1(std::string& napis) {
	std::vector<std::string> wynik;
	unsigned int pocz = 0; 
	unsigned int konc = 0;
	while ((konc = napis.find(' ', pocz)) != std::string::npos) {
		if (konc != pocz) {
			auto slowo = napis.substr(pocz, konc - pocz);
			wyczysc(slowo);
			if (!slowo.empty())
				wynik.push_back(slowo);
		}
		pocz = konc + 1;
	}
	if (konc != pocz) {
		auto slowo = napis.substr(pocz);
		wyczysc(slowo);
		if (!slowo.empty())
			wynik.push_back(slowo);

	}

	return wynik;
}

void test1() {
	std::string napis = "We think in generalities, but we live in details";
	std::vector<std::string> wynik {"We", "think", "in", "generalities", "but", 
				"we", "live", "in", "details"};
	assert(slowaV1(napis) == wynik);
}

void test2() {
	std::string napis = "";
	std::vector<std::string> wynik;
	assert(slowaV1(napis) == wynik);
}

int main() {
	test1();
	test2();
	return 0;
}


