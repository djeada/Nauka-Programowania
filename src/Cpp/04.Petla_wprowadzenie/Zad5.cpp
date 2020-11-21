#include <iostream>
using namespace std;

int main() {

	//Dla pobranych dwoch liczb, powinny zostac wyswietlone:
	
	cout << "Podaj dwie liczby: " << endl;
	int a, b;
	cin >> a >> b;

	if (b < a) {
		int pom=a;
		a = b;
		b = pom;
	}

	//wszystkie liczby naturalne większe od mniejszej pobranej 
	//liczby i jednoczesnie mniejsze od wiekszej pobranej liczby.  
	for (int i = a + 1; i < b; i++)
		cout << i << " ";

	cout << endl;

	//wszystkie liczby naturalne podzielne przez 3 
	//wieksze od mniejszej pobranej liczby i jednoczesnie 
	//mniejsze od wiekszej pobranej liczby.
	for (int i = a + 1; i < b; i++) {
		if (i % 3 == 0)
			cout << i << " ";
	}

	return 0;
}
