#include <iostream>

int main()
{

    //Dla dwoch pobranych liczb, sprawdz czy pobrane liczby sa identyczne.

    std::cout << "podaj dwie liczby:" << std::endl;
    int a;
    int b;

    std::cin >> a;
    std::cin >> b;

    if (a == b)
        std::cout << "liczby sa jednakowe" << std::endl;
    else
        std::cout << "liczby sa rozne" << std::endl;
    return 0;
}
