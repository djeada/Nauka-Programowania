#include <iostream>

int main()
{

    //Dla pobranej liczby, powinny zostac zwrocone
    //cyfry pobranej liczby poczynajac od cyfry jednosci.

    std::cout << "Podaj liczbe" << std::endl;
    int a;
    std::cin >> a;

    while (a > 0) {
        std::cout << a % 10 << std::endl;
        a = a / 10;
    }

    return 0;
}
