#include <iostream>

using namespace std;

int main() {

	//Dla pobranej liczby, wypisz dzien tygodnia odpowiadajcy tej liczbie.

	cout << "Podaj numer dnia tygodnia:" << endl;
	int dzien;
	cin >> dzien;
	

	switch (dzien) {
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
			cout << "podano niepoprawna liczbe" << endl;
	
	}
    

	return 0;
}

