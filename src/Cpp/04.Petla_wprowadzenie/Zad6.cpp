#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {

	//Dla pobranej liczby n, wyswietl sume n 
	//pierwszych wyrazow ciagu danego wzorem:
	cout << "Podaj liczbe: " << endl;
	int n;
	cin >> n;

	cout << fixed << setprecision(2);

	//a_n = n/(n+1)
	float suma = 0;
	for(float i = 1; i <= n; i++){
		float a = i/(i + 1);
		suma += a;
	}
	cout << suma << endl;
	
	//a_n = (n^2+5)/n
	suma = 0;
	for (float i = 1; i <= n; i++){
		float a = (pow(i, 2) + 5)/i;
		suma += a;
	}
	cout << suma << endl;

	//a_n = n + 2^n
	suma = 0;
	for (int i = 1; i <= n; i++){
		int a = i + pow(2, i);
		suma += a;
	}
	
	cout << suma << endl;

	return 0;
}
