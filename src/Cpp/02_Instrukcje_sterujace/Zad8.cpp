#include <iostream>

using namespace std;

int main() {

	//Pobierz od uzytkownika trzy dlugosci bokow i sprawdz, 
	//czy mozna z nich zbudowac trojkat.
	
	cout << "podaj trzy liczby:" << endl;
	int a;
	cin >> a;
	int b;
	cin >> b;
	int c;
	cin >> c; 

	if (a + b > c && b + c > a && a + c > b)
		cout << "z podanych bokow mozna zbudowac trojkat" << endl;
 
	else
		cout << "z podanych bokow nie mozna zbudowac trojkata" << endl; 

	return 0;
}

