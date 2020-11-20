#include <iostream>
#include <cmath>

using namespace std;

int main() {

	//Wyznacz wartosc funkcji y = 3x + 10 w zadanym punkcie.

	cout << "podaj x" << endl;
	int x;
	cin >> x;

	cout << "3*x+10" << endl; 
	cout << 3*x+10 << endl;

	
	//Pobierz wspolczynniki a, b oraz punkt x i wyznacz wartosc funkcji y = ax + b w zadanym punkcie.
	
	cout << "podaj a" << endl;
	int a;
	cin >> a;

	cout << "podaj b" << endl;
	int b;
	cin >> b; 

	cout << "podaj x" << endl;
	cin >> x;

	cout << "a*x+b" << endl;
	cout << a*x+b << endl;

	//Wyznacz wartosc funkcji y = x^3 + 2x^2 - 20 w zadanym punkcie.

	cout << "podaj x" << endl;
	cin >> x;

	cout << "y = x**3 + 2x**2 - 20" << endl;
	cout << pow(x,3) + 2*pow(x,2) - 20 << endl;

	//Pobierz wspolczynniki a, b, c, d, m, n oraz punkt x i wyznacz wartosc funkcji y = a*x^m + b*x^n + c - a w zadanym punkcie.
	
	cout << "podaj a" << endl;
	cin >> a;

	cout << "podaj b" << endl;
	cin >> b;

	cout << "podaj c" << endl;
	int c;
	cin >> c;

	cout << "podaj d" << endl;
	int d;
	cin >> d;

	cout << "podaj m" << endl;
	int m;
	cin >> m;

	cout << "podaj n" << endl;
	int n;
	cin >> n;

	cout << "podaj x" << endl;
	cin >> x;

	cout << "a*x**m + b*x**n + c - a" << endl;
	cout << a*pow(x,m)+b*pow(x,n)+c-a << endl;

	//Wyznacz wartosc funkcji y = sin3x*cos2x + e^x^2 + log(x^3+2x^2-x-3) w zadanym punkcie.

	cout << "podaj x" << endl;

	cin >> x;

	cout << "sin(3*x)*cos(2*X) + e**x**2 + log(x**3 + 2*x**2 - x - 3)" << endl;
	cout << sin(3*x)*cos(2*x) + exp(pow(x,2)) + log(pow(x,3) + 2*pow(x,2) - x - 3) << endl;

	return 0;
}
