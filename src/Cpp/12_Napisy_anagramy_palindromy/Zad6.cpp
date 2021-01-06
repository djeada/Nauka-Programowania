#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

/*
Znajdz wszystkie permutacje slowa.
*/

bool palindrom(string& slowo) {
	int N = slowo.length() - 1;
	for (int i = 0; i <= N/2; i++) {
		if (slowo[i] != slowo[N - i])
			return false;
	}

	return true;
}

void permutacja (string& slowoWej, string& slowoWyj, vector<string>& wynik) {
	if (slowoWej.empty() && palindrom(slowoWyj) &&
		 find(wynik.begin(), wynik.end(), slowoWyj) == wynik.end()) {
		wynik.push_back(slowoWyj);
		return;
	}

	for (int i = 0; i < slowoWej.length(); ++i) {
		string noweSlowoWej = slowoWej;
		string noweSlowoWyj = slowoWyj;
		noweSlowoWej .erase(i,1);
		noweSlowoWyj += slowoWej.at(i);
		permutacja (noweSlowoWej, noweSlowoWyj, wynik);
	}
}

vector<string> permutacje(string& slowoWej) {
	
	vector<string> wynik;

	string slowoWyj;  
	permutacja(slowoWej, slowoWyj, wynik);
	
	return wynik;
}

bool wektoryRowne(vector<string> v1, vector<string> v2) {
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    return v1 == v2;
}

void test1() {
	string slowo = "adamm";
	vector<string> wynik {"madam", "amdma"};
	assert( wektoryRowne( permutacje(slowo), wynik)); 
}

int main() {
	test1();
	return 0;
}

