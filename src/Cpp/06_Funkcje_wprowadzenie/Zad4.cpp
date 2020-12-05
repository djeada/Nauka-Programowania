#include <cmath>
#include <iostream>

using namespace std;

//Napisz funkcje, ktora:

//a) dla podanych dwoch liczb, zwroci mniejsza
int min2(int a, int b) {
	return a < b ? a : b;
}

//b) dla podanych dwoch liczb, zwroci wieksza
int maks2(int a, int b) {
	return a > b ? a : b;
}

//c) dla podanych trzech liczb, zwroci najmniejsza
int min3(int a, int b, int c) {
	int minAB = a < b ? a : b;
	return minAB < c ? minAB : c;
}

//d) dla podanych trzech liczb, zwroci najwieksza
int maks3(int a, int b, int c) {
	int maksAB = a > b ? a : b;
	return maksAB > c ? maksAB : c;
}

int main() {
	cout << "Podaj dwie liczby: " << endl;
	int a;
	cin >> a;
	int b;
	cin >> b;

	cout << "mniejsza liczba to: " << min2(a, b) << endl;
	cout << "wieksza liczba to: " << maks2(a, b) << endl;

	cout << "Podaj trzy liczby: " << endl;
	cin >> a;
	cin >> b;
	int c;
	cin >> c;

	cout << "najmniejsza liczba to: " << min3(a, b, c) << endl;
	cout << "najwieksza liczba to " << maks3(a, b, c) << endl;

	return 0;
}
