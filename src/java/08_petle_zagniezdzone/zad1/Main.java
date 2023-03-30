/*
Tytul: Kwadrat
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze kwadrat o boku rownym tej liczbie.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 2 powinno zostac wypisane:
**
**

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanej liczby
  // wypisze kwadrat o boku rownym otrzymanej liczbie.

  public static void kwadrat(int a) {

    for (int y = 0; y < a; y++) {
      for (int x = 0; x < a; x++) {
        System.out.print("x");
      }
      System.out.print("\n");
    }
  }

  public static void main(String[] args) {

    int a = 5;
    kwadrat(a);
  }
}

