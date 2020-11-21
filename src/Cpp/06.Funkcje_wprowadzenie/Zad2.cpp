#include <iostream>
#include <string>

using namespace std;

//Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora 
//dla otrzymanych dwoch liczb zwroci: 

//a) ich sume
int suma(int a, int b) {
	return a + b;
}

//b) roznice drugiej i pierwszej
int roznica(int a, int b) {
	return b - a;
}

//c) ich iloczyn
int iloczyn(int a, int b) {
	return a * b;
}

//d) reszte z dzielenia pierwszej przez druga
int reszta(int a, int b) {
	return a % b;
}

int main() {
	cout << "Podaj dwie liczby: " << endl;
	int a;
	cin >> a;
	int b;
	cin >> b;

	cout << "suma liczb to: " << suma(a,b) << endl;
	cout << "roznice drugiej i pierwszej to: " << roznica(a,b) << endl;
	cout << "iloczyn liczb to: " << iloczyn(a,b) << endl;
	cout << "reszte z dzielenia pierwszej przez druga to: " << reszta(a,b) << endl;

	return 0;
}
