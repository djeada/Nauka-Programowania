/*
Napisz klase Czlowiek, klase pochodna Student oraz klase pochodna klasy pochodnej StudentFizyki.
Czlowiek powinien przechowywac informacje o imieniu, nazwisku, miejscu urodzenia i zawodzie.
Student powinien dodac pola numer albumu oraz kierunek studiow.
Student fizyki powinien dodac pola srednia z laboratoriow oraz srednia z wykladow.
*/

#include <iostream>
#include <cassert>

using namespace std;

class Czlowiek {

    public:
        string imie;
        string nazwisko;
        string miejsceUrodzenia;
        string zawod;
    
    public:
        Czlowiek(string imie, string nazwisko, string miejsceUrodzenia, string zawod) :
            imie(imie),
            nazwisko(nazwisko),
            miejsceUrodzenia(miejsceUrodzenia),
            zawod(zawod)
            {

            }

		string getImie() {
			return imie;
		}

		string getNazwisko() {
			return nazwisko;
		}        

		string getMiejsceUrodzenia() {
			return miejsceUrodzenia;
		}

		string getZawod() {
			return zawod;
		}
};

class Student : public Czlowiek {

        protected:
            int numerAlbumu;
            string kierunekStudiow;

        public:
            Student(string imie, string nazwisko, string miejsceUrodzenia, int numerAlbumu, string kierunekStudiow) :
                numerAlbumu(numerAlbumu),
                kierunekStudiow(kierunekStudiow),
                Czlowiek(imie, nazwisko, miejsceUrodzenia, "Student")
                {

                }

		int getNumerAlbumu() {
			return numerAlbumu;
		}

		string getKierunekStudiow() {
			return kierunekStudiow;
		}        
};
 
class StudentFizyki : public Student {

	private:
		double sredniaLaboratoria;
		double sredniaWyklady;

	public:
		 StudentFizyki(string imie, string nazwisko, string miejsceUrodzenia, int numerAlbumu, double sredniaLaboratoria, double sredniaWyklady) :
			sredniaLaboratoria(sredniaLaboratoria),
			sredniaWyklady(sredniaWyklady),
			Student(imie, nazwisko, miejsceUrodzenia, numerAlbumu, "Fizyka")
			{

			}
		
		double getSredniaLaboratoria() {
			return sredniaLaboratoria;
		}

		double getSredniaWyklady() {
			return sredniaWyklady;
		}
};

void Test1()
{
	const string imie = "Jan";
	const string nazwisko = "Kowalski";
	const string miejsceUrodzenia = "Warszawa";
	const string zawod = "Profesor";

    Czlowiek czlowiek(imie, nazwisko, miejsceUrodzenia, zawod);

	assert(czlowiek.getImie() == imie);
	assert(czlowiek.getNazwisko() == nazwisko);
	assert(czlowiek.getMiejsceUrodzenia() == miejsceUrodzenia);
	assert(czlowiek.getZawod() == zawod);
}

void Test2()
{
	const string imie = "Jan";
	const string nazwisko = "Kowalski";
	const string miejsceUrodzenia = "Warszawa";
	const string zawod = "Student";
	const int numerAlbumu = 271932;
	const string kierunekStudiow = "Fizyka";	

    Student student(imie, nazwisko, miejsceUrodzenia, numerAlbumu, kierunekStudiow);

	assert(student.getImie() == imie);
	assert(student.getNazwisko() == nazwisko);
	assert(student.getMiejsceUrodzenia() == miejsceUrodzenia);
	assert(student.getZawod() == zawod);
	assert(student.getNumerAlbumu() == numerAlbumu);
	assert(student.getKierunekStudiow() == kierunekStudiow);
}

void Test3()
{
	const string imie = "Jan";
	const string nazwisko = "Kowalski";
	const string miejsceUrodzenia = "Warszawa";
	const string zawod = "Student";
	const int numerAlbumu = 271932;
	const string kierunekStudiow = "Fizyka";	
	const double sredniaLaboratoria = 3.82;
	const double sredniaWyklady = 4.56;

    StudentFizyki student(imie, nazwisko, miejsceUrodzenia, numerAlbumu, sredniaLaboratoria, sredniaWyklady);

	assert(student.getImie() == imie);
	assert(student.getNazwisko() == nazwisko);
	assert(student.getMiejsceUrodzenia() == miejsceUrodzenia);
	assert(student.getZawod() == zawod);
	assert(student.getNumerAlbumu() == numerAlbumu);
	assert(student.getKierunekStudiow() == kierunekStudiow);
	assert(student.getSredniaLaboratoria() == sredniaLaboratoria);
	assert(student.getSredniaWyklady() == sredniaWyklady);
}

int main() {

    Test1();
	Test2();
	Test3();

    return 0;
}
