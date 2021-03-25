#include <iostream>

int main()
{

    //Dla pobranych czterech liczb, znajdz najwieksza liczbe.

    std::cout << "podaj cztery liczby:" << std::endl;

    int a;
    int b;
    int c;
    int d;

    std::cin >> a;
    std::cin >> b;
    std::cin >> c;
    std::cin >> d;

    int maksAB = a > b ? a : b;
    int maksCD = c > d ? c : d;
    int maks = maksAB > maksCD ? maksAB : maksCD;

    std::cout << maks << std::endl;

    return 0;
}
