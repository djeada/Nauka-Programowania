/*
Napisz klase Ptak, dziedziczaca po klasach Zwierz oraz ObiektLatajacy.
Zwierz powinien miec dostepne publiczne metody: "jedz()", "spij()", "wydajDzwiek()". ObiektLatajacy powinien miec dostepne publiczne metody: "lec()", "wyladuj()".
*/

#include <iostream>

using namespace std;

class Zwierz {
    
    private:
        string nazwa;
        string pokarm;
        string dzwiek;

    public:
        Zwierz(string nazwa, string pokarm, string dzwiek) :
            nazwa(nazwa),            
            pokarm(pokarm),
            dzwiek(dzwiek) {

            }

		void jedz() {
			cout << nazwa << " spozywa " << pokarm << "." << endl;
		}

		void spij() {
			cout << nazwa << " idzie spac." << endl;
		}

		void wydajDzwiek() {
			cout << dzwiek  << endl;
		}
};

class ObiektLatajacy {

        private:
            string nazwa;

        public:
            ObiektLatajacy(string nazwa) :
                nazwa(nazwa)
                {

                }

		void lec() {
			cout << nazwa << " wznosi sie w powietrze." << endl;
		}

		void laduj() {
			cout << nazwa << " laduje." << endl;
		}
};
 
class Ptak : public Zwierz, public ObiektLatajacy {

	public:
		 Ptak(string nazwa) :
			Zwierz(nazwa, "robaki", "Aww!Aww!"),
            ObiektLatajacy(nazwa)
            {

			}
};
    
int main() {

    Ptak koliber("Koliberek");
	koliber.jedz();
	koliber.lec();
	koliber.laduj();
	koliber.wydajDzwiek();
	koliber.spij();
	
    return 0;
}
