#include <cmath>
#include <iostream>

//Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora
//dla otrzymanych dwoch liczb ustali czy:

//a) pierwsza liczba jest wieksza od drugiej
bool czyWieksza(int a, int b)
{
    return a > b;
}

//b) czy suma liczb jest mneijsza niz 10
bool czySumaMniejsza(int a, int b)
{
    int suma = a + b;
    return suma < 10;
}

//c) czy obie sa nieparzyste
bool czyObieNieparzyste(int a, int b)
{
    return a % 2 == 1 && b % 2 == 1;
}

//d) czy wieksza liczba jest mniejsza
//od pierwszej podniesionej do kwadratu
int wieksza(int a, int b)
{
    return a > b ? a : b;
}

bool czyWiekszaNizKwad(int a, int b)
{
    return wieksza(a, b) < pow(a, 2);
}

int main()
{
    std::cout << "Podaj dwie liczby: " << std::endl;
    int a;
    int b;

    std::cin >> a;
    std::cin >> b;

    std::cout << "Pierwsza liczba jest wieksza od drugiej: " << std::boolalpha << czyWieksza(a, b) << std::endl;

    std::cout << "Suma liczb jest mniejsza od 10: " << std::boolalpha << czySumaMniejsza(a, b) << std::endl;

    std::cout << "Obie liczby nieparzyste: " << std::boolalpha << czyObieNieparzyste(a, b) << std::endl;

    std::cout << "Wieksza liczba jest mniejsza od pierwszej podniesionej do kwadratu "
              << std::boolalpha << czyWiekszaNizKwad(a, b) << std::endl;

    return 0;
}
