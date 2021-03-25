#include <cassert>
#include <iostream>
#include <vector>

//Stworz klasy Pies oraz Kot dziedziczace po klasie Zwierz.
//Kazda z klas powinna miec wlasna implementacje metody odglos(),
//wypisujacej dowolny tekst na konsole. Przy iteracji po liscie
//skladajacej sie z obiektow wszystkich trzech klas i wywolywaniu
//na kazdym z osobna metody odlgos() na konsoli powinnien pojawic
//sie tekst wlasciwy dla danego zwierzaka.

class Zwierz {
public:
    virtual void odglos() const
    {
        std::cout << "Jestem zwierzem" << std::endl;
    }
};

class Pies : public Zwierz {
public:
    void odglos() const override
    {
        std::cout << "Hau" << std::endl;
    }
};

class Kot : public Zwierz {
public:
    void odglos() const override
    {
        std::cout << "Miau" << std::endl;
    }
};

int main()
{

    std::vector<Zwierz> zwierzaki{ Zwierz(), Pies(), Kot() };

    for (const auto& zwierz : zwierzaki)
        zwierz.odglos();

    return 0;
}
