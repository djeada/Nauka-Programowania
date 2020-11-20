#include <iostream>

using namespace std;

int main() {

	//Dla pobranej liczby, wyswietl liczbe dni miesiaca odpowiadajacemu danej liczbie.

	cout << "Podaj numer miesiaca:" << endl;
	int numer;
	cin >> numer;
	

	switch (numer) {
		case 1:
			cout << "Styczen ma 31 dni" << endl;
			break;		

		case 2:
			cout << "Luty ma 28 lub 29 dni" << endl;
 			break;		        

		case 3:
			cout << "Marzec ma 31 dni" << endl;
    			break;
	
		case 4:
			cout << "Kwiecien ma 30 dni" << endl;
	     		break;

		case 5:
			cout << "Maj ma 31 dni" << endl;
        			break;	
	
		case 6:
			cout << "Czerwiec ma 30 dni" << endl;
    			break;		

		case 7:
			cout << "Lipiec ma 31 dni" << endl;
			break;

		case 8:
			cout << "Sierpien ma 31 dni" << endl;
			break;

		case 9:
			cout << "Wrzesien ma 30 dni" << endl;
			break;

		case 10:
			cout << "Pazdziernik ma 31 dni" << endl;
			break;

		case 11:
			cout << "Listopad ma 30 dni" << endl;
			break;

		case 12:
			cout << "Grudzien ma 31 dni" << endl;
			break;

		default: 
			cout << "Podano niepoprawny numer miesiaca" << endl;
	
	}
    

	return 0;
}

