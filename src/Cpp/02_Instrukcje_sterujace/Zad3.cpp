#include <iostream>

int main()
{

    //Dla pobranej liczby, sprawdz czy liczba jest ujemna, dodatnia, czy jest zerem.

    std::cout << "podaj liczbe:" << std::endl;

    int a;
    std::cin >> a;

    if (a < 0)
        std::cout << "libczba jest ujemna" << std::endl;
    else if (a > 0)
        std::cout << "liczba jest dodatnia" << std::endl;
    else
        std::cout << "liczba jest zerem" << std::endl;

    return 0;
}
