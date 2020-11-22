#include <iostream>

using namespace std;

//Napisz funkcje, ktora dla otrzymanej liczby 
//wypisze kwadrat o boku rownym otrzymanej liczbie.

void kwadrat(int a) {

	for (int y = 0; y < a; y++) {
		for (int x = 0; x < a; x++)
			cout << "x";
		cout << endl;
	}

}

int main () {

	int a = 5;
	kwadrat(a);
	
	return 0;
}


