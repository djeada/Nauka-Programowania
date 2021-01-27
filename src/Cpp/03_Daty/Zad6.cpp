#include <iostream>

using namespace std;

int main() {

	//Dla pobranych trzech liczb, sprawdz czy reprezentuja one poprawna date. 
	//Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.
	
	cout << "Podaj dzien, miesiac i rok: " << endl;
	int dzien;
	cin >> dzien;
	int miesiac;
	cin >> miesiac;
	int rok;
	cin >> rok;	

	if (rok >= 1 ) {
		if (miesiac == 1 || miesiac == 3 || miesiac == 5 || miesiac == 7 || miesiac == 8 || miesiac == 10 || miesiac == 12) {
			if (dzien >= 1 && dzien <= 31)
				cout << "Podana data jest poprawna" << endl;
			else  
				cout << "Podano niepoprawna date" << endl;
		}
			
		else if (miesiac == 4 || miesiac == 6 || miesiac == 9 || miesiac == 11) {
			if (dzien >= 1 && dzien <= 30)
				cout << "Podana data jest poprawna" << endl;
			else 
				cout << "Podano niepoprawna date" << endl;
		}

		else if (miesiac == 2) {
			if (rok % 4 == 0 ) {
        				if (rok % 100 == 0 ) {
            				if (rok % 400 == 0  && dzien >= 1 && dzien <= 29)
						cout << "Podana data jest poprawna" << endl;
					else if (dzien >= 1 && dzien <= 28 )
						cout << "Podana data jest poprawna" << endl;
					else	
						cout << "Podano niepoprawna date" << endl;
				}
         				else if (dzien >= 1 && dzien <= 29 )
					cout << "Podana data jest poprawna" << endl;
				else
					cout << "Podano niepoprawna date" << endl;
			}
     			else if (dzien >= 1 && dzien <= 28 )
				cout << "Podana data jest poprawna" << endl;
		}
	
		else  
			cout << "Podano niepoprawna date" << endl;
  	}
	else  
		cout << "Podano niepoprawna date" << endl;

	return 0;
}

