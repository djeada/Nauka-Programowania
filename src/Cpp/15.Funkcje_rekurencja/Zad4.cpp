#include <cassert>

/*
Silnia.	
*/

int silniaV1(int n) { 
	
	if(n == 0 || n == 1) 
		return 1;

	return n * silniaV1(n-1);
}

int main() {
	int n = 3;
	int wynik = 6;
	
	assert(silniaV1(n) == wynik);
	
    return 0;
}

