#include <cassert>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

//Otrzymujesz napis reprezentajacy zdanie. 
//Zwroc liste skladajaca sie ze slow zdania. 
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

vector<string> slowaV1(string& napis) {
	vector<string> wynik;
	int pocz = 0; 
	int konc = 0;
	while ((konc = napis.find(' ', pocz)) != string::npos) {
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
	string napis = "We think in generalities, but we live in details";
	vector<string> wynik({"We", "think", "in", "generalities", "but", 
				"we", "live", "in", "details"});
	assert(slowaV1(napis) == wynik);
}

void test2() {
	string napis = "";
	vector<string> wynik;
	assert(slowaV1(napis) == wynik);
}


int main() {
	test1();
	test2();
	return 0;
}


