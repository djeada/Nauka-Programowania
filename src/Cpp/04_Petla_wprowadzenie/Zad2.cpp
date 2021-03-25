#include <iostream>

int main()
{

    //Dla pobranej liczby, powinny zostac wyswietlone
    //wszystkie liczby naturalne mniejsze od podanej liczby.

    std::cout << "Podaj liczbe" << std::endl;
    int a;
    std::cin >> a;

    for (int i = 1; i < a; i++)
        std::cout << i << " ";

    std::cout << std::endl;

    return 0;
}
