/*
Tytul: Znalezienie brakujacego elementu w liscie.
Tresc: Dla dostarczonej listy, skladajacej sie z nieuporzadkowanych kolejnych (oprocz jednego) elementow ciagu arytmetycznego, znajdz brakujacy element.
Dane wejsciowe: Lista zawierajaca liczby naturalne.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej listy: [5, 2, 1, 3] zostanie zwrocona liczba: 4.

*/

public class Main {

  public static int znajdzMaksV1(int[] tablica) {

    int maks = tablica[0];

    for (int elem : tablica) if (elem > maks) maks = elem;

    return maks;
  }

  public static int znajdzMaksV2(int[] tablica) {

    int maks = tablica[0];

    for (int elem : tablica) maks = Math.max(maks, elem);

    return maks;
  }

  private static void test1() {
    int[] tablica = new int[] {3, 5, -7, 4, 9, -11, 2};
    int wynik = 9;

    assert znajdzMaksV1(tablica) == wynik;
    assert znajdzMaksV2(tablica) == wynik;
  }

  private static void test2() {
    int[] tablica = new int[] {3, -2, 4, 29, -3, -40, 8, 5, -7, -1};
    int wynik = 29;

    assert znajdzMaksV1(tablica) == wynik;
    assert znajdzMaksV2(tablica) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

