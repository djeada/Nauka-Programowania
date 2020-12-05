#include <iostream>

using namespace std;

int main() {

	//Dla pobranych czterech liczb, znajdz najwieksza liczbe. 
	
	cout << "podaj cztery liczby:" << endl;
	int a;
	cin >> a;
	int b;
	cin >> b;
	int c;
	cin >> c; 
	int d;
	cin >> d; 

	int maksAB = a > b ? a : b;
	int maksCD = c > d ? c : d;
	int maks = maksAB > maksCD ? maksAB : maksCD;

	cout << maks << endl;
	
	return 0;
}

