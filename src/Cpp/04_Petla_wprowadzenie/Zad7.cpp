#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	//Dla pobranej liczby, wyswietl liczbe Pi podniesiona 
	//do potegi rownej pobranej liczbie. Wynik powinien byc
	//zaokraglony do dwoch miejsc po przecinku.

	cout << "Podaj liczbe: " << endl;
	int n;
	cin >> n;
	
	cout << fixed << setprecision(2);

	int wynik = 1;
	for (int i = 0; i < n; i++)
		wynik *= 3.14;

	cout << wynik << endl;

	return 0;
}
