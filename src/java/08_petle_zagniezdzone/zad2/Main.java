/*
Tytul: Trojkat prostokatny rownoboczny
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze trojkat prostokatny rownoboczny o wysokosci rownej tej liczbie.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 3 powinno zostac wypisane:
*
**
***

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanej liczby
  // wypisze trojkat prostokatny rownoboczny o
  // wysokosci rownej otrzymanej liczbie.

  public static void trojkat(int a) {

    for (int y = 0; y < a; y++) {
      for (int x = 0; x <= y; x++) {
        System.out.print("x");
      }
      System.out.print("\n");
    }
  }

  public static void main(String[] args) {

    int a = 5;
    trojkat(a);
  }
}

