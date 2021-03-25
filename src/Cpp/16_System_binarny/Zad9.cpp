#include <cassert>
#include <string>

// Przy uzyciu operatorow bitowych:
//a) Zamien wielkie litery na male.
std::string wielkieNaMale(std::string slowo)
{
    std::string wynik = "";

    for (const int& litera : slowo)
        wynik += (char)(litera | (int)' ');

    return wynik;
}

//b) Zamien male litery na wielkie.
std::string maleNaWielkie(std::string slowo)
{
    std::string wynik = "";

    for (const int& litera : slowo)
        wynik += (char)(litera & (int)'_');

    return wynik;
}

//c) Zamien male litery na wielkie i wielkie na male.
std::string odwrocWielkoscLiter(std::string slowo)
{

    std::string wynik = "";

    for (const int& litera : slowo) {

        if (litera >= 'a' and litera <= 'z')
            wynik += (char)(litera ^ (int)' ');

        else if (litera >= 'A' and litera <= 'Z')
            wynik += (char)(litera ^ (int)' ');

        else
            wynik += (char)litera;
    }

    return wynik;
}

void test1()
{
    std::string slowo = "KURCZAKU";
    std::string wynik = "kurczaku";

    assert(wielkieNaMale(slowo) == wynik);
}

void test2()
{
    std::string slowo = "piesek";
    std::string wynik = "PIESEK";

    assert(maleNaWielkie(slowo) == wynik);
}

void test3()
{
    std::string slowo = "wszedl Kotek na PloteK i mrUga";
    std::string wynik = "WSZEDL kOTEK NA pLOTEk I MRuGA";

    assert(odwrocWielkoscLiter(slowo) == wynik);
}

int main()
{

    test1();
    test2();
    test3();

    return 0;
}
