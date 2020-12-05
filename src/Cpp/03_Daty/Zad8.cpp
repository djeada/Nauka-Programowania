#include <iostream>

using namespace std;

int main() {

	/*Niech data bedzie dana w formacie DD/MM/CCYY :
	DD - dzien
	MM - miesiac
	CC - stulecie
	YY - rok 

	A = CC/4 - 2*CC - 1 
	B = 5*YY/4
	C = 26*(MM + 1)/10

	Dzien = (A + B + C + DD) mod 7
	*/
	
  	cout << "Podaj dzien:" << endl;
	int DD;
	cin >> DD;
	
	cout << "Podaj miesiac:" << endl;
	int MM;
	cin >> MM;

	cout << "Podaj rok:" << endl;
	int rok;
	cin >> rok;

	int CC = rok/100;
	int YY = rok % 100;

	int A = (CC/4) - 2*CC - 1;
	int B = 5*YY/4;
	int C = 26*(MM+1)/10;

	int wynik = (A + B + C + DD) % 7;

	switch (wynik) {
		case 1:
			cout << "pierwszym dniem tygodnia jest poniedzialek" << endl;
			break;		

		case 2:
			cout << "drugim dniem tygodnia jest wtorek" << endl;
			break;		        

		case 3:
			cout << "trzecim dniem tygodnia jest sroda" << endl;
			break;

		case 4:
			cout << "czwartym dniem tygodnia jest czwartek" << endl;
	     		break;

		case 5:
			cout << "piatym dniem tygodnia jest piatek" << endl;
			break;	

		case 6:
			cout << "szostym dniem tygodnia jest sobota" << endl;
			break;		

		case 7:
			cout << "siodmym dniem tygodnia jest niedziela" << endl;
			break;
		
		default: 
			cout << "bledne dane" << endl;
	
	}

	return 0;
}

