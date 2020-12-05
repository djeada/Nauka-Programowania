#include <iostream>
#include <cassert>

using namespace std;

//Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci
//ich najwiekszy wspolny dzielnik.

int nwdV1(int a, int b) {

	if (b == 0) 
		return a;
 
	return nwdV1(b, a % b);
}

int nwdV2(int a, int b) {

	int c;
	
	while (b != a % b) {
	    c = b;
	    b = a % b;
	    a = c;
	    
	   if ( b == 0) 
		   break;
	}

	return a;
}

int main () {

	int a = 14;
	int b = 21;
	int wynik = 7;

	assert(nwdV1(a, b) == wynik);
	assert(nwdV2(a, b) == wynik);
	
	return 0;
}


