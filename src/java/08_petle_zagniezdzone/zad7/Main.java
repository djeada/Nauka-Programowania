/*
Tytul: Choinka.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N trojkatow ustawionych w kolumnie, jeden na drugim. Wysokosc pierwszego trojkata to 1, a kazdego nastepnego jest rowna wysokosci poprzedniego powiekszonej o 1.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 3 powinno zostac wypisane:
*
*
**
*
**
***

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanej liczby
  // wyswietli N trojkatow. Trojkaty powinny byc
  // ustawione w kolumnie, jeden na drugim. Wysokosc
  // pierwszego trojkata to 1, a dla kazdego nastepnego
  // rowna jest wysokosci poprzedniego powiekszonej o 1.

  public static void trojkat(int a) {

    for (int y = 0; y < a; y++) {
      for (int x = 0; x <= y; x++) {
        System.out.print("*");
      }
      System.out.print("\n");
    }
  }

  public static void choinka(int n) {

    for (int i = 1; i <= n; i++) {
      trojkat(i);
    }
  }

  public static void main(String[] args) {

    int a = 5;
    choinka(a);
  }
}

