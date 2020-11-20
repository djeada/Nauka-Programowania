#include <iostream>

using namespace std;

int main() {

	//Pobierz podstawe i wysokosc trojkata i wypisz pole. 

	cout << "podaj podstawe i wysokosc trojkata:" << endl;

	float a;
	cin >> a;
	float h;
	cin >> h;

	cout << "pole trojkata o podstawie " << a << " i wysokosci " 
		<< h << " jest rowne " << a*h/2 << endl;

	//Pobierz dlogosci bokow prostokata i wypisz pole.

	cout << "podaj dlugosci bokow prostokata:" << endl;

	cin >> a;
	float b;
	cin >> b;

	cout << "pole prostokata o bokach " << a << " i " << b 
		<< " jest rowne " << a*b << endl;

	return 0;
}
