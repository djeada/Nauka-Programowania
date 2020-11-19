#include <cassert>

/*
Potega.
*/

int potegaV1(int a, int b) { 
	
	if (b == 0) 
		return 1;

	return a * potegaV1(a, b-1);
}

int main() {
	int a = 3;
	int b = 2;
	int wynik = 9;
	
	assert(potegaV1(a, b) == wynik);
	
    return 0;
}

