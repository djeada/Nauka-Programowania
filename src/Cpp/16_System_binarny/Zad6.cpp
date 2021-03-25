#include <algorithm>
#include <cassert>
#include <cmath>
#include <string>

//Konwersja miedzy dowolnymi systemami liczbowymi.
int naDec(std::string liczba, int podstawa)
{
    int wartoscDec = 0;

    for (int i = liczba.size() - 1; i >= 0; i--) {

        if (liczba[i] >= 'A' && liczba[i] < 'Z')
            wartoscDec += (liczba[i] - 'A' + 10) * pow(podstawa, (liczba.size() - 1 - i));

        else
            wartoscDec += (liczba[i] - '0') * pow(podstawa, (liczba.size() - 1 - i));
    }

    return wartoscDec;
}

void zmianaPodstawy(std::string& liczba, int podstawa, int nowaPodstawa)
{

    if (podstawa > (10 + 'Z' - 'A'))
        return;

    int wartoscDec = naDec(liczba, podstawa);
    liczba = "";
    podstawa = nowaPodstawa;

    while (wartoscDec > 0) {
        int reszta = wartoscDec % podstawa;
        wartoscDec /= podstawa;

        char nowyZnak = '0' + reszta;

        if (nowyZnak > '9')
            nowyZnak = 'A' + (nowyZnak - '9') - 1;

        liczba += nowyZnak;
    }

    reverse(liczba.begin(), liczba.end());
}

void test1()
{
    std::string liczba = "4301";
    std::string wynik = "1003031";
    zmianaPodstawy(liczba, 10, 4);

    assert(liczba == wynik);
}

int main()
{

    test1();
    return 0;
}
