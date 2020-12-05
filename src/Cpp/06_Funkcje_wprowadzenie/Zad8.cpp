#include <iostream>
#include <limits>

using namespace std;

//Napisz funkcje realizujaca zaokraglanie ilorazu bez uzycia '/' i '%'.

int podziel(int a, int b) {
	
	int znak = 1;
	int licznik = 0;

	if (b == 0)
		return numeric_limits<int>::signaling_NaN();
	
	if (a == 0)
		return 0;

	if (a < 0) {
		znak = -1;
		a = -a;
	}
	
	if (b < 0) {
		znak *= -1;
		b = -b;
	}	

	if (znak == 1) {
		licznik = 0; 
		while (a >= b) {
			a -= b;
			licznik += 1;
		}
	}	

	else {
		licznik = 1; 
		while (a > b) {
			a -= b;
			licznik += 1;
		}
	}
		
	return licznik*znak;
}

int main() {
	cout << "Podaj dwie liczby: " << endl;
	int a;
	cin >> a;
	int b;
	cin >> b;

	cout << "iloraz pierwszej przez druga to: " <<  podziel(a,b) << endl;

	return 0;
}
