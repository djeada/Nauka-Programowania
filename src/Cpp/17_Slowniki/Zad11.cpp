#include <cassert>
#include <unordered_map>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

//Otrzymujesz dwie listy. Zbuduj slownik skladajacy się z kluczy będacych 
//elementami pierwszej listy i wartosciami będacymi elementami drugiej listy. 
//Jesli listy sa roznej dlugosci zwroc pusty slownik.

bool porownujKlucze(const pair<string, int>& a, const pair<string, int>& b) { 
	return a.first < b.first; 
} 

vector<pair<string, int>> sortujWzgledemKluczy(const unordered_map<string, int>& slownik) { 

	vector<pair<string, int>> wynik;

	for (const auto& it : slownik)
		wynik.push_back(pair<string, int>(it.first, it.second));

	sort(wynik.begin(), wynik.end(), porownujKlucze); 

	return wynik;
}

bool porownujWartosci(const pair<string, int>& a, const pair<string, int>& b) { 
	return a.second < b.second; 
}
  
vector<pair<string, int>> sortujWzgledemWartosci(const unordered_map<string, int>& slownik) { 

	vector<pair<string, int>> wynik;

	for (const auto& it : slownik)
		wynik.push_back(pair<string, int>(it.first, it.second));

	sort(wynik.begin(), wynik.end(), porownujWartosci); 

	return wynik;
}

void test1() {

	unordered_map<string, int> slownik {{"c", 3}, {"x", 5}, {"a", -2}, {"b", 4}};
	vector<pair<string, int>> wynik {{"a", -2}, {"c", 3}, {"b", 4}, {"x", 5}};

	assert(sortujWzgledemWartosci(slownik) == wynik);
}

void test2() {
	unordered_map<string, int> slownik {{"c", 3}, {"x", 5}, {"a", -2}, {"b", 4}};
	vector<pair<string, int>> wynik {{"a", -2}, {"b", 4}, {"c", 3}, {"x", 5}};

	assert(sortujWzgledemKluczy(slownik) == wynik);
}

int main() {

	test1();
	test2();

	return 0;
}
