#include <iostream>

using namespace std;

int main() {


	//Czy liczba jest numerem tygodnia/miesiąca?
	
	cout << "podaj liczbe:" << endl;
	int a;
	cin >> a; 

	if (a >= 1 && a <= 7)
		cout << "Liczba jest poprawnym numerem tygodnia" << endl;

	else
		cout << "Liczba nie jest poprawnym numerem tygodnia" << endl;

	if (a >= 1 && a <= 12)
		cout << "Liczba jest poprawnym numerem miesiaca" << endl;
	else
		cout << "Liczba nie jest poprawnym numerem miesiaca" << endl;
	
	return 0;
}

