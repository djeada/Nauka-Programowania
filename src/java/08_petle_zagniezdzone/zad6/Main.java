/*
Tytul: Litera Z.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze litere Z o wysokosci rownej tej liczbie.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 5 powinno zostac wypisane:
*****
*
*
*
*****

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanej liczby
  // wypisze litere Z, o wysokosci rownej
  // otrzymanej liczbie.

  public static void literaX(int n) {

    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        if (y == 0 || y == n - 1) {
          System.out.print("*");
        } else if (x == n - y - 1) {
          System.out.print("*");
        } else {
          System.out.print(" ");
        }
      }
      System.out.print("\n");
    }
  }

  public static void main(String[] args) {

    int a = 5;
    literaX(a);
  }
}

