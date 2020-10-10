/*
Suma liczb naturalnych mniejszych od N.
*/

#include <cassert>

int sumaV1(int N) { 
	
	if (N <= 0)
		return 0;

	return N + sumaV1(N - 1);
}

int main() {
	int N = 10;
	int wynik = 55;
	
	assert(sumaV1(N) == wynik);
	
    return 0;
}

