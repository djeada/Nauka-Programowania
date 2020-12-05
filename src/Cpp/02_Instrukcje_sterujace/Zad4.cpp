#include <iostream>

using namespace std;

int main() {


	//Dla dwoch pobranych liczb, wypisz najpierw wieksza potem mniejsza.
	
	cout << "podaj dwie liczby:" << endl;
	int a;
	cin >> a;
	int b;
	cin >> b; 
	if (a > b) {
		cout << a << endl;
		cout << b << endl;
		cout << "pierwsza liczba jest wieksza od drugiej" << endl;

	}
		
	else {
		cout << b << endl;
		cout << a << endl;
		cout << "pierwsza liczba nie jest wieksza od drugiej" << endl;

	}	
	
	return 0;
}

