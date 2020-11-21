#include <iostream>
using namespace std;

int main() {

	//Dla pobranej liczby, sprawdz czy jest palindromem.
	
	cout << "Podaj liczbe" << endl;
	int a;
	cin >> a;
	
	int odwrocona = 0;
	int pom = a;

	while (pom > 0) {
		int cyfra = pom % 10;
		odwrocona= (odwrocona*10 + cyfra);
		pom /= 10; 
	}

	if (odwrocona == a)
		cout << "podana liczba jest palindromem" << endl;
	else
		cout << "podana liczba nie jest palindromem" << endl;

	return 0;
}
