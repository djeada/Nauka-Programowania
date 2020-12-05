#include <iostream>
#include <cassert>

using namespace std;

//Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci
//ich najmniejsza wspolna wielokrotnosc.

int nwd(int a, int b) {

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

int nww(int a, int b) {
	return a * b / nwd(a, b);
}

int main () {

	int a = 14;
	int b = 21;
	int wynik = 42;

	assert(nww(a, b) == wynik);
	
	return 0;
}


