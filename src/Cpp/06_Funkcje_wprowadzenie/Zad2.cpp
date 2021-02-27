#include <iostream>
#include <string>

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
	std::cout << "Podaj dwie liczby: " << std::endl;
	int a;
	std::cin >> a;
	int b;
	std::cin >> b;

	std::cout << "suma liczb to: " << suma(a,b) << std::endl;
	std::cout << "roznice drugiej i pierwszej to: " << roznica(a,b) << std::endl;
	std::cout << "iloczyn liczb to: " << iloczyn(a,b) << std::endl;
	std::cout << "reszte z dzielenia pierwszej przez druga to: " << reszta(a,b) << std::endl;

	return 0;
}
