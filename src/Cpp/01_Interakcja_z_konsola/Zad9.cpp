#include <cmath>
#include <iomanip>
#include <iostream>

int main()
{

    //Otrzymujesz roczna stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc
    //udzielonego kredytu. Oblicz miesieczna rate oraz calkowity koszt kredytu.

    std::cout << "Podaj: stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc 
        udzielonego kredytu " << std::endl;

        float stopa;
    int lata;
    int kredyt;

    std::cin >> stopa;
    std::cin >> lata;
    std::cin >> kredyt;

    float r = stopa / 12 * 0.01;
    int n = lata * 12;

    float rata = kredyt * r * pow((1 + r), n) / (pow((1 + r), n) - 1);
    float calkKosz = rata * n;

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "rata mieieczna to " << rata << std::endl;
    std::cout << "calkowity koszt to " << calkKosz << std::endl;

    return 0;
}
