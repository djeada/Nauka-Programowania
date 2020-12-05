#include <iostream>

using namespace std;

int main() {

	//Dla pobranych trzech liczb, wypisz je w kolejnosci rosnacej.
	
	cout << "podaj trzy liczby:" << endl;
	int a;
	cin >> a;
	int b;
	cin >> b;
	int c;
	cin >> c; 

	if (a >= b && a >= c) {
		if (b >= c)
			cout << c << b << a << endl;
		else
			cout << b << c << a << endl;
	}

	else if (c >= b && c >= a) {
		if (a >= b)
			cout << b << a << c << endl;
		else
			cout << a << b << c << endl;
	}
	else{
		if (a >= c)
			cout << c << a << b << endl;
		else
			cout << a << c << b << endl;
	}
	return 0;
}

