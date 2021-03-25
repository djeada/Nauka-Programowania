#include <cassert>
#include <cmath>
#include <numbers>
#include <stdexcept>

//Zaprojektuj klase Ksztalt oraz klasy pochodne Kolo oraz Kwadrat.

class Ksztalt {
public:
    virtual double obwod() = 0;
    virtual double pole() = 0;
};

class Kolo : public Ksztalt {
public:
    Kolo(double _promien)
    {
        if (_promien <= 0)
            throw std::invalid_argument("Wartosc musi byc dodatnia.");

        promien = _promien;
    }

    double obwod()
    {
        return 2 * std::numbers::pi * promien;
    }

    double pole()
    {
        return std::numbers::pi * pow(promien, 2);
    }

private:
    double promien;
};

class Kwadrat : public Ksztalt {
public:
    Kwadrat(double _bok)
    {
        if (_bok <= 0)
            throw std::invalid_argument("Wartosc musi byc dodatnia.");

        bok = _bok;
    }

    double obwod()
    {
        return 4 * bok;
    }

    double pole()
    {
        return pow(bok, 2);
    }

private:
    double bok;
};

void test1()
{
    Kolo kolo(3);
    assert(abs(kolo.obwod() - 18.85) < 0.01);
    assert(abs(kolo.pole() - 28.27) < 0.01);
}

void test2()
{
    Kwadrat kwadrat(3);
    assert(abs(kwadrat.obwod() - 12) < 0.01);
    assert(abs(kwadrat.pole() - 9) < 0.01);
}

int main()
{

    test1();
    test2();

    return 0;
}
