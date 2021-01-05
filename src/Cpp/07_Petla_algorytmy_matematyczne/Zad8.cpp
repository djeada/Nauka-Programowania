#include <iostream>
#include <cassert>
#include <cmath>

using namespace std;

//Napisz funkcje, ktora dla otrzymanej liczby sprawdzi
//czy jest ona liczba pierwsza.

bool czyPierwsza(int n) {

	if (!(n % 2) && n != 2)
		return false;
	
	for (int i = 3; i <= sqrt((double)n); i += 2) {
		if (!(n % i))
			return false;
	}
	
	return true;
}

int main () {

	int a = 15;
	assert(!czyPierwsza(a));
	
	a = 7;
	assert(czyPierwsza(a));
	
	return 0;
}


