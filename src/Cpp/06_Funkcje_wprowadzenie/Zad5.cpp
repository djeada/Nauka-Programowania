#include <cmath>
#include <iostream>

//Napisz funkcje, ktora zamieni wartosci miejscami.

void swap(int& a, int& b)
{
    int c = a;
    a = b;
    b = c;
}

int main()
{
    std::cout << "Podaj dwie liczby: " << std::endl;
    int a;
    std::cin >> a;
    int b;
    std::cin >> b;

    swap(a, b);
    std::cout << "Liczby zamienione miejscami to: " << a << " " << b << std::endl;

    return 0;
}
