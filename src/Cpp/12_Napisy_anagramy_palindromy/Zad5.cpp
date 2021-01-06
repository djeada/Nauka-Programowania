#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;

//Otrzymujesz napis reprezentujacy zdanie oraz slowo. 
//Znajdz wszystkie anagramy otrzymanego slowa w zdaniu. 
//Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.

void naMale(string& slowo) {
    transform(slowo.begin(), slowo.end(), slowo.begin(), ::tolower); 
}

bool anagram(string s1, string s2) {

	int N = s1.length();
	int M = s2.length();

	if(N != M) return false;

	int pom[256] = {0};

	for (const auto& znak : s1)
		pom[znak]++;

	for (const auto& znak : s2)
		pom[znak]--;

	for (const auto& x : pom) {
		if (x != 0) 
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

vector<string> anagramyV1(const string& zdanie, const string& napis) {
	vector<string> wynik;
	int pocz = 0; 
	int konc = 0;
	while ((konc = zdanie.find(' ', pocz)) != string::npos) {
		if (konc != pocz) {
			auto slowo = zdanie.substr(pocz, konc - pocz);
			wyczysc(slowo);
			naMale(slowo);
			if (!slowo.empty() && anagram(slowo, napis))
				wynik.push_back(slowo);
		}
		pocz = konc + 1;
	}
	if (konc != pocz) {
		auto slowo = zdanie.substr(pocz);
		wyczysc(slowo);
		naMale(slowo);
		if (!slowo.empty()  && anagram(slowo, napis))
			wynik.push_back(slowo);

	}

	return wynik;
}

void test1() {
	string zdanie = "Za jego nikczemne uczynki, spotakla go wysoce sroga kara.";
	string slowo = "arak";
	vector<string> wynik({"kara"});
	assert(anagramyV1(zdanie, slowo) == wynik);
}

int main() {
	test1();
    
	return 0;
}


