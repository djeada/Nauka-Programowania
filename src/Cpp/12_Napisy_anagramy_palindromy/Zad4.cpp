#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

//Otrzymujesz napis reprezentujacy zdanie. 
//Znajdz wszystkie palindromy w zdaniu.
//Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.

void naMale(std::string& slowo) {
    transform(slowo.begin(), slowo.end(), slowo.begin(), ::tolower); 
}

bool palindrom(std::string& slowo) {
	int N = slowo.length() - 1;
	for (int i = 0; i <= N/2; i++) {
		if (slowo[i] != slowo[N - i])
			return false;
	}

	return true;
}

void wyczysc(std::string& napis){
	auto it = napis.begin();

	while (it != napis.end()) {
		if (ispunct(*it))
			napis.erase(it);
		else
			it++;
	}
}

std::vector<std::string> palindromyV1(std::string& napis) {
	std::vector<std::string> wynik;
	unsigned int pocz = 0; 
	unsigned int konc = 0;
	while ((konc = napis.find(' ', pocz)) != std::string::npos) {
		if (konc != pocz) {
			auto slowo = napis.substr(pocz, konc - pocz);
			wyczysc(slowo);
			naMale(slowo);
			if (!slowo.empty() && palindrom(slowo))
				wynik.push_back(slowo);
		}
		pocz = konc + 1;
	}
	if (konc != pocz) {
		auto slowo = napis.substr(pocz);
		wyczysc(slowo);
		naMale(slowo);
		if (!slowo.empty() && palindrom(slowo))
			wynik.push_back(slowo);

	}

	return wynik;
}

void test1() {
	std::string napis = "Tata zbaral kajak na wycieczke i uderzyl sie w oko";
	std::vector<std::string> wynik({"kajak", "i", "w", "oko"});
	assert(palindromyV1(napis) == wynik);
}

int main() {
	test1();
    
	return 0;
}


