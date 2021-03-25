#include <iostream>

//Napisz funkcje, ktora dla otrzymanej liczby n,
//poprosi uzytkownika o podanie n liczb i zwroci
//ich srednia arytmetyczna

float srednia(int n)
{

    float suma = 0.0;
    int x;

    for (int i = 0; i < n; i++) {
        std::cout << "Podaj liczbe: " << std::endl;
        std::cin >> x;
        suma += x;
    }

    return suma / n;
}

int main()
{

    std::cout << "Podaj liczbe n: " << std::endl;
    int n;
    std::cin >> n;

    float wynik = srednia(n);

    std::cout << "Srednia z podanych liczb to " << wynik << std::endl;

    return 0;
}
