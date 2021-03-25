#include <iostream>

int main()
{

    //Wypisz pobrana od uzytkownika liczbe, jesli jest wieksza od 5.

    std::cout << "podaj liczbe:" << std::endl;
    int x;
    std::cin >> x;

    if (x > 5)
        std::cout << x << std::endl;

    return 0;
}
