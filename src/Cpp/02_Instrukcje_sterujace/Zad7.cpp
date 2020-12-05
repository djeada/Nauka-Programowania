#include <iostream>

using namespace std;

int main() {

	
	//Prawo wylacznego srodka
	cout <<  "Prawo wylacznego srodka" << endl;
	bool p = false;
	cout <<  "dla p majacego wartosc logiczna " << p << " wyrazenie p v ~p ma wartosc logiczna " << boolalpha << (p || !p) << endl;
	p = true;
	cout <<  "dla p majacego wartosc logiczna " << p << " wyrazenie p v ~p ma wartosc logiczna " << boolalpha << (p || !p) << endl;

	//Zasada niesprzecznosci
	cout <<  "\nZasada niesprzecznosci" << endl;
	p = false;
	cout <<  "dla p majacego wartosc logiczna " << p << " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna " << boolalpha << !(p && !p) << endl;
	p = true;
	cout <<  "dla p majacego wartosc logiczna " << p << " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna " << boolalpha << !(p && !p) << endl;

	//Przemiennosc koniunkcji
	cout <<  "\nPrzemiennosc koniunkcji" << endl;
	p = false;
	bool q = false;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna " << boolalpha << ((p && q) == (q && p)) << endl;
	p = true;
	q = false;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna " << boolalpha << ((p && q) == (q && p)) << endl;
	p = false;
	q = true;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna " << boolalpha << ((p && q) == (q && p)) << endl;
	p = true;
	q = true;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna " << boolalpha << ((p && q) == (q && p)) << endl;

	//Przemiennosc alternatywy
	cout <<  "\nPrzemiennosc alternatywy" << endl;
	p = false;
	q = false;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie (p v q) < = > (q v p) ma wartosc logiczna " << boolalpha << ((p || q) == (q || p)) << endl;
	p = true;
	q = false;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie (p v q) < = > (q v p) ma wartosc logiczna " << boolalpha << ((p || q) == (q || p)) << endl;
	p = false;
	q = true;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie (p v q) < = > (q v p) ma wartosc logiczna " << boolalpha << ((p || q) == (q || p)) << endl;
	p = true;
	q = true;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie (p v q) < = > (q v p) ma wartosc logiczna " << boolalpha << ((p || q) == (q || p)) << endl;

	//Pierwsze prawo de Morgana
	cout <<  "\nPierwsze prawo de Morgana" << endl;
	p = false;
	q = false;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna " << boolalpha << (!(p && q) == (!q || !p)) << endl;
	p = true;
	q = false;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		"wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna " << boolalpha << (!(p && q) == (!q || !p)) << endl;
	p = false;
	q = true;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna " << boolalpha << (!(p && q) == (!q || !p)) << endl;
	p = true;
	q = true;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna " << boolalpha << (!(p && q) == (!q || !p)) << endl;

	//Drugie prawo de Morgana
	cout <<  "\nDrugie prawo de Morgana" << endl;
	p = false;
	q = false;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna " << boolalpha << (!(p || q) == (!q && !p)) << endl;
	p = true;
	q = false;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna " << boolalpha << (!(p || q) == (!q && !p)) << endl;
	p = false;
	q = true;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna " << boolalpha << (!(p || q) == (!q && !p)) << endl;
	p = true;
	q = true;
	cout <<  "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << 
		" wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna " << boolalpha << (!(p || q) == (!q && !p)) << endl;
	
	return 0;
}

