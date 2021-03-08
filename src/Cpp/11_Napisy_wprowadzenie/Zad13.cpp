#include <cassert>
#include <string>
#include <vector>
#include <cmath>

//Otrzymujesz zdanie. Znajdz znaki znajdujace 
//sie na pozycjach bedacych liczbami pierwszymi.

bool czyPierwsza(int n) {

	if (!(n % 2) && n != 2)
		return false;
	
	for (int i = 3; i <= sqrt((double)n); i += 2) {
		if (!(n % i))
			return false;
	}
	
	return true;
}

std::vector<char> znaki(const std::string& napis) {
	
	std::vector<char> znaki;

	for (unsigned int i = 0; i < napis.size(); i++) {
		if (czyPierwsza(i))
			znaki.push_back(napis[i]);
	}

	return znaki;
}

void test1() {
	std::string napis = "Kaczka lubi wiosne.";
	std::vector<char> wynik {'a','c','z','a', 'l',' ','i','e'};
	assert(znaki(napis) == wynik);
}

int main() {
	test1();
	return 0;
}


