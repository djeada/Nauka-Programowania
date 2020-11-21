#include <cmath>
#include <iostream>

using namespace std;

//Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora 
//dla otrzymanych dwoch liczb ustali czy:

//a) pierwsza liczba jest wieksza od drugiej
bool czyWieksza(int a, int b) {
	return a > b;
}

//b) czy suma liczb jest mneijsza niz 10
bool czySumaMniejsza(int a, int b) {
	int suma = a + b;
	return suma < 10;
}

//c) czy obie sa nieparzyste
bool czyObieNieparzyste(int a, int b) {
	return a % 2 == 1 && b % 2 == 1;
}

//d) czy wieksza liczba jest mniejsza 
//od pierwszej podniesionej do kwadratu
int wieksza(int a, int b) {
	return a > b ? a : b;
}

bool czyWiekszaNizKwad(int a, int b) {
	return wieksza(a, b) < pow(a, 2);
}

int main() {
	cout << "Podaj dwie liczby: " << endl;
	int a;
	cin >> a;
	int b;
	cin >> b;

	cout << "Pierwsza liczba jest wieksza od drugiej: " << boolalpha << czyWieksza(a,b) << endl;

	cout << "Suma liczb jest mniejsza od 10: " << boolalpha << czySumaMniejsza(a, b) << endl;

	cout << "Obie liczby nieparzyste: " << boolalpha << czyObieNieparzyste(a,b) << endl;

	cout << "Wieksza liczba jest mniejsza od pierwszej podniesionej do kwadratu " 
		<< boolalpha << czyWiekszaNizKwad(a,b) << endl;

	return 0;
}
