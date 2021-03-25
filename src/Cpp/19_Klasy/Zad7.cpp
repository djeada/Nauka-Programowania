#include <cassert>
#include <iostream>
#include <vector>

class Klasa {
    inline static unsigned int licznik = 0;

public:
    Klasa()
    {
        licznik++;
    }

    ~Klasa()
    {
        licznik--;
    }

    unsigned int static liczbaInstancji()
    {
        return licznik;
    }

    void static wyswietl()
    {
        std::cout << "Aktualna liczba instancji: " << licznik << std::endl;
    }
};

void test1()
{
    unsigned int n = 5;
    std::vector<Klasa> lista(n);
    assert(Klasa::liczbaInstancji() == n);
}

void test2()
{
    assert(Klasa::liczbaInstancji() == 0);
}

int main()
{

    test1();
    test2();

    return 0;
}
