#include <cassert>
#include <unordered_map>

using namespace std;

//Otrzymujesz slownik par napisow i liczb oraz pojedyncza liczbe. 
//Usuń ze slownika pary, dla ktorcyh liczba w parze jest rowna otrzymanej liczbie.
void usun(unordered_map<string, int>& slownik, int liczba) {
	
	auto it = slownik.begin();

	while (it != slownik.end()) {
		
		if (it->second == liczba)
			it = slownik.erase(it);
	
		else
			it++;
	}
}

void test1() {

	unordered_map<string, int> slownik {{"aaa", 5}, {"abc", 1}, {"xxx", 5}, {"cba", 3}};
	int liczba = 5;
	
	unordered_map<string, int> wynik {{"abc", 1}, {"cba", 3}};

	usun(slownik, liczba);

	assert(slownik == wynik);
}

void test2() {
	unordered_map<string, int> slownik {{"slownik", 3}, {"word", 3}, {"lll", 3}, {"mmn", 1}};
	int liczba = 3;
	
	unordered_map<string, int> wynik {{"mmn", 1}};

	usun(slownik, liczba);

	assert(slownik == wynik);
}

int main() {

	test1();
	test2();

	return 0;
}

