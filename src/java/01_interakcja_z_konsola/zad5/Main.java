/*
Tytul: Obliczanie wartosci funkcji w danym punkcie.
Tresc zadania: Napisz program, ktory bedzie obliczac wartosc funkcji w danym punkcie zgodnie z nastepujacymi instrukcjami:
a) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = 3x + 10$ w tym punkcie.
b) Pobierz wspolczynniki $a$, $b$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax + b$ w tym punkcie.
c) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = x^3 + 22 - 20$ w tym punkcie.
d) Pobierz wspolczynniki $a$, $b$, $c$, $d$, $m$, $n$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax^m + bx^n + c - a$ w tym punkcie.
e) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = sin^3(x) \cdot cos^2(x) + e^(x^2) + log(x^3 + 2x^2 - x - 3)$ w tym punkcie.
Dane wejsciowe:
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
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Wyznacz wartosc funkcji y = 3x + 10 w zadanym punkcie.

    System.out.print("podaj x\n");
    int x;
    Scanner s = new Scanner(System.in);

    x = Integer.parseInt(s.nextLine());

    System.out.print("3*x+10\n");
    System.out.print(3 * x + 10);
    System.out.print("\n");

    // Pobierz wspolczynniki a, b oraz punkt x i wyznacz wartosc funkcji y = ax + b w zadanym
    // punkcie.

    System.out.print("podaj a\n");
    int a;
    a = Integer.parseInt(s.nextLine());

    System.out.print("podaj b\n");
    int b;
    b = Integer.parseInt(s.nextLine());

    System.out.print("podaj x\n");
    x = Integer.parseInt(s.nextLine());

    System.out.print("a*x+b\n");
    System.out.print(a * x + b);
    System.out.print("\n");

    // Wyznacz wartosc funkcji y = x^3 + 2x^2 - 20 w zadanym punkcie.

    System.out.print("podaj x\n");
    x = Integer.parseInt(s.nextLine());

    System.out.print("y = x**3 + 2x**2 - 20\n");
    System.out.print(Math.pow(x, 3) + 2 * Math.pow(x, 2) - 20);
    System.out.print("\n");

    // Pobierz wspolczynniki a, b, c, d, m, n oraz punkt x i wyznacz wartosc funkcji y = a*x^m +
    // b*x^n + c - a w zadanym punkcie.

    System.out.print("podaj a\n");
    a = Integer.parseInt(s.nextLine());

    System.out.print("podaj b\n");
    b = Integer.parseInt(s.nextLine());

    System.out.print("podaj c\n");
    int c;
    c = Integer.parseInt(s.nextLine());

    System.out.print("podaj d\n");
    int d;
    d = Integer.parseInt(s.nextLine());

    System.out.print("podaj m\n");
    int m;
    m = Integer.parseInt(s.nextLine());

    System.out.print("podaj n\n");
    int n;
    n = Integer.parseInt(s.nextLine());

    System.out.print("podaj x\n");
    x = Integer.parseInt(s.nextLine());

    System.out.print("a*x**m + b*x**n + c - a\n");
    System.out.print(a * Math.pow(x, m) + b * Math.pow(x, n) + c - a);
    System.out.print("\n");

    // Wyznacz wartosc funkcji y = sin3x*cos2x + e^x^2 + log(x^3+2x^2-x-3) w zadanym punkcie.

    System.out.print("podaj x\n");

    x = Integer.parseInt(s.nextLine());

    System.out.print("sin(3*x)*cos(2*X) + e**x**2 + log(x**3 + 2*x**2 - x - 3)\n");
    System.out.print(
        Math.sin(3 * x) * Math.cos(2 * x)
            + Math.exp(Math.pow(x, 2))
            + Math.log(Math.pow(x, 3) + 2 * Math.pow(x, 2) - x - 3));
    System.out.print("\n");
  }
}

