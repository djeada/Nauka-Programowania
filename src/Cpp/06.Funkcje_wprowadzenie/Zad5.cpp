#include <cmath>
#include <iostream>

using namespace std;

//Napisz funkcje, ktora zamieni wartosci miejscami.

int swap(int& a, int& b) {
	int c = a;
	a = b;
	b = c;
}

int main() {
	cout << "Podaj dwie liczby: " << endl;
	int a;
	cin >> a;
	int b;
	cin >> b;

	swap(a, b);
	cout << "Liczby zamienione miejscami to: " << a << " " << b << endl;

	return 0;
}
