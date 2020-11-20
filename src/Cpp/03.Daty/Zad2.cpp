#include <iostream>

using namespace std;

int main() {

	//Czy osoba jest pelnoletnia?
	
	cout << "Podaj trzy liczby reprezentujace dzien, miesiac i rok urodzenia osoby:" << endl;
	int dzien;
	cin >> dzien;
	int miesiac;
	cin >> miesiac;
	int rok;
	cin >> rok; 

	cout << "Podaj trzy liczby reprezentujace dzisiejsza date:" << endl;
	int dzienAktualny;
	cin >> dzienAktualny;
	int miesiacAktualny;
	cin >> miesiacAktualny;
	int rokAktualny;
	cin >> rokAktualny;

	int roznicaLata = rokAktualny - rok;
	int roznicaMiesiace = miesiacAktualny - miesiac;
	int roznicaDni = dzienAktualny - dzien;

	if (roznicaLata > 18)
		cout << "osoba jest pelnoletnia" << endl;

	else if (roznicaLata == 18) {

		if (roznicaMiesiace > 0)
			cout << "osoba jest pelnoletnia" << endl;
		
		else if (roznicaMiesiace == 0) {

			if (roznicaDni >= 0)
				cout << "osoba jest pelnoletnia" << endl;
			
			else
				cout << "osoba nie jest pelnoletnia" << endl;
		}
		else
			cout << "osoba nie jest pelnoletnia"<< endl;
	}
		
	else
		cout << "osoba nie jest pelnoletnia"<< endl;

	return 0;
}

