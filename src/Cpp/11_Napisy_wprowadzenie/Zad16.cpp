#include <cassert>
#include <string>
#include <algorithm>

using namespace std;

//Odleglosc Hamminga to miara odmiennosci dwoch napisow o takiej samej 
//dlugosci, zdefiniowana jako liczba pozycji na ktorych napisy maja rozne 
//znaki.

int odlegloscHammingaV1(const string& napisA, const string& napisB) {
	if (napisA.size() != napisB.size())
		return -1;
		
	int wynik = 0;
	
	for (int i = 0; i < napisA.size(); i++) {
		if (napisA[i] != napisB[i])
			wynik++;
	}
			
	return wynik;
}

void test1() {
	string napisA = "xxbab";
	string napisB = "bbabb";
	int wynik = 4;
	assert(odlegloscHammingaV1(napisA, napisB) == wynik);
}

void test2() {
	string napisA = "xxbab";
	string napisB = "bbabb";
	int wynik = 4;
	assert(odlegloscHammingaV1(napisA, napisB) == wynik);
}

int main() {
	test1();
	test2();
	return 0;
}


