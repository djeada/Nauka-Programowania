#include <iostream>

int main()
{

    //Pobierz podstawe i wysokosc trojkata i wypisz pole.

    std::cout << "podaj podstawe i wysokosc trojkata:" << std::endl;

    float a;
    std::cin >> a;
    float h;
    std::cin >> h;

    std::cout << "pole trojkata o podstawie " << a << " i wysokosci "
              << h << " jest rowne " << a * h / 2 << std::endl;

    //Pobierz dlogosci bokow prostokata i wypisz pole.

    std::cout << "podaj dlugosci bokow prostokata:" << std::endl;

    std::cin >> a;
    float b;
    std::cin >> b;

    std::cout << "pole prostokata o bokach " << a << " i " << b
              << " jest rowne " << a * b << std::endl;

    return 0;
}
