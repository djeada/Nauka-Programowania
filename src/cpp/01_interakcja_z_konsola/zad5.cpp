/*
Tytul: Obliczanie wartosci funkcji w danym punkcie.
Tresc zadania: Napisz program, ktory bedzie obliczac wartosc funkcji w danym
punkcie zgodnie z nastepujacymi instrukcjami: a) Otrzymujesz wspolrzedna $x$.
Wyznacz wartosc funkcji $y = 3x + 10$ w tym punkcie. b) Pobierz wspolczynniki
$a$, $b$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax + b$ w tym punkcie. c)
Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = x^3 + 22 - 20$ w tym
punkcie. d) Pobierz wspolczynniki $a$, $b$, $c$, $d$, $m$, $n$ oraz punkt $x$.
Wyznacz wartosc funkcji $y = ax^m + bx^n + c - a$ w tym punkcie. e) Otrzymujesz
wspolrzedna $x$. Wyznacz wartosc funkcji $y = sin^3(x) \cdot cos^2(x) + e^(x^2)
+ log(x^3 + 2x^2 - x - 3)$ w tym punkcie. Dane wejsciowe:
* Liczba naturalna dla punktow 1, 3 i 5.
* Trzy liczby naturalne dla punktu 2.
* Szesc liczb naturalnych dla punktu 4.
Dane wyjsciowe:
* Liczba naturalna dla punktow 1, 2, 3 i 4.
* Liczba zmiennoprzecinkowa dla punktu 5.
Przyklad:
a) Jesli otrzymasz wspolrzedna $x = 3$, program powinien wypisac liczbe 19.
b) Jesli pobierzesz liczby 1, 2 i 3, program powinien wypisac liczbe 5.
c) Jesli otrzymasz wspolrzedna $x = 5$, program powinien wypisac liczbe 155.
d) Jesli pobierzesz liczby 1, 1, 1, 1, 1 i 1, program powinien wypisac liczbe 2.
e) Jesli otrzymasz wspolrzedna $x = 2$, program powinien wypisac liczbe 57.179.

*/
#include <cmath>
#include <iostream>

int main() {

  std::cout << "podaj x" << std::endl;
  int x;
  std::cin >> x;

  std::cout << "3*x+10" << std::endl;
  std::cout << 3 * x + 10 << std::endl;

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

  std::cout << "podaj x" << std::endl;
  std::cin >> x;

  std::cout << "y = x**3 + 2x**2 - 20" << std::endl;
  std::cout << pow(x, 3) + 2 * pow(x, 2) - 20 << std::endl;

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

  std::cout << "podaj x" << std::endl;

  std::cin >> x;

  std::cout << "sin(3*x)*cos(2*X) + e**x**2 + log(x**3 + 2*x**2 - x - 3)"
            << std::endl;
  std::cout << sin(3 * x) * cos(2 * x) + exp(pow(x, 2)) +
                   log(pow(x, 3) + 2 * pow(x, 2) - x - 3)
            << std::endl;

  return 0;
}

