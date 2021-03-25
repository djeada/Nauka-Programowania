#include <iostream>

int main()
{

    //Dla pobranej liczby, sprawdz czy jest palindromem.

    std::cout << "Podaj liczbe" << std::endl;
    int a;
    std::cin >> a;

    int odwrocona = 0;
    int pom = a;

    while (pom > 0) {
        int cyfra = pom % 10;
        odwrocona = (odwrocona * 10 + cyfra);
        pom /= 10;
    }

    if (odwrocona == a)
        std::cout << "podana liczba jest palindromem" << std::endl;
    else
        std::cout << "podana liczba nie jest palindromem" << std::endl;

    return 0;
}
