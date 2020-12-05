#include <iostream>
using namespace std;

int main() {

	//Dla pobranej liczby, powinny zostac zwrocone cyfry 
	//liczby spelniajce nastepujacy warunek:
	
	cout << "Podaj liczbe: " << endl;
	int a;
	cin >> a;

	//a) Liczby parzyste;

	int pom = a;
	cout << "Cyfry liczby badace liczbami parzystymi: " << endl;

	while (pom > 0) {
		int cyfra = pom % 10;
		
		if (cyfra % 2 == 0)
			cout << cyfra << endl;
		
		pom /= 10;  
	}

	//b) Mniejsze niz 5;

	pom = a;
	cout << "Cyfry liczby mniejsze niz 5: " << endl;

	while (pom > 0) {
		int cyfra = pom % 10;
		
		if (cyfra < 5)
			cout << cyfra << endl;
		
		pom /= 10;  
	}

	//c) Rozne od 0;

	pom = a;
	cout << "Cyfry liczby rozne od 0: " << endl;

	while (pom > 0) {
		int cyfra = pom % 10;
		
		if (cyfra != 0)
			cout << cyfra  << endl;
		
		pom /= 10;  
	}

	return 0;
}
