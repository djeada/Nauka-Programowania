#include <iostream>

int main()
{

    //Dla dwoch pobranych liczb, wypisz najpierw wieksza potem mniejsza.

    std::cout << "podaj dwie liczby:" << std::endl;

    int a;
    int b;

    std::cin >> a;
    std::cin >> b;

    if (a > b) {
        std::cout << a << std::endl;
        std::cout << b << std::endl;
        std::cout << "pierwsza liczba jest wieksza od drugiej" << std::endl;

    }

    else {
        std::cout << b << std::endl;
        std::cout << a << std::endl;
        std::cout << "pierwsza liczba nie jest wieksza od drugiej" << std::endl;
    }

    return 0;
}
