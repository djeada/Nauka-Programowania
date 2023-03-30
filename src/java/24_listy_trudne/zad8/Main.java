/*
Tytul: Sznurek.
Tresc: Masz do sprzedania sznurek o dlugosci n, a takze liste cen dla sznurkow o dlugosciach od 1 do n. Ceny moga byc rozne dla roznych dlugosci. Znajdz maksymalny zysk, ktory mozna osiagnac poprzez sprzedaz danego sznurka.
Dane wejsciowe: Lista n liczb calkowitych reprezentujacych ceny dla sznurkow o dlugosciach od 1 do n, oraz liczba naturalna n reprezentujaca dlugosc sznurka, ktory chcesz sprzedac.
Dane wyjsciowe: Najwieksza mozliwa wartosc, jaka mozna uzyskac ze sprzedazy danego sznurka.
Przyklad:
Dla listy cen: [1, 5, 8, 9, 10, 17, 17, 20] oraz dlugosci sznurka 4, powinna zostac zwrocona liczba 10.

*/
import java.util.*;

public class Main {

  public static int podzielSznurekV1(List<Integer> ceny, int n) {
    if (ceny.size() < n)
      throw new IllegalArgumentException(
          "Dlugosc sznurka do sprzedazy nie moze byc " + "wieksza od liczby elementow listy ceny.");

    if (n == 0) return 0;

    int maks = 0;

    for (int i = 0; i < n; i++) {
      int cena = ceny.get(i) + podzielSznurekV1(ceny, n - i - 1);

      if (cena > maks) maks = cena;
    }

    return maks;
  }

  public static int podzielSznurekV2(List<Integer> ceny, int n) {
    if (ceny.size() < n)
      throw new IllegalArgumentException(
          "Dlugosc sznurka do sprzedazy nie moze byc " + "wieksza od liczby elementow listy ceny.");

    List<Integer> pom = new ArrayList<>(n + 1);

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < i + 1; j++)
        pom.set(i + 1, Math.max(pom.get(i + 1), ceny.get(j) + pom.get(i - j)));
    }

    return pom.get(n);
  }

  public static void test1() {
    List<Integer> lista = Arrays.asList(1, 5, 8, 9, 10, 17, 17, 20);
    int n = 4;
    int wynik = 10;

    assert (podzielSznurekV1(lista, n) == wynik);
    assert (podzielSznurekV2(lista, n) == wynik);
  }

  public static void test2() {
    List<Integer> lista = Arrays.asList(3, 9, 10, 20);
    int n = 5;

    for (int funkcja : Arrays.asList(podzielSznurekV1, podzielSznurekV2)) {
      try {
        funkcja(lista, n);
        assert (false);
      } catch (Exception e) {
        assert (true);
      }
    }
  }

  public static void test3() {
    List<Integer> lista = Arrays.asList(5);
    int n = 1;
    int wynik = 5;

    assert (podzielSznurekV1(lista, n) == wynik);
    assert (podzielSznurekV2(lista, n) == wynik);
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

