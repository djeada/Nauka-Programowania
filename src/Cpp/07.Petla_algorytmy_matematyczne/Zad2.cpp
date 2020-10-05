#include <iostream>
#include <cassert>

using namespace std;

int doPotegi(int a, int b) {
	
	if (b == 0) 
		return 1;
	else 
		return a * doPotegi(a, b - 1);
}

int main () {

	int a = 2;
	int b = 3;
	int wynik = 8;

	assert (doPotegi(a, b) == wynik);

	return 0;
}
