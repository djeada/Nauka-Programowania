#include <iostream>

int main()
{

    //Dla pobranej liczby, powinny zostac zwrocone cyfry
    //liczby spelniajce nastepujacy warunek:

    std::cout << "Podaj liczbe: " << std::endl;
    int a;
    std::cin >> a;

    //a) Liczby parzyste;

    int pom = a;
    std::cout << "Cyfry liczby badace liczbami parzystymi: " << std::endl;

    while (pom > 0) {
        int cyfra = pom % 10;

        if (cyfra % 2 == 0)
            std::cout << cyfra << std::endl;

        pom /= 10;
    }

    //b) Mniejsze niz 5;

    pom = a;
    std::cout << "Cyfry liczby mniejsze niz 5: " << std::endl;

    while (pom > 0) {
        int cyfra = pom % 10;

        if (cyfra < 5)
            std::cout << cyfra << std::endl;

        pom /= 10;
    }

    //c) Rozne od 0;

    pom = a;
    std::cout << "Cyfry liczby rozne od 0: " << std::endl;

    while (pom > 0) {
        int cyfra = pom % 10;

        if (cyfra != 0)
            std::cout << cyfra << std::endl;

        pom /= 10;
    }

    return 0;
}
