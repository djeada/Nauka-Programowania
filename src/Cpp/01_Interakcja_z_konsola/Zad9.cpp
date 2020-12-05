#include <iostream>
#include <cmath>
#include<iomanip>

using namespace std;

int main() {

	//Otrzymujesz roczna stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc
	//udzielonego kredytu. Oblicz miesieczna rate oraz calkowity koszt kredytu. 

	cout << "podaj stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc udzielonego kredytu" << endl;

	float stopa;
	cin >> stopa;
	int lata;
	cin >> lata;
	int kredyt; 
	cin >> kredyt;

	float r = stopa / 12 * 0.01;
	int n = lata * 12;

	float rata = kredyt * r * pow((1 + r), n) / (pow((1 + r), n) - 1);

	float c_koszt = rata * n;

	cout << fixed << setprecision(2);
	cout << "rata mieieczna to " << rata << endl;
	cout << "calkowity koszt to " << c_koszt << endl;

	return 0;
}
