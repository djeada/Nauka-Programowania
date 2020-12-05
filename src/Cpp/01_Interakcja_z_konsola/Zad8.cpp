#include <iostream>
#include <cmath>

using namespace std;

int main() {

	/*
	Otrzymujesz cene oraz wymiary pojedynczej plytki. Oblicz ile bedzie wynosila cena
	za podloge o podanych wymiarach. Podloga jest prostokatem, a plytka kwadratem
	*/

	cout << "podaj: cene plytki, dlugosc boku plytki i wymiary podlogi" << endl;

	int cena;
	cin >> cena;
	int bokPlytki;
	cin >> bokPlytki;
	int szerokoscPodlogi;
	cin >> szerokoscPodlogi; 
	int dlugoscPodlogi;
	cin >> dlugoscPodlogi; 

	int szerokoscKonieczna = szerokoscPodlogi + bokPlytki - szerokoscPodlogi % bokPlytki;
	int dlugoscKonieczna = dlugoscPodlogi + bokPlytki - dlugoscPodlogi % bokPlytki;
	
	int polePlytki = pow(bokPlytki,2);
	int polePodlogi = szerokoscKonieczna * dlugoscKonieczna;
	
	float calkowityKoszt = cena * (float)polePodlogi / polePlytki;

	cout <<  "Dla plytki o dlugosci boku " << bokPlytki << "i ceny " << cena << 
		" calkowity koszt wylozenia podlogi o wymiarach " << szerokoscPodlogi << 
		"x" << dlugoscPodlogi << " wynosi " << calkowityKoszt << endl;

	return 0;
}
