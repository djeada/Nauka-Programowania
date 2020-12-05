#include <iostream>
using namespace std;

int main() {

	//Dla pobranej liczby, powinny zostac wyswietlone 
	//wszystkie liczby naturalne mniejsze od podanej liczby.

	cout << "Podaj liczbe" << endl;
	int a;
	cin >> a;
	
	for (int i = 1; i < a; i++)
		cout << i << " ";

	return 0;
}
