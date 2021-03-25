#include <iomanip>
#include <iostream>

int main()
{

    //Dla pobranej liczby, wyswietl liczbe Pi podniesiona
    //do potegi rownej pobranej liczbie. Wynik powinien byc
    //zaokraglony do dwoch miejsc po przecinku.

    std::cout << "Podaj liczbe: " << std::endl;
    int n;
    std::cin >> n;

    std::cout << std::fixed << std::setprecision(2);

    int wynik = 1;
    for (int i = 0; i < n; i++)
        wynik *= 3.14;

    std::cout << wynik << std::endl;

    return 0;
}
