#include <cassert>
#include <string>
#include <algorithm>

//Odleglosc Hamminga to miara odmiennosci dwoch napisow o takiej samej 
//dlugosci, zdefiniowana jako liczba pozycji na ktorych napisy maja rozne 
//znaki.

int odlegloscHammingaV1(const std::string& napisA, const std::string& napisB) {
	if (napisA.size() != napisB.size())
		return -1;
		
	int wynik = 0;
	
	for (unsigned int i = 0; i < napisA.size(); i++) {
		if (napisA[i] != napisB[i])
			wynik++;
	}
			
	return wynik;
}

void test1() {
	std::string napisA = "xxbab";
	std::string napisB = "bbabb";
	int wynik = 4;
	assert(odlegloscHammingaV1(napisA, napisB) == wynik);
}

void test2() {
	std::string napisA = "xxbab";
	std::string napisB = "bbabb";
	int wynik = 4;
	assert(odlegloscHammingaV1(napisA, napisB) == wynik);
}

int main() {
	test1();
	test2();
	return 0;
}


