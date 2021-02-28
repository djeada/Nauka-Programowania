#include <vector>
#include <cassert>
#include <unordered_set>
#include <algorithm>

//Otrzymujesz liste liczb. Usun z niej wszystkie duplikaty.
//Tylko pierwsze wystapienie danej wartosci powinno zostac zachowane.

//Zlozonosc czasowa O(nlogn)
void usunDuplikatyV1(std::vector<int>& lista) {
  	sort(lista.begin(), lista.end());
	lista.erase(unique( lista.begin(), lista.end()), lista.end());
}

//Zlozonosc czasowa O(n)
//Zlozonosc pamieciowa O(n)
void usunDuplikatyV2(std::vector<int>& lista) {
	std::unordered_set<int> zbior;
	for (auto liczba : lista)
		zbior.insert(liczba);

	lista.assign(zbior.begin(), zbior.end());
}

//Zlozonosc czasowa O(n)
//Zlozonosc pamieciowa O(n)
void usunDuplikatyV3(std::vector<int>& lista) {
	std::vector<int> pom;

	auto i = lista.begin();
	while (i != lista.end()) {
		if (find (pom.begin(), pom.end(), *i) != pom.end())
			i = lista.erase(i);
		else {
			pom.push_back(*i);
			++i;
		}
	}
}

bool wektoryRowne(std::vector<int>& v1, std::vector<int>& v2) {
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	return v1 == v2;
}

void test1() {
	std::vector<int> lista {3, 5, 3, 3, 2};
    	std::vector<int> wynik {3, 5, 2};	

	usunDuplikatyV1(lista);
	assert(wektoryRowne(lista, wynik));
}

void test2() {
	std::vector<int> lista {3, 5, 3, 3, 2};
    	std::vector<int> wynik {3, 5, 2};	

	usunDuplikatyV2(lista);
	assert(wektoryRowne(lista, wynik));
}

void test3() {
	std::vector<int> lista {3, 5, 3, 3, 2};
    	std::vector<int> wynik {3, 5, 2};	

	usunDuplikatyV3(lista);
	assert(wektoryRowne(lista, wynik));
}

int main() {

	test1();
	test2();
	test3();	

	return 0;
}
