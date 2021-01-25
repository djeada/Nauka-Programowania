#include <cassert>
#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//Otrzymujesz napis. Znajdz w otrzymanym napisie wszystkie znaki powtarzajace sie wiecej niz raz.

unordered_map<char, int> budujSlownik(const string& slowo) {
	unordered_map<char, int> slownik;

	for (const auto& znak : slowo)
		slownik[znak]++;

	return slownik;
}

vector<char> znaki(const string& slowo) {

	unordered_map<char, int> slownik = budujSlownik(slowo);
	vector<char> wynik;

	for (auto it = slownik.begin(); it != slownik.end(); it++) {
		if (it->second > 1)
			wynik.push_back(it->first);
	}

	return wynik;
}

bool wektoryRowne(vector<char> v1, vector<char> v2) {
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    return v1 == v2;
}


void test1() {
	string slowo = "podwodny";
	vector<char> wynik {'o', 'd'};

	assert(wektoryRowne(znaki(slowo), wynik));
}

void test2() {
	string slowo = "jedzie pociag z daleka";
	vector<char> wynik {'e', 'a', 'i', 'd', 'z', ' '};

	assert(wektoryRowne(znaki(slowo), wynik));
}

int main() {

	test1();
	test2();

	return 0;
}

