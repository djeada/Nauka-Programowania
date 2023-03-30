/*
Tytul: Wyszukiwanie liniowe rekurencyjnie.
Tresc: Otrzymujesz liste liczb naturalnych oraz liczbe naturalna klucz. Przy uzyciu rekurencji znajdz indeks odpowiadajacy pierwszemu wystapieniu klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych oraz liczba naturalna klucz.
Dane wyjsciowe: Liczba calkowita.
Przyklad:
Dla otrzymanej listy oraz liczby: [1, 2, 2] i 2, powinna zostac zwrocona liczba: 1.

*/
public class Main {

  public static int ciagV1(int n) {

    if (n == 1) {
      return 1;
    }

    return 1 + ciagV1(n - 1) * 2;
  }

  public static void test1() {
    int n = 5;
    int wynik = 31;

    assert ciagV1(n) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

