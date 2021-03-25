#include <cmath>
#include <iomanip>
#include <iostream>

int main()
{

    //Dla pobranej liczby n, wyswietl sume n
    //pierwszych wyrazow ciagu danego wzorem:
    std::cout << "Podaj liczbe: " << std::endl;
    int n;
    std::cin >> n;

    std::cout << std::fixed << std::setprecision(2);

    //a_n = n/(n+1)
    float suma = 0;
    for (float i = 1; i <= n; i++) {
        float a = i / (i + 1);
        suma += a;
    }
    std::cout << suma << std::endl;

    //a_n = (n^2+5)/n
    suma = 0;
    for (float i = 1; i <= n; i++) {
        float a = (pow(i, 2) + 5) / i;
        suma += a;
    }
    std::cout << suma << std::endl;

    //a_n = n + 2^n
    suma = 0;
    for (int i = 1; i <= n; i++) {
        int a = i + pow(2, i);
        suma += a;
    }

    std::cout << suma << std::endl;

    return 0;
}
