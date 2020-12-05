#include <iostream>
using namespace std;

int main() {
	//Dla pobranej od uzytkownika liczby, 
	//zwroc liczbe cyfr pobranje liczby.

	cout << "Podaj liczbe" << endl;
	int a;
	cin >> a;

	int licznik = 0;
	
	while (a > 0) {
		a = a / 10; 
		licznik++;
	}

	cout << "Podana cyfra sklada sie z " << licznik << " cyfr." << endl;

	return 0;
}
