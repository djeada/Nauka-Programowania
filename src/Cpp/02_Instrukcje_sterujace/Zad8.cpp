#include <iostream>

int main()
{

    //Pobierz od uzytkownika trzy dlugosci bokow i sprawdz,
    //czy mozna z nich zbudowac trojkat.

    std::cout << "podaj trzy liczby:" << std::endl;

    int a;
    int b;
    int c;

    std::cin >> a;
    std::cin >> b;
    std::cin >> c;

    if (a + b > c && b + c > a && a + c > b)
        std::cout << "z podanych bokow mozna zbudowac trojkat" << std::endl;

    else
        std::cout << "z podanych bokow nie mozna zbudowac trojkata" << std::endl;

    return 0;
}
