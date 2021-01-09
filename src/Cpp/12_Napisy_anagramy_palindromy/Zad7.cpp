#include <string>
#include <algorithm>
#include <cassert>
#include <unordered_map>

using namespace std;

//Dla dwoch slow, ile minimalnie znakow musimy usunac 
//aby uzyskac anagramy. Zwroc -1 dla slow, o roznych 
//dlugosciach.


unordered_map<char, int> histogram(const string& slowo) {
    unordered_map<char, int> histo;
    
    for (auto znak : slowo)
        histo[znak]++;

    return histo;
}

int liczbaZnakowV1(const string& slowoA, const string& slowoB) {
	if (slowoA.size() != slowoB.size())
		return -1;

	unordered_map<char, int> histoSlowaA = histogram(slowoA);
	unordered_map<char, int> histoSlowaB = histogram(slowoB);
	int licznik = 0;

	for (auto para : histoSlowaA) {
		if (histoSlowaB.count(para.first) == 0)
			licznik++;
		else
			licznik += para.second - histoSlowaB[para.first];
	}

	for (auto para : histoSlowaB) {
		if (histoSlowaA.count(para.first)== 0)
			licznik++;
		else
			licznik += para.second - histoSlowaA[para.first];
	}

	return licznik;
}

void test1() {
	string slowoA = "grazyna";
	string slowoB = "razynax";
	int wynik = 2;
	assert(liczbaZnakowV1(slowoA, slowoB) == wynik); 
}

void test2() {
	string slowoA = "pan cytryna";
	string slowoB = "pan pomarancza";
	int wynik = -1;
	assert(liczbaZnakowV1(slowoA, slowoB) == wynik); 
}

void test3() {
	string slowoA = "20ejdy0978oa";
	string slowoB = "akv81w39j1ob";
	int wynik = 12;
	assert(liczbaZnakowV1(slowoA, slowoB) == wynik); 

}

int main() {
	test1();
	test2();
	test3();
	return 0;
}

