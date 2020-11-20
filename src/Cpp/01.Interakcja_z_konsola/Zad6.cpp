#include <iostream>

using namespace std;

int main() {

	//Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.

	cout << "podaj wielkosc w kilogramach:" << endl;

	int kilogramy;
	cin >> kilogramy;
	int gramy = kilogramy * 1000;

	cout << kilogramy << " kg to " << gramy << " g." << endl; 

	//Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.

	cout << "podaj wielkosc w calach:" << endl;

	float cal;
	cin >> cal;
	float cm = cal / 2.54;

	cout << cal << " cal to " << cm << " cm." << endl; 
	 
	//Pobierz ilosc sekund i przelicz na godziny.

	cout << "podaj ilosc sekund:" << endl;

	float sekundy;
	cin >> sekundy;
	float godziny = sekundy / 3600;

	cout << sekundy << " sekund to " << godziny << " godzin" << endl;

	//Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada. 

	cout << "podaj liczbe w euro:" << endl;

	float euro;
	cin >> euro;
	float zloty = euro * 4.40;

	cout << euro << " euro to " << zloty << " zlotych" << endl;

	//Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada. 
	
	cout << "podaj miare kata w stopniach:" << endl; 

	float katStopnie;
	cin >> katStopnie;
	float katRad = katStopnie * 0.0174532;

	cout << katStopnie << " stopni to " << katRad << " radianow." << endl;

	//Pobierz temperature w stopniach Farenheita i wypisz 
	//ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada. 

	cout << "podaj temperature w Farenheitach:" << endl; 

	float tempF;
	cin >> tempF;
	float tempC = (tempF -32) * 5 / 9;
	float tempK = tempC - 273;

	cout << tempF << " F to " << tempC << " C i " << tempK << " K" << endl;

	return 0;
}
