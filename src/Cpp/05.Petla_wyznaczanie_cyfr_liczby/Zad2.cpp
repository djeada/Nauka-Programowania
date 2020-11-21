#include <iostream>
using namespace std;

int main() {

	//Dla pobranej liczby, powinny zostac zwrocone 
	//cyfry pobranej liczby poczynajac od cyfry jednosci.

	cout << "Podaj liczbe" << endl;
	int a;
	cin >> a;
	
	while (a > 0) {
		cout << a % 10 << endl;
		a = a / 10; 
	}

	return 0;
}
