#include <iostream>

using namespace std;

//Napisz funkcje, ktora dla otrzymanej liczby
//wypisze litere X, o wysokosci rownej 
//otrzymanej liczbie.

void literaX(int n) {

	for (int y = 0; y < n; y++) {
		for (int x = 0; x < n; x++) {
 			if (y == x || x == (n - 1 - y)) 
				cout << "*";  
			else
				cout << " ";
		}
		cout << endl;
	}
}

int main () {

	int a = 5;
	literaX(a);
	
	return 0;
}


