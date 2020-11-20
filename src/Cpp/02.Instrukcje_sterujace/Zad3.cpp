#include <iostream>

using namespace std;

int main() {

	//Dla pobranej liczby, sprawdz czy liczba jest ujemna, dodatnia, czy jest zerem.
	
	cout << "podaj liczbe:" << endl;
	int a;
	cin >> a;

	if (a < 0)
		cout << "libczba jest ujemna" << endl;
	else if (a > 0)
		cout << "liczba jest dodatnia" << endl;
	else
		cout << "liczba jest zerem" << endl;

	return 0;
}

