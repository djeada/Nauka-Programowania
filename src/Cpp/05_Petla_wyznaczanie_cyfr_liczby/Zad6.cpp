#include <iostream>
using namespace std;

int main() {

	//Dla pobranej liczby n, wyswietl sume n 
	//pierwszych wyrazow ciagu danego wzorem:
	cout << "Podaj liczbe: " << endl;
	int a;
	cin >> a;

	//a) mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10

	cout << "mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10: " << endl;
	for (int i = 0; i < a; i++) { 
		int pom = i;
		int suma = 0;

		while (pom > 0) {
			suma += (pom % 10);
			pom /= 10;  
		}

		if (suma == 10)
			cout << i << endl;
	}

	//b) dwucyfrowe mniejsze od pobranej liczby

	cout << "dwucyfrowe mniejsze od pobranej liczby: " << endl;
	for (int i = 10; i < 100 && i < a; i++) { 
		cout << i << endl;
	}

	
	//c) trzycyfrowe ktorych suma cyfr jest	rowna pobranej liczbie
	cout << "trzycyfrowe ktorych suma cyfr jest rowna pobranej liczbie" << endl;
	for (int i = 100; i < 1000; i++) { 
		int pom = i;
		int suma = 0;

		while (pom > 0) {
			suma += (pom % 10);
			pom /= 10;  
		}

		if (suma == a)
			cout <<  i << endl;
	}

	//d) trzycyfrowe podzielne przez sume cyfr pobranej liczby
	cout <<  "trzycyfrowe podzielne przez sume cyfr pobranej liczby" << endl;

	int pom = a;
	int suma = 0;

	while (pom > 0) {
		suma += (pom % 10);
		pom /= 10;   
	}

	for (int i=100; i<1000; i++) { 

		if (i % suma == 0)
			cout << i << endl;
	}

	//e) mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr
	cout << "mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr" << endl;

	for (int i = 0; i < a; i++) { 
		int pom = i;
		bool flaga = true;
		while (pom > 0) {
			int cyfra = pom % 10;
			if (cyfra % 2 == 1) {
				flaga = false;
				break;
			}
			pom /= 10;  
		}

		if (flaga)
			cout <<  i << endl;
	}

	return 0;
}
