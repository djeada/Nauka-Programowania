#include <iostream>

using namespace std;

//Napisz funkcje, ktora dla otrzymanej liczby N
//wypisze N pierwszych wierszy i kolumn 
//tabliczki mnozenia.

void tabliczkaMnozenia(int n) {

	for (int y = 1; y <= n; y++) {
		for (int x = 1; x <= n; x++)
			cout << y*x << " ";
		cout << endl;
	}
}

int main () {

	int a = 5;
	tabliczkaMnozenia(a);
	
	return 0;
}


