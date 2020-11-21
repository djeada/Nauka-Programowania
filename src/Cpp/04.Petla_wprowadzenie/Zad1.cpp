#include <iostream>
using namespace std;

int main() {
	//Pros uzytkownika o podanie liczby, dopoki 
	//nie zostanie podana liczba 7.

	int a = 0;

	while (a != 7) {
		cout << "Podaj liczbe: " << endl;
		cin >> a;
	}

	return 0;
}
