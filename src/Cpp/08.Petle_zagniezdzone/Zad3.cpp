#include <iostream>

using namespace std;

//Napisz funkcje, ktora dla otrzymanej liczby 
//wypisze zaczyajac od podstawy trojkat prostokatny 
//rownoboczny o wysokosci rownej otrzymanej liczbie.

void trojkat(int a) {

	for (int y = 0; y < a; y++) {
		for (int x = 0; x < a - y; x++)
			cout << "x";
		cout << endl;
	}
}

int main () {

	int a = 5;
	trojkat(a);
	
	return 0;
}


