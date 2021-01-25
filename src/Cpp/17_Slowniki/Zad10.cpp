#include <cassert>
#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//Otrzymujesz tekst w postaci napisu. Znajdz czestosc wystepowania kazdego ze slow w tekscie. 
//Zignoruj roznice miedzy malymi i wielkimi literami. Pamietaj, slowa skladaja sie wylacznie z liter!
void wyczysc(string& napis){
	auto it = napis.begin();

	while (it != napis.end()) {
		if (ispunct(*it))
			napis.erase(it);
		else
			it++;
	}
}

void naMale(string& slowo) {
    transform(slowo.begin(), slowo.end(), slowo.begin(), ::tolower); 
}

vector<string> rozdzielSlowa(const string& napis) {
	vector<string> wynik;
	int pocz = 0; 
	int konc = 0;
	while ((konc = napis.find(' ', pocz)) != string::npos) {
		if (konc != pocz) {
			auto slowo = napis.substr(pocz, konc - pocz);
			wyczysc(slowo);
			naMale(slowo);
			if (!slowo.empty())
				wynik.push_back(slowo);
		}
		pocz = konc + 1;
	}
	if (konc != pocz) {
		auto slowo = napis.substr(pocz);
		wyczysc(slowo);
		naMale(slowo);
		if (!slowo.empty())
			wynik.push_back(slowo);

	}

	return wynik;
}

unordered_map<char, int> budujSlownik(const string& slowo) {
	unordered_map<char, int> slownik;

	for (const auto& znak : slowo)
		slownik[znak]++;

	return slownik;
}

vector<vector<string>> znajdzAnagramy(const string& tekst) {

	auto slowa = rozdzielSlowa(tekst);
	
	vector<vector<string>> wynik;

	auto it = slowa.begin();

	while (it != slowa.end()) {
		auto it2 = it;
		auto slowo = *it;
		auto histogram = budujSlownik(slowo);
		
		vector<string> anagramy {slowo};

		it2++;
		while (it2 != slowa.end()) {
			slowo = *it2;

			if (histogram == budujSlownik(slowo)) {
				if (find(anagramy.begin(), anagramy.end(), slowo) == anagramy.end())
					anagramy.push_back(slowo);
				it2 = slowa.erase(it2);
			}
			else
				it2++;
		}


		if (anagramy.size() > 1)
			wynik.push_back(anagramy);

		it = slowa.erase(it);
	}

	return wynik;
}


void test1() {
	string slowo = "To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. "
			"Burza nad galeria i alergia na narty to zadna zbrodnia, jak bandzior i jego arbuz.";
	
	vector<vector<string>> wynik {{"absurd", "brudas"}, {"tyran", "narty"}, {"bandzior", "zbrodnia"}, {"burza", "arbuz"}, {"galeria", "alergia"}};

	auto anagramy = znajdzAnagramy(slowo);
	assert(equal(anagramy.begin(), anagramy.end(), wynik.begin()));
}

void test2() {
	string slowo = "I love the way sometimes the letters of an anagram rearrange themselves in my "
			"head with no effort, whereas sometimes I have to write them out in a circle to work it out.";
	
	vector<vector<string>> wynik;

	auto anagramy = znajdzAnagramy(slowo);
	assert(equal(anagramy.begin(), anagramy.end(), wynik.begin()));
}

int main() {

	test1();
	test2();

	return 0;
}

