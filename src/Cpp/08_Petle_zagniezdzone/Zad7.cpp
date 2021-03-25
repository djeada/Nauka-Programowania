#include <iostream>

//Napisz funkcje, ktora dla otrzymanej liczby
//wyswietli N trojkatow. Trojkaty powinny byc
//ustawione w kolumnie, jeden na drugim. Wysokosc
//pierwszego trojkata to 1, a dla kazdego nastepnego
//rowna jest wysokosci poprzedniego powiekszonej o 1.

void trojkat(int a)
{

    for (int y = 0; y < a; y++) {
        for (int x = 0; x <= y; x++)
            std::cout << "*";
        std::cout << std::endl;
    }
}

void choinka(int n)
{

    for (int i = 1; i <= n; i++)
        trojkat(i);
}

int main()
{

    int a = 5;
    choinka(a);

    return 0;
}
