#include <cassert>
#include <string>

//Napisz klase Czlowiek, klase pochodna Student oraz klase pochodna klasy pochodnej StudentFizyki.
//Czlowiek powinien przechowywac informacje o imieniu, nazwisku, miejscu urodzenia i zawodzie.
//Student powinien dodac pola numer albumu oraz kierunek studiow.
//Student fizyki powinien dodac pola srednia z laboratoriow oraz srednia z wykladow.

class Czlowiek {

public:
    std::string imie;
    std::string nazwisko;
    std::string miejsceUrodzenia;
    std::string zawod;

public:
    Czlowiek(std::string imie, std::string nazwisko, std::string miejsceUrodzenia, std::string zawod)
        : imie(imie)
        , nazwisko(nazwisko)
        , miejsceUrodzenia(miejsceUrodzenia)
        , zawod(zawod)
    {
    }

    std::string getImie()
    {
        return imie;
    }

    std::string getNazwisko()
    {
        return nazwisko;
    }

    std::string getMiejsceUrodzenia()
    {
        return miejsceUrodzenia;
    }

    std::string getZawod()
    {
        return zawod;
    }
};

class Student : public Czlowiek {

protected:
    int numerAlbumu;
    std::string kierunekStudiow;

public:
    Student(std::string imie, std::string nazwisko, std::string miejsceUrodzenia, int numerAlbumu, std::string kierunekStudiow)
        : Czlowiek(imie, nazwisko, miejsceUrodzenia, "Student")
        , numerAlbumu(numerAlbumu)
        , kierunekStudiow(kierunekStudiow)
    {
    }

    int getNumerAlbumu()
    {
        return numerAlbumu;
    }

    std::string getKierunekStudiow()
    {
        return kierunekStudiow;
    }
};

class StudentFizyki : public Student {

private:
    double sredniaLaboratoria;
    double sredniaWyklady;

public:
    StudentFizyki(std::string imie, std::string nazwisko, std::string miejsceUrodzenia, int numerAlbumu, double sredniaLaboratoria, double sredniaWyklady)
        : Student(imie, nazwisko, miejsceUrodzenia, numerAlbumu, "Fizyka")
        , sredniaLaboratoria(sredniaLaboratoria)
        , sredniaWyklady(sredniaWyklady)
    {
    }

    double getSredniaLaboratoria()
    {
        return sredniaLaboratoria;
    }

    double getSredniaWyklady()
    {
        return sredniaWyklady;
    }
};

void test1()
{
    const std::string imie = "Jan";
    const std::string nazwisko = "Kowalski";
    const std::string miejsceUrodzenia = "Warszawa";
    const std::string zawod = "Profesor";

    Czlowiek czlowiek(imie, nazwisko, miejsceUrodzenia, zawod);

    assert(czlowiek.getImie() == imie);
    assert(czlowiek.getNazwisko() == nazwisko);
    assert(czlowiek.getMiejsceUrodzenia() == miejsceUrodzenia);
    assert(czlowiek.getZawod() == zawod);
}

void test2()
{
    const std::string imie = "Jan";
    const std::string nazwisko = "Kowalski";
    const std::string miejsceUrodzenia = "Warszawa";
    const std::string zawod = "Student";
    const int numerAlbumu = 271932;
    const std::string kierunekStudiow = "Fizyka";

    Student student(imie, nazwisko, miejsceUrodzenia, numerAlbumu, kierunekStudiow);

    assert(student.getImie() == imie);
    assert(student.getNazwisko() == nazwisko);
    assert(student.getMiejsceUrodzenia() == miejsceUrodzenia);
    assert(student.getZawod() == zawod);
    assert(student.getNumerAlbumu() == numerAlbumu);
    assert(student.getKierunekStudiow() == kierunekStudiow);
}

void test3()
{
    const std::string imie = "Jan";
    const std::string nazwisko = "Kowalski";
    const std::string miejsceUrodzenia = "Warszawa";
    const std::string zawod = "Student";
    const int numerAlbumu = 271932;
    const std::string kierunekStudiow = "Fizyka";
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

int main()
{

    test1();
    test2();
    test3();

    return 0;
}
