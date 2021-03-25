#include <iostream>

int main()
{

    //Dla pobranych dwoch liczb, powinny zostac wyswietlone:

    std::cout << "Podaj dwie liczby: " << std::endl;
    int a, b;
    std::cin >> a >> b;

    if (b < a) {
        int pom = a;
        a = b;
        b = pom;
    }

    //wszystkie liczby naturalne większe od mniejszej pobranej
    //liczby i jednoczesnie mniejsze od wiekszej pobranej liczby.
    for (int i = a + 1; i < b; i++)
        std::cout << i << " ";

    std::cout << std::endl;

    //wszystkie liczby naturalne podzielne przez 3
    //wieksze od mniejszej pobranej liczby i jednoczesnie
    //mniejsze od wiekszej pobranej liczby.
    for (int i = a + 1; i < b; i++) {
        if (i % 3 == 0)
            std::cout << i << " ";
    }

    return 0;
}
