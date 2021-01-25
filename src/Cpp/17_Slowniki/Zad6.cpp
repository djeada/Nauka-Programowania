#include <cassert>
#include <unordered_map>
#include <string>

using namespace std;

// Otrzymujesz napis. Znajdz czestosc wystepowania znakow w otrzymanym napisie.

unordered_map<char, int> budujSlownik(const string& slowo) {
	unordered_map<char, int> slownik;

	for (const auto& znak : slowo)
		slownik[znak]++;

	return slownik;
}

void test1() {
	string slowo = "klasa";
	unordered_map<char, int> wynik {{'k', 1}, {'l', 1}, {'a', 2}, {'s', 1}};

	assert(budujSlownik(slowo) == wynik);
}

void test2() {
	string slowo = "robot";
	unordered_map<char, int> wynik {{'r', 1}, {'o', 2}, {'b', 1}, {'t', 1}};

	assert(budujSlownik(slowo) == wynik);
}

int main() {

	test1();
	test2();

	return 0;
}

