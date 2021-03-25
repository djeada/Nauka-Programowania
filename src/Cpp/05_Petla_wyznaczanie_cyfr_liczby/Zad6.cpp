#include <iostream>

int main()
{

    //Dla pobranej liczby n, wyswietl sume n
    //pierwszych wyrazow ciagu danego wzorem:
    std::cout << "Podaj liczbe: " << std::endl;
    int a;
    std::cin >> a;

    //a) mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10

    std::cout << "mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10: " << std::endl;
    for (int i = 0; i < a; i++) {
        int pom = i;
        int suma = 0;

        while (pom > 0) {
            suma += (pom % 10);
            pom /= 10;
        }

        if (suma == 10)
            std::cout << i << std::endl;
    }

    //b) dwucyfrowe mniejsze od pobranej liczby

    std::cout << "dwucyfrowe mniejsze od pobranej liczby: " << std::endl;
    for (int i = 10; i < 100 && i < a; i++) {
        std::cout << i << std::endl;
    }

    //c) trzycyfrowe ktorych suma cyfr jest	rowna pobranej liczbie
    std::cout << "trzycyfrowe ktorych suma cyfr jest rowna pobranej liczbie" << std::endl;
    for (int i = 100; i < 1000; i++) {
        int pom = i;
        int suma = 0;

        while (pom > 0) {
            suma += (pom % 10);
            pom /= 10;
        }

        if (suma == a)
            std::cout << i << std::endl;
    }

    //d) trzycyfrowe podzielne przez sume cyfr pobranej liczby
    std::cout << "trzycyfrowe podzielne przez sume cyfr pobranej liczby" << std::endl;

    int pom = a;
    int suma = 0;

    while (pom > 0) {
        suma += (pom % 10);
        pom /= 10;
    }

    for (int i = 100; i < 1000; i++) {

        if (i % suma == 0)
            std::cout << i << std::endl;
    }

    //e) mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr
    std::cout << "mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr" << std::endl;

    for (int i = 0; i < a; i++) {
        int pom = i;
        bool flaga = true;
        while (pom > 0) {
            int cyfra = pom % 10;
            if (cyfra % 2 == 1) {
                flaga = false;
                break;
            }
            pom /= 10;
        }

        if (flaga)
            std::cout << i << std::endl;
    }

    return 0;
}
