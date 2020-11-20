#include <iostream>

using namespace std;

int main() {

	//Czy rok jes przestepny?

	cout << "Podaj rok:" << endl;
	int rok;	
	cin >> rok;

	if (rok % 4 == 0) {
		
		if (rok % 100 == 0) {
	 		if (rok % 400 == 0)
					cout << "rok jest przestepny" << endl;
		  	else
					cout << "rok nie jest przestepny" << endl;
		}
	 
		else
			cout << "rok jest przestepny" << endl;
	}

	else
		cout << "rok nie jest przestepny" << endl;

	return 0;
}

