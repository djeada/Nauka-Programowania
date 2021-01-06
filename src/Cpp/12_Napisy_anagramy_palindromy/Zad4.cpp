#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;

//Otrzymujesz napis reprezentujacy zdanie. 
//Znajdz wszystkie palindromy w zdaniu.
//Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.

void naMale(string& slowo) {
    transform(slowo.begin(), slowo.end(), slowo.begin(), ::tolower); 
}

bool palindrom(string& slowo) {
	int N = slowo.length() - 1;
	for (int i = 0; i <= N/2; i++) {
		if (slowo[i] != slowo[N - i])
			return false;
	}

	return true;
}

void wyczysc(string& napis){
	auto it = napis.begin();

	while (it != napis.end()) {
		if (ispunct(*it))
			napis.erase(it);
		else
			it++;
	}
}

vector<string> palindromyV1(string& napis) {
	vector<string> wynik;
	int pocz = 0; 
	int konc = 0;
	while ((konc = napis.find(' ', pocz)) != string::npos) {
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
	string napis = "Tata zbaral kajak na wycieczke i uderzyl sie w oko";
	vector<string> wynik({"kajak", "i", "w", "oko"});
	assert(palindromyV1(napis) == wynik);
}

int main() {
	test1();
    
	return 0;
}


