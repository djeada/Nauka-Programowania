#include <iostream>

int main()
{
    //Dla pobranej od uzytkownika liczby,
    //zwroc liczbe cyfr pobranje liczby.

    std::cout << "Podaj liczbe" << std::endl;
    int a;
    std::cin >> a;

    int licznik = 0;

    while (a > 0) {
        a = a / 10;
        licznik++;
    }

    std::cout << "Podana liczba sklada sie z " << licznik << " cyfr." << std::endl;

    return 0;
}
