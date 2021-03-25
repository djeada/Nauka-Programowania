#include <iostream>

//Wywolaj metode klasy bazowej w metodzie
//klasy potomnej nadipsujacej ta metode.

class Rodzic {
public:
    void info()
    {
        std::cout << "Jestem rodzicem" << std::endl;
    }
};

class DzieckoA : public Rodzic {
public:
    void info()
    {
        std::cout << "Jestem dzieckiem A" << std::endl;
    }
};

class DzieckoB : public Rodzic {
public:
    void info()
    {
        std::cout << "Jestem dzieckiem B" << std::endl;
        Rodzic::info();
    }
};

int main()
{

    Rodzic rodzic;
    rodzic.info();

    DzieckoA dzieckoA;
    dzieckoA.info();

    DzieckoB dzieckoB;
    dzieckoB.info();

    return 0;
}
