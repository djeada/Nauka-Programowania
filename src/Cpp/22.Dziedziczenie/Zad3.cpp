/*
Stworz klasy Pies oraz Kot dziedziczace po klasie Zwierz. 
Kazda z klas powinna miec wlasna implementacje metody odglos(), wypisujacej dowolny tekst na konsole.
Przy iteracji po liscie skladajacej sie z obiektow wszystkich trzech klas i wywolywaniu na kazdym z osobna metody odlgos() na konsoli powinnien pojawic sie tekst wlasciwy dla danego zwierzaka.
*/
#include <iostream>
#include <cassert>

using namespace std;

class Zwierz {
	public:
		virtual void odglos() {
			cout << "Jestem zwierzem" << endl;
		}
};

class Pies : public Zwierz {
	public:
		void odglos() override {
			cout << "Hau" << endl;
		}
};

class Kot : public Zwierz {
	public:
		void odglos() override {
			cout << "Miau" << endl;
		}
};

int main() {

	Zwierz* zwierzaki[] = {new Zwierz(), new Pies(), new Kot()};
	
	for (auto zwierz : zwierzaki)
		zwierz->odglos();

    return 0;
}

//g++ -std=c++14 Zad3.cpp -o exe
