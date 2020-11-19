#include <cassert>
#include <iostream>
/*
Liczba Fibonacciego.	
*/

int fibonnaciV1(int n) { 
	
	if(n == 0 || n == 1) 
		return n;
	
	return fibonnaciV1(n-1) + fibonnaciV1(n-2);
}

int fibonnaciV2(int n) {
	static int pom[100] = {0};

	if (pom[n] != 0) 
		return pom[n];

	if (n == 0 || n == 1) {
		pom[n] = n;
		return pom[n];
	}

	pom[n] = fibonnaciV2(n-1) + fibonnaciV2(n-2);

	return pom[n];
}

int main() {
	int n = 7;
	int wynik = 13;

	assert(fibonnaciV1(n) == wynik);
	assert(fibonnaciV2(n) == wynik);
	
    return 0;
}

