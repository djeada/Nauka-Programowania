#include <iostream>

using namespace std;

int main() {


	//Dla dwoch pobranych liczb, sprawdz czy pobrane liczby sa identyczne.
	
	cout << "podaj dwie liczby:" << endl;
	int a;
	cin >> a;
	int b;
	cin >> b; 
	if (a == b)
		cout << "liczby sa jednakowe" << endl;
	else
		cout << "liczby sa rozne" << endl;
	return 0;
}

