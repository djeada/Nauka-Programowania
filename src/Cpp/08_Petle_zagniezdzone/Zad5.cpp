#include <iostream>

//Napisz funkcje, ktora dla otrzymanej liczby
//wypisze litere X, o wysokosci rownej
//otrzymanej liczbie.

void literaX(int n)
{

    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            if (y == x || x == (n - 1 - y))
                std::cout << "*";
            else
                std::cout << " ";
        }
        std::cout << std::endl;
    }
}

int main()
{

    int a = 5;
    literaX(a);

    return 0;
}
