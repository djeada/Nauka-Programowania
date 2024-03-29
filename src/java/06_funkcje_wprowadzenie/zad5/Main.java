/*
Tytul: Maks i min
Napisz funkcje, ktora:
a) Dla otrzymanych dwoch liczb zwroci mniejsza.
b) Dla otrzymanych dwoch liczb zwroci wieksza.
c) Dla otrzymanych trzech liczb zwroci najmniejsza.
d) Dla otrzymanych trzech liczb zwroci najwieksza.
Dane wejsciowe:
a) Dwie liczby naturalne.
b) Dwie liczby naturalne.
c) Trzy liczby naturalne.
d) Trzy liczby naturalne.
Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.
Przyklad:
a) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrocic liczbe 1.
b) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrocic liczbe 3.
c) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrocic liczbe 1.
d) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrocic liczbe 3."

*/
import java.util.*;

public class Main {
  // Napisz funkcje, ktora:

  // a) dla podanych dwoch liczb, zwroci mniejsza
  public static int min2(int a, int b) {
    return a < b ? a : b;
  }

  // b) dla podanych dwoch liczb, zwroci wieksza
  public static int maks2(int a, int b) {
    return a > b ? a : b;
  }

  // c) dla podanych trzech liczb, zwroci najmniejsza
  public static int min3(int a, int b, int c) {
    int minAB = a < b ? a : b;
    return minAB < c ? minAB : c;
  }

  // d) dla podanych trzech liczb, zwroci najwieksza
  public static int maks3(int a, int b, int c) {
    int maksAB = a > b ? a : b;
    return maksAB > c ? maksAB : c;
  }

  public static void main(String[] args) {

    System.out.print("Podaj dwie liczby: \n");

    Scanner s = new Scanner(System.in);

    int a = Integer.parseInt(s.nextLine());
    int b = Integer.parseInt(s.nextLine());

    System.out.print("mniejsza liczba to: " + min2(a, b) + "\n");
    System.out.print("wieksza liczba to: " + maks2(a, b) + "\n");

    System.out.print("Podaj trzy liczby: \n");
    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());
    int c = Integer.parseInt(s.nextLine());

    System.out.print("najmniejsza liczba to: " + min3(a, b, c) + "\n");
    System.out.print("najwieksza liczba to " + maks3(a, b, c) + "\n");
  }
}

