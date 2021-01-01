#include <vector>
#include <cassert>
#include <unordered_set>
#include <algorithm>

using namespace std;

//Otrzymujesz liste liczb. Usun z niej wszystkie duplikaty.
//Tylko pierwsze wystapienie danej wartosci powinno zostac zachowane.

//Zlozonosc czasowa O(nlogn)
void usunDuplikatyV1(vector<int>& lista) {
  	sort(lista.begin(), lista.end());
	lista.erase(unique( lista.begin(), lista.end()), lista.end());
}

//Zlozonosc czasowa O(n)
//Zlozonosc pamieciowa O(n)
void usunDuplikatyV2(vector<int>& lista) {
	unordered_set<int> zbior;
	for (auto liczba : lista)
		zbior.insert(liczba);

	lista.assign(zbior.begin(), zbior.end());
}

//Zlozonosc czasowa O(n)
//Zlozonosc pamieciowa O(n)
void usunDuplikatyV3(vector<int>& lista) {
	vector<int> pom;

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

bool wektoryRowne(vector<int>& v1, vector<int>& v2) {
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    return v1 == v2;
}

int main() {

    	vector<int> lista({3, 5, 3, 3, 2});
    	vector<int> wynik({3, 5, 2});	

	vector<int> kopia(lista);
	usunDuplikatyV1(kopia);
	assert(wektoryRowne(kopia, wynik));

	kopia = lista;
	usunDuplikatyV2(kopia);
	assert(wektoryRowne(kopia, wynik));

	kopia = lista;
	usunDuplikatyV3(kopia);
	assert(wektoryRowne(kopia, wynik));

	return 0;
}
