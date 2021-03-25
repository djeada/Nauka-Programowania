#include <cmath>
#include <iostream>

int main()
{

    //Wyznacz wartosc funkcji y = 3x + 10 w zadanym punkcie.

    std::cout << "podaj x" << std::endl;
    int x;
    std::cin >> x;

    std::cout << "3*x+10" << std::endl;
    std::cout << 3 * x + 10 << std::endl;

    //Pobierz wspolczynniki a, b oraz punkt x i wyznacz wartosc funkcji y = ax + b w zadanym punkcie.

    std::cout << "podaj a" << std::endl;
    int a;
    std::cin >> a;

    std::cout << "podaj b" << std::endl;
    int b;
    std::cin >> b;

    std::cout << "podaj x" << std::endl;
    std::cin >> x;

    std::cout << "a*x+b" << std::endl;
    std::cout << a * x + b << std::endl;

    //Wyznacz wartosc funkcji y = x^3 + 2x^2 - 20 w zadanym punkcie.

    std::cout << "podaj x" << std::endl;
    std::cin >> x;

    std::cout << "y = x**3 + 2x**2 - 20" << std::endl;
    std::cout << pow(x, 3) + 2 * pow(x, 2) - 20 << std::endl;

    //Pobierz wspolczynniki a, b, c, d, m, n oraz punkt x i wyznacz wartosc funkcji y = a*x^m + b*x^n + c - a w zadanym punkcie.

    std::cout << "podaj a" << std::endl;
    std::cin >> a;

    std::cout << "podaj b" << std::endl;
    std::cin >> b;

    std::cout << "podaj c" << std::endl;
    int c;
    std::cin >> c;

    std::cout << "podaj d" << std::endl;
    int d;
    std::cin >> d;

    std::cout << "podaj m" << std::endl;
    int m;
    std::cin >> m;

    std::cout << "podaj n" << std::endl;
    int n;
    std::cin >> n;

    std::cout << "podaj x" << std::endl;
    std::cin >> x;

    std::cout << "a*x**m + b*x**n + c - a" << std::endl;
    std::cout << a * pow(x, m) + b * pow(x, n) + c - a << std::endl;

    //Wyznacz wartosc funkcji y = sin3x*cos2x + e^x^2 + log(x^3+2x^2-x-3) w zadanym punkcie.

    std::cout << "podaj x" << std::endl;

    std::cin >> x;

    std::cout << "sin(3*x)*cos(2*X) + e**x**2 + log(x**3 + 2*x**2 - x - 3)" << std::endl;
    std::cout << sin(3 * x) * cos(2 * x) + exp(pow(x, 2)) + log(pow(x, 3) + 2 * pow(x, 2) - x - 3) << std::endl;

    return 0;
}
