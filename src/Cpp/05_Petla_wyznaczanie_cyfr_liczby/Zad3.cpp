#include <iostream>

int main()
{

    //Dla pobranej liczby, wyswietl liczbe Pi tyle razy
    //ile wynosi pobrana liczba, z dokladnoscia do tylu
    //miejsc po przecinku ile wynosi pobrana liczba.

    std::cout << "Podaj liczbe" << std::endl;
    int a;
    std::cin >> a;

    int suma = 0;

    while (a > 0) {
        suma += (a % 10);
        a = a / 10;
    }

    std::cout << "Suma cyfr podanej liczby wynosi " << suma << std::endl;

    return 0;
}
