#include <iostream>
#include <numbers>
#include <iomanip>

using namespace std;

int main() {

	//Dla pobranej liczby, wyswietl liczbe Pi tyle razy 
	//ile wynosi pobrana liczba, z dokladnoscia do tylu 
	//miejsc po przecinku ile wynosi pobrana liczba.
	
	cout << "Podaj liczbe: " << endl;
	int n;
	cin >> n;

	cout << fixed << setprecision(n);

	for (int i = 0; i < n; i++)
		cout << numbers::pi << " ";

	return 0;
}

//g++-10 -Wall -Wextra -std=c++20 Zad3.cpp -o exe
