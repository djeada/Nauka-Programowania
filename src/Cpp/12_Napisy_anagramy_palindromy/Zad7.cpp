#include <string>
#include <algorithm>
#include <cassert>
#include <unordered_map>

//Dla dwoch slow, ile minimalnie znakow musimy usunac 
//aby uzyskac anagramy. Zwroc -1 dla slow, o roznych 
//dlugosciach.


std::unordered_map<char, int> histogram(const std::string& slowo) {
    std::unordered_map<char, int> histo;
    
    for (auto znak : slowo)
        histo[znak]++;

    return histo;
}

int liczbaZnakowV1(const std::string& slowoA, const std::string& slowoB) {
	if (slowoA.size() != slowoB.size())
		return -1;

	std::unordered_map<char, int> histoSlowaA = histogram(slowoA);
	std::unordered_map<char, int> histoSlowaB = histogram(slowoB);
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
	std::string slowoA = "grazyna";
	std::string slowoB = "razynax";
	int wynik = 2;
	assert(liczbaZnakowV1(slowoA, slowoB) == wynik); 
}

void test2() {
	std::string slowoA = "pan cytryna";
	std::string slowoB = "pan pomarancza";
	int wynik = -1;
	assert(liczbaZnakowV1(slowoA, slowoB) == wynik); 
}

void test3() {
	std::string slowoA = "20ejdy0978oa";
	std::string slowoB = "akv81w39j1ob";
	int wynik = 12;
	assert(liczbaZnakowV1(slowoA, slowoB) == wynik); 

}

int main() {

	test1();
	test2();
	test3();

	return 0;
}

